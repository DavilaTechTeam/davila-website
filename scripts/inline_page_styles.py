#!/usr/bin/env python3
"""Inline page-used CSS without adding stylesheet requests.

Run after editing page markup or assets/css sources.
Requires: tinycss2, cssselect2, lxml. GitHub Pages serves the resulting HTML;
this maintenance script is not a production runtime dependency.
"""
from pathlib import Path
import re
import tinycss2
import cssselect2
from lxml import html

ROOT=Path(__file__).resolve().parents[1]
LINK=re.compile(r'<link\s+rel="stylesheet"\s+href="/(assets/css/[^"]+)"\s*/?>')
INLINE=re.compile(r'<style data-source-styles="([^"]+)">.*?</style>',re.S)

def page_css(source,nodes):
    out=[]
    for rule in tinycss2.parse_stylesheet(source,skip_comments=True,skip_whitespace=True):
        if rule.type=='qualified-rule':
            selector=tinycss2.serialize(rule.prelude).strip()
            # Keep pseudo states/elements, and form styles that an embed may use.
            keep=bool(':' in selector or re.search(r'\b(?:input|textarea|select|label|form)\b|\.form|\.choice|\.upload|\.submit',selector))
            if not keep:
                try:
                    selectors=cssselect2.compile_selector_list(rule.prelude)
                    keep=any(s.test(n) for s in selectors for n in nodes)
                except cssselect2.SelectorError:
                    keep=True  # Unknown selectors are preserved, never discarded.
            if keep:out.append(tinycss2.serialize([rule]))
        elif rule.type=='at-rule' and rule.lower_at_keyword=='media' and rule.content is not None:
            nested=page_css(tinycss2.serialize(rule.content),nodes)
            if nested:out.append('@media '+tinycss2.serialize(rule.prelude).strip()+'{'+nested+'}')
        else:
            out.append(tinycss2.serialize([rule]))
    return ''.join(out)

def main():
    total_before=total_after=0;pages=0
    for path in sorted(ROOT.glob('*.html')):
        source=path.read_text();links=list(LINK.finditer(source));inline=INLINE.search(source)
        if not links and not inline:continue
        names=[m[1] for m in links] if links else inline[1].split()
        wrapper=cssselect2.ElementWrapper.from_html_root(html.fromstring(source))
        nodes=list(wrapper.iter_subtree())
        full='\n'.join((ROOT/name).read_text() for name in names)
        result=page_css(full,nodes)
        tag='<style data-source-styles="'+' '.join(names)+'">'+result+'</style>'
        if links:
            first=True
            def emit(m):
                nonlocal first
                if first:first=False;return tag
                return ''
            updated=LINK.sub(emit,source)
        else:updated=INLINE.sub(lambda m:tag,source,count=1)
        path.write_text(updated)
        pages+=1;total_before+=len(full.encode());total_after+=len(result.encode())
    print(f'{pages} pages: {total_before:,} full-source CSS bytes -> {total_after:,} page-used inline CSS bytes; no stylesheet requests.')

if __name__=='__main__':main()

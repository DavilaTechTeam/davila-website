# SEO direction for Davila & Associates

Confirmed by Joaquin on October 19, 2026: the objective is nationwide U.S. visibility, not a McAllen-only campaign.

Use the homepage for the broad nationwide language-service proposition. Use document, certified, legal, academic and language-direction pages for their distinct customer needs. Keep McAllen as the truthful office location and retain the local landing page. Describe in-person work by location and availability; do not imply an office or guaranteed staffing in every state. Avoid copied city pages, invented credentials, unsupported acceptance guarantees and keyword stuffing.

## Maintenance

- Keep each indexable page's title, description and canonical URL unique and accurate.
- Keep visible FAQs and JSON-LD synchronized. Structured data is descriptive; it does not guarantee rich results or rankings.
- Update sitemap lastmod only when substantive page content changes.
- Keep confirmation/error pages out of the index and sitemap.
- GitHub Pages publishes the root of main. It cannot configure per-path HTTP 301 rules here. The legacy videography path and archived homepage use instant meta refresh plus a canonical and a visible fallback link. Google documents instant meta refresh as a permanent-redirect signal. The retired social-media URL has no equivalent successor and intentionally remains HTTP 404, now with helpful navigation.
- Preserve the existing HubSpot intake and tracking scripts. A Google Analytics measurement ID has not been verified; do not fabricate one.

## October 19 implementation

Nationwide homepage and document-service messaging; distinct Spanish-to-English and English-to-Spanish content; direct service links in footers; article canonical/social metadata and Article/Breadcrumb markup; service breadcrumbs and synchronized FAQs; index protection for the thank-you page; legacy URL handling; shared logo asset instead of repeated base64 copies.

## Measurement still needed

Use Search Console to compare the last complete 28 days with the preceding 28 days, filtered to the United States. Record non-branded clicks, impressions, CTR, positions, queries and landing pages. Inspect indexing and submit the sitemap if needed. Confirm conversions through the existing HubSpot setup and verify whether Google Analytics is connected. Search Console was accessed after deployment; the baseline and indexing actions are recorded below. Google Analytics remains unverified. No ranking gain is claimed at deployment.

Re-run duplicate-content and mobile performance checks after recrawling. Prior audit baseline (October 15): 20% duplicate content; that historical percentage is not a result of today's edits. Prior Semrush figures were estimates, not first-party traffic.

## SpyFu audit follow-up

The October 19 12:22 PM crawl predates these changes: 99 health, 8 error occurrences, 90 warnings, 37 notices, 38 unpublished suggested fixes. Its duplicate-title group is the homepage at / and /index.html. Both identify / as canonical. Internal home links now use / consistently; GitHub Pages still serves /index.html as the same resource. Do not give those URLs different page content just to satisfy a duplicate alert. Article social cards/favicon declarations and concise titles/descriptions were completed after reviewing the report. Keyword-match warnings depend on SpyFu target assignments and require intent review before changing copy.

## Search Console follow-up — October 19, 2026

Nationwide measurement baseline: Web search, United States, September 20–October 17, 2026: 25 clicks, 1,723 impressions, 1.5% CTR, average position 15.2. All-country totals for that same period: 29 clicks, 2,161 impressions, 1.3% CTR, average position 17.6. These dates predate the SEO changes and do not establish a ranking gain.

The page indexing report (updated October 11) listed 22 indexed and 7 excluded URLs. The academic-document and birth-certificate service URLs were discovered but not indexed. Google accepted individual indexing requests for both on October 19; acceptance is not confirmation of indexing. The HTTPS sitemap was resubmitted successfully on October 19 (18 discovered pages; last-read display still October 16 immediately after submission).

The remaining excluded URLs were three normal HTTP/non-www homepage redirects, the retired /industries URL, and the retired /free-quote URL. Live requests confirmed the last two returned 404. They now use instant meta refresh redirects with fallback links to the existing homepage industries and quote sections. They stay out of the sitemap. These are HTML redirects, not configurable HTTP 301s on this host.

A fresh SpyFu crawl was started October 19 at 3:37 PM Central (task db60731f-e44c-4bc7-8e17-8e24b00fba5f). Its initial display showed 18 pages crawled, health 100, 0 errors, 18 warnings and 25 notices; after keyword analysis populated, the final count was 64 warnings and 25 notices (previous screenshot: health 99, 8 errors, 90 warnings, 37 notices). Final warnings included keyword/title/H1 suggestions, social text suggestions, one long meta description, two keyword-overlap targets and text-to-code ratio; notices covered optional image title attributes and readability. SpyFu also says some pages could not be processed; its AI suggestions are not automatically approved or published. The two legacy redirects were deployed after this crawl and are not included in those results. The three corrected audit targets are English-to-Spanish translation services, certified translation services, and legal document translation services.

## Nationwide keyword implementation — October 19, late evening

See SEO-KEYWORD-MAP.md for the 18-page editorial target map, purpose boundaries and measurement limits. Titles and main headings now describe each page’s distinct purpose. Added document-specific preparation, certification/delivery questions and cross-links; general interpreting focuses on meeting logistics while legal interpreting owns proceeding needs. Social text and applicable Service/Article metadata match the revised page descriptions. Source verification does not establish that the two SpyFu overlap flags are cleared; a fresh audit is still required.

## Verification completed — October 20, 2026, overnight

The browser was reconnected and SpyFu sign-in restored. All 18 primary targets were saved and confirmed against this map in the live UI. A clean follow-up crawl was started at 12:02 AM Central after the assignments were completed: task a322f5d8-dd04-4355-ab15-935384fe628f. It completed with 18/18 pages, health 100, 0 errors, 16 warnings and 22 notices. The refreshed overview and its issue list agreed on these counts. No missing-target-title or missing-target-H1 issue was listed.

Warning breakdown: title improvement suggestions 2; meta description improvement suggestions 2; Open Graph text improvement suggestions 2; keyword-overlap targets 3; H1 improvement suggestion 1; low text-to-code ratio 6. Notices: optional image title attributes on 18 pages; readability on 4 pages. The three overlap targets were certified translation, interpreting and marriage certificate translation; all showed Already linked / Remedy in place, with 0 fixable rows. This does not mean every related page has ceased to rank for the same phrase.

SpyFu also displayed “Some pages could not be processed” for its suggestions. The crawl completed, but the AI recommendation coverage is incomplete; the reduced suggestion count is not evidence of a ranking gain. The final count differs from the earlier 11:57 PM run, which had processed older targets while assignments were being updated. No automatic SpyFu suggestions were published.

Search Console live tests on October 19 at 11:55–11:56 PM reported both academic-document and birth-certificate service pages available to Google and eligible for indexing, with one valid Breadcrumb item on each. The Google-index view still reported both as not indexed, with no recorded crawl. Individual indexing requests had already been accepted earlier that day. The sitemap showed Success, 18 discovered pages, and an updated last-read date of October 19. This verifies accessibility and discovery, not completed indexing or rankings.

## Remaining-issue cleanup — October 20, 2026

Reviewed the final 12:02 AM audit drilldowns. Its two title suggestions requested the full company brand on the document hub and Spanish-to-English page. Its H1 suggestion only removed punctuation; the actual edit made the Spanish-to-English heading more specific to official records. Updated the two descriptions and matching social/Service metadata for clearer intake and nationwide coordination.

Moved 34 existing inline stylesheet blocks from 19 pages into five shared, content-hashed assets under assets/css. Every CSS block and its cascade order were verified byte-for-byte against the previous commit. No relative CSS resource URLs were present. Across those pages, HTML fell from 739,726 to 289,188 bytes (450,538 fewer HTML bytes). The five CSS files total 58,473 bytes and can be reused across pages; this is a source-size measurement, not a Core Web Vitals or ranking result. Keep hashed file names and HTML references synchronized when changing CSS.

Simplified the certified service, certified-translation guide, legal interpreting and legal videography copy into shorter sentences. Visible FAQ answers and JSON-LD were synchronized. The certified guide links to the American Translators Association’s explanation of certified translation; it does not claim ATA membership or certification. Existing image sources and alt text were preserved and descriptive title hover labels added. Existing scripts, HubSpot intake and tracking were verified unchanged.

The three overlap flags already showed Remedy in place. Google indexing remains a search-engine decision; passing a live test and submitting an indexing request do not confirm indexing. A post-publication audit is needed to measure the effect of this cleanup on SpyFu flags.

### Stylesheet-loading adjustment

The post-cleanup crawl cleared all 22 prior notices and the low text-to-code flags, but identified external stylesheet loading as render-blocking. The final approach keeps the full CSS source assets and uses scripts/inline_page_styles.py to emit only page-used rules inline. It preserves all pseudo-state/element rules, all form rules, unsupported selectors, media conditions and the original order of retained rules. No stylesheet request is needed by the published HTML. Re-run the script after changing markup or CSS; it requires tinycss2, cssselect2 and lxml. The full-source styles remain referenced by data-source-styles for reproducibility. This supersedes the intermediate external-loading approach above.

### Final loading correction deployed and verified

Commit 4c7fba324bf6b44296c89b92348b54b2134ebf21 deployed successfully. The final 19 HTML pages total 502,518 bytes versus 739,726 at the start of this cleanup (237,208 fewer HTML bytes). They issue no stylesheet requests. The original CSS source assets are maintained for regeneration. Browser comparison of 46 measured elements across the homepage, certified service and certified guide found no changes to measured layout, font, spacing or colors. Live HTTP responses for all three exactly matched the final source. Scripts, source images, alt text, intake, canonicals and structured data passed their checks.

The 12:16 AM crawl (9a1cc662-6c76-47b8-802a-5dcd88641df7) showed 0 notices: image-title and readability flags cleared, and low text-to-code warnings were absent. It newly flagged external CSS loading on 18 pages. That finding motivated the final inline page-used CSS approach, not an attempt to hide CSS loading with JavaScript or a broken no-script fallback.

A final verification crawl was started October 20 at 12:25 AM Central (fc05e53e-fda0-42f4-8c8e-0fd9b8881713). All 18 pages were crawled; at the latest check the AI-writing stage was still running. Do not treat earlier warning totals as the final result of this revision or claim a search-ranking gain from tool scores. SpyFu’s Published counter tracks its own publishing workflow, not these direct GitHub deployments.

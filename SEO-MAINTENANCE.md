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

# Tech & SaaS Stack — Affiliate Blog

**Purpose:** Autonomous affiliate content site publishing SEO-optimized web hosting & SaaS comparisons.

## Quick Start

- **Live:** https://techsaasstack.com (custom domain)
- **Fallback:** https://fellowizsick.github.io/tech-saas-stack/
- **Repo:** https://github.com/fellowizsick/tech-saas-stack
- **Framework:** Jekyll (GitHub Pages native)
- **Local path:** `C:\Users\1990j\blog\`
- **Owner:** Jon Brown / fellowizsick

## Commands

- **Preview locally:** `cd /c/Users/1990j/blog && bundle exec jekyll serve`
- **Build:** Pushed to `main` branch → GitHub Actions auto-deploys
- **New post:** `_posts/YYYY-MM-DD-slug.md` with Jekyll frontmatter
- **Git push:** `cd /c/Users/1990j/blog && git add -A && git commit -m "msg" && git push origin main`

## Cron Jobs

| Job | Schedule | Purpose |
|-----|----------|---------|
| `d3b6a8f5127f` (affiliate-content-engine) | Every 8h | Researches keyword → writes 2000+ word article → commits → deploys |
| `1f97082738ed` (deals-updater) | Daily 3AM | Verifies links, updates pricing, adds new programs |
| `353d74ca169a` (indexnow-ping) | Daily 2AM | Submits sitemap to Bing/Yandex |

## Site Stats

- **73 posts live** (as of Jun 28 2026)
- **6 active affiliate programs:** InterServer (r/1155259), Cloudways (id=2179745), SiteGround (/go/affiliate), ScalaHosting (?aid=jon), Bluehost (Impact Radius), Kinsta (?ref=jon)
- **Custom domain:** techsaasstack.com (Namecheap, ~$1/yr)
- **Google Analytics:** G-RLHP59H7Z2
- **Google Search Console:** Verified (HTML tag)
- **IndexNow key:** `924c5f4229bef1e57d26850c89e21708`

## Key Files

- `_config.yml` — Site config (url, baseurl, plugins, SEO)
- `_layouts/default.html` — Main layout (nav, footer, analytics, schema)
- `_layouts/post.html` — Post layout (affiliate disclosure, related articles, CTAs)
- `assets/css/style.css` — Full design system (OKLCH colors, glass morphism, dark mode)
- `assets/css/responsive.css` — Mobile/hamburger menu styles
- `best-deals.md` — Deals comparison page (4 copies in 2 repos)
- `_posts/` — All published articles
- `robots.txt` — Sitemap URL for custom domain
- `_headers` — Security headers
- `privacy.md` — Privacy policy

## Content Rules

- Use raw HTML `<table>` tags for comparisons (Jekyll strips pipe tables in HTML wrappers)
- Every post needs inline `<div class="disclosure-bar">` at top
- Affiliate links must return HTTP 200 when curl'd
- No markdown pipe tables inside HTML tags
- `future: true` in config (posts publish immediately)
- Permalink format: `/:year/:month/:title/`

## Affiliate Programs (Active)

| Program | ID | Link Format |
|---------|----|-------------|
| InterServer | `1155259` | `https://www.interserver.net/r/1155259` |
| Cloudways | `2179745` | `https://www.cloudways.com/en/?id=2179745` |
| SiteGround | `/go/affiliate` | `https://www.siteground.com/go/affiliate` |
| ScalaHosting | `?aid=7ff57600` | `https://scalahosting.com/?aid=7ff57600` |
| Bluehost | Impact Radius | `https://bluehost.sjv.io/c/7392811/1376228/11352` |
| Kinsta | `?ref=jon` | `https://kinsta.com/?ref=jon` |

## Known Issues

- 🔴 Kinsta/Hostinger/WP Engine — reapplying with custom domain
- 🔴 Bluehost/Cloudways/InterServer Cloudflare-protected — can't auto-pull pricing
- 🔴 Awin onboarding — verification tag added, awaiting dashboard completion
- ⏸️ Blog strategy research cron is paused (job `8678e4ac9ee7`)

## Engineering Loop

This project follows the autonomous self-improvement cycle:
STUDY → PLAN → EXECUTE → VERIFY → LEARN

New content fills gaps identified by `ls _posts/ | grep -i "topic"` checks. Roundup format when head-to-head pairings exhausted.

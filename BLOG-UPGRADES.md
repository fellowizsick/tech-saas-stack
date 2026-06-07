# Blog Upgrades — Implementation Log
**Date:** June 6, 2026
**Blog:** Tech & SaaS Stack (fellowizsick.github.io/tech-saas-stack)

---

## Changes Made

### ✅ Email Capture (ConvertKit-ready)
- Added signup form to **bottom of every post** (`_layouts/post.html`)
- Added signup form to **homepage** (`index.html`)
- Form submits to ConvertKit — update `SUBSCRIPTION_ID` when account is created
- Styled with blue gradient background, clean input + button

### ✅ FAQ Schema (SEO)
- Added JSON-LD FAQPage schema to `_layouts/default.html`
- Triggered by `faq:` frontmatter in posts — just add Q&A pairs
- Gets featured snippets on Google

### ✅ Coupon / Deals Page
- **New page:** `/deals/` — 7 affiliate deals with cards, discounts, CTAs
- Added to **nav bar** and footer
- Deal cards highlight on hover, show discount badges
- Update affiliate IDs when approved

### ✅ Lead Magnet (Hosting Decision Checklist)
- **New page:** `/hosting-checklist/` — decision matrix + scoring table
- Printable format for reader downloads
- Links to flagship comparison post

### ✅ Footer & Nav Updates
- Deals page link in nav bar (after category links)
- Email capture form in footer of posts

---

## Setup Notes When ConvertKit is Ready

1. Create free ConvertKit account
2. Create a form → copy the form action URL
3. Replace `SUBSCRIPTION_ID` in:
   - `_layouts/post.html` (line ~36)
   - `index.html` (line ~87)
4. Create an automation: new subscriber → email them the checklist link

---

## Cron Prompt Update Needed

The cron prompt should now add these instructions:
- For every post: link to 5+ existing posts (was 2-3)
- If comparison post: add `faq:` frontmatter with 4-6 Q&A
- At bottom of every post: link to `/deals/` and `/hosting-checklist/`

---

## Research Reference

Top blogs (WPBeginner, Backlinko, Authority Hacker) differentiate by:
1. Email-first strategy (lead magnets, nurture sequences)
2. Coupon/deals pages (3-5x conversion vs standard posts)
3. Custom visuals in every post
4. Topic clustering (15-30 posts per pillar topic)
5. Heavy internal linking (5-15 links per post)

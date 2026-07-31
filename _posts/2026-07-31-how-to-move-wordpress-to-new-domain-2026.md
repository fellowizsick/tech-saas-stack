---
layout: post
title: "How to Move WordPress to a New Domain Without Losing SEO (2026 Guide)"
description: "Step-by-step guide to move WordPress to a new domain in 2026 without losing SEO. Learn how to migrate files and database, set up 301 redirects, and use Google Search Console's change of address tool."
date: 2026-07-31 10:00:00 -0500
categories: [WordPress, Tutorials]
---

<div class="disclosure-bar">
  <strong>Disclosure:</strong> Some links in this post are affiliate links. If you purchase through them, I may earn a commission at no additional cost to you. All recommendations are based on research and publicly available information.
</div>

Rebranding your business, switching from a `.net` to a `.com`, or finally buying the domain that matches your brand — there are plenty of good reasons to move WordPress to a new domain. The scary part isn't the move itself. It's the fear of watching your Google rankings, organic traffic, and hard-earned domain authority evaporate overnight.

Here's the good news: **you can move WordPress to a new domain without losing SEO**, as long as you do it in the right order. The process takes a few hours of careful work and a bit of patience while search engines re-crawl your site. Miss a step — especially the 301 redirects — and you can lose a meaningful share of your organic traffic for months.

This guide walks through the entire WordPress domain migration process: prepping your backups, migrating your files and database, swapping every hardcoded URL, building bulletproof redirects, and telling Google exactly what changed. By the end, your new domain will be positioned to keep most — in many cases all — of your existing rankings.

## What Actually Happens When You Change a WordPress Domain

Before touching anything, it helps to understand what's really going on. When you change your WordPress domain, three separate things break simultaneously:

1. **The site itself** — WordPress stores your domain in the database (`wp_options` table) and across your content. Pointing the domain at a fresh install without updating these references produces a site with broken links, missing images, and a white screen.
2. **Your SEO equity** — Every backlink, social share, and bookmark pointing at your old domain stops counting toward you the moment the old site goes away. Search engines treat the old domain and new domain as completely different websites unless you explicitly connect them.
3. **Your integrations** — Email services, payment gateways, analytics, CDNs, and newsletter tools usually have your old URL baked into their configuration.

The redirect strategy in Step 6 is what preserves your SEO equity. Everything else is housekeeping that keeps the site functional. Handle both halves and the move is boringly smooth.

## Prerequisites: What You Need Before You Start

- **Access to your old hosting account** (cPanel, hPanel, or your host's custom panel) and your **new hosting account**
- **Control of your domain registrar** — both the old domain's DNS and the new domain's settings
- **A full backup** of your WordPress files and database (if you don't have one, stop here and read our [WordPress backup guide](/2026/07/how-to-back-up-wordpress-site-2026/) first)
- **An SEO baseline** — export your current rankings or note your top 20 URLs. You'll compare against this after the move
- **3-4 hours of mostly hands-off time** — DNS propagation alone takes up to 48 hours to fully settle worldwide

## Step 1: Pick the Right Hosting for the New Domain

You can move to a new domain on your existing hosting, but this is also the natural moment to evaluate whether your host is still the right fit — especially if you're upgrading the brand alongside the domain. If you're weighing providers, a managed WordPress host removes most of the migration complexity below.

<a href="https://www.cloudways.com/en/?id=2179745" rel="nofollow sponsored" target="_blank">Cloudways</a> gives you a staging environment by default, which is ideal for a domain migration: you build and test the entire new site in staging, swap the domain, and only cut over when everything checks out. Their Cloudways Migrator plugin handles sites up to 5GB with real-time progress tracking.

<a href="https://www.siteground.com/go/affiliate" rel="nofollow sponsored" target="_blank">SiteGround</a> includes a free WordPress migration plugin and lets you park an additional domain alongside your existing site, which makes the transition period less stressful — your old domain keeps working while you prepare the new one.

If you'd rather have a human handle the heavy lifting, <a href="https://scalahosting.com/?aid=7ff57600" rel="nofollow sponsored" target="_blank">ScalaHosting</a> assigns a professional migration team to every managed VPS plan, and their SPanel makes managing multiple domains straightforward. On a budget, <a href="https://www.interserver.net/r/1155259" rel="nofollow sponsored" target="_blank">InterServer</a> offers free migration assistance on standard hosting plans — a solid option if you're consolidating costs during the rebrand.

Whichever route you choose, sign up for the new host **before** you start migrating. You need the new server ready to receive the site.

## Step 2: Point Your New Domain at the New Host

With the new hosting account ready, connect your new domain to it:

1. Log in to your **domain registrar** (Namecheap, GoDaddy, Cloudflare, etc.) and find DNS management for the new domain
2. Update the **A record** to your new host's server IP (your host's dashboard lists the exact IP or nameservers to use)
3. If your host provides custom **nameservers**, point the domain at those instead
4. If you bought the new domain *from* your registrar as a transfer, make sure it's fully unlocked and verified

DNS changes propagate gradually — anywhere from a few minutes to 48 hours. You don't have to wait for propagation to finish before continuing; you'll test the new site via its temporary URL (every host provides one, e.g., `temp.yourhost.com/yourdomain`) or by editing your local `hosts` file.

## Step 3: Migrate Your Files and Database

This is the same process as a normal [WordPress host migration](/2026/07/how-to-migrate-wordpress-site-new-host-2026/), but with one extra consideration: you're not just moving data, you're moving it to a new identity. Choose one of these three methods:

### Method A: Migration Plugin (Easiest)

Most managed hosts provide a free migration plugin — Cloudways Migrator, SiteGround Migrator, and similar. Install the plugin on your old site, enter your new site's temporary URL or credentials, and let it move files, database, and settings in one pass.

**Best for:** Most sites under 2-5GB, especially beginners.

### Method B: Manual Transfer (Most Control)

1. Export the database from your old host (phpMyAdmin → Export, or `wp db export` via [WP-CLI](/2026/07/how-to-use-wp-cli-wordpress-2026/))
2. Download your entire `wp-content` folder and WordPress core via FTP or file manager
3. Upload everything to the new server, creating a fresh `wp-config.php` with the new database credentials
4. Import the database on the new host, then run a search-and-replace on URLs (Step 5)

**Best for:** Sites with custom server configs, or when you want full control over every file.

### Method C: Professional Migration Support (Safest for Complex Sites)

If you're running an ecommerce store, membership site, or a site with a large media library, let the new host's migration team do it. Most managed hosts include this free — it's worth taking them up on it even if you're technical, because they've seen every edge case (custom `.htaccess` rules, non-standard database prefixes, multisite networks).

**Best for:** Complex sites, or anyone migrating during a busy business period.

<table class="comparison-table">
  <thead>
    <tr>
      <th>Method</th>
      <th>Skill Level</th>
      <th>Time</th>
      <th>Cost</th>
      <th>Best For</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Migration plugin</td>
      <td>Beginner</td>
      <td>30-60 min</td>
      <td>Free (with managed hosts)</td>
      <td>Sites under 5GB, most bloggers</td>
    </tr>
    <tr>
      <td>Manual transfer</td>
      <td>Intermediate</td>
      <td>1-3 hours</td>
      <td>Free</td>
      <td>Full control, custom configs</td>
    </tr>
    <tr>
      <td>Host migration team</td>
      <td>None required</td>
      <td>24-48 hours</td>
      <td>Free (most managed hosts)</td>
      <td>Ecommerce, complex or large sites</td>
    </tr>
  </tbody>
</table>

Whichever method you pick, **do not delete the old site yet**. You need it live for the redirects in Step 6.

## Step 4: Update Every WordPress URL Reference

Now the part that trips people up. WordPress stores URLs in dozens of places — not just in Settings, but inside post content, widgets, theme customizer values, and plugin options.

1. **Settings → General** — Update the WordPress Address (URL) and Site Address (URL) to the new domain. Do this *before* you log into the site on the new domain, or WordPress will redirect you back to the old one.
2. **Search-and-replace the database** — Old URLs hide inside post bodies (`wp_posts`), post meta, options, and `wp_commentmeta`. Run a search-and-replace that swaps every instance of `https://olddomain.com` with `https://newdomain.com`.
   - The **Better Search Replace** plugin does this safely without touching serialized data incorrectly
   - **WP-CLI** users: `wp search-replace 'https://olddomain.com' 'https://newdomain.com' --all-tables --precise`
3. **Theme customizer & widgets** — Check custom logo URLs, menus, footer text, and any hardcoded links in your theme
4. **Plugins with stored URLs** — Email marketing integrations, payment gateways, and CDN plugins often store the site URL in their settings. Re-save them with the new domain.

A search-and-replace handles most of this automatically, but a manual pass through your theme's `header.php` and `footer.php` is worth the ten minutes — hardcoded URLs there survive database replacements.

## Step 5: The SEO Lifesaver — 301 Redirects

This is the single most important step of the entire process. **301 redirects tell search engines — permanently — that your old URLs have moved.** Without them, Google treats the new domain as a brand-new site with zero authority, and every backlink you've earned over the years is wasted.

### The Wildcard Redirect (Simplest, Most Reliable)

Redirect every URL on the old domain to the matching URL on the new domain:

- **With an `.htaccess` file** (Apache servers), add this at the top:

```apache
RewriteEngine On
RewriteRule ^(.*)$ https://newdomain.com/$1 [R=301,L]
```

- **With nginx**, add a `server` block for the old domain containing:

```nginx
location / {
    return 301 https://newdomain.com$request_uri;
}
```

- **With Cloudflare**, add a Bulk Redirect rule mapping `olddomain.com/*` → `newdomain.com/$1` with status 301.

### Redirect Plugins

If you'd rather not touch server config files, plugins like Redirection or Rank Math's redirect module let you build 301 rules from the WordPress dashboard. The `^/(.*)` wildcard pattern achieves the same result.

### The One-Way Road

Never use 302 (temporary) redirects for a permanent domain change, and never redirect new → old. A 302 tells search engines the move is temporary and they should keep ranking the old URLs — the opposite of what you want. If you're consolidating two sites into one domain, build explicit per-URL redirects for the top pages instead of a blanket wildcard.

**Keep the old domain live for at least 6-12 months.** Search engines need multiple crawl cycles to fully transfer signals. Renew it for another year — it's the cheapest insurance policy your SEO will ever have.

## Step 6: Set Up SSL on the New Domain

A new domain needs its own SSL certificate, and in 2026 an HTTPS-only site is table stakes for rankings and trust.

1. Most hosts provide free Let's Encrypt or AutoSSL certificates — enable it in your hosting dashboard for the new domain
2. If your host charges for SSL, that's a signal to look elsewhere; every host recommended in this guide includes free SSL
3. After enabling it, force HTTPS with a redirect so every visitor and crawler lands on `https://newdomain.com` (not `http://`)

Mixed content (HTTPS page loading HTTP images or scripts) is a common post-migration issue — most browsers block it, breaking images and sliders. A plugin like Really Simple SSL handles both the force-HTTPS redirect and mixed-content fixes automatically. More on this in our [SSL setup guide](/2026/07/how-to-set-up-ssl-wordpress-2026/).

## Step 7: Tell Google — Search Console Change of Address

This is the step most people skip, and it's the one that makes the biggest difference to how fast Google transfers your rankings.

1. **Verify the new domain** in Google Search Console (add the property, then add the DNS TXT or HTML tag verification)
2. **Verify the old domain** — you must own both properties for the change of address tool to work
3. In the **old domain's property**, go to Settings → Change of Address, select the new property, and confirm
4. **Resubmit your sitemap** (`/sitemap.xml` or `/sitemap_index.xml`) in the new property
5. Submit the same **URL Inspection requests** for your top pages so Google re-crawls them quickly
6. Set up a **redirect chain monitor** — search for `site:olddomain.com` weekly and confirm Google is dropping old URLs from the index

If you use Bing Webmaster Tools or Yandex, do the same there — the change-of-address concept works identically. And update the **canonical URLs** in your SEO plugin ([WordPress SEO setup guide](/2026/07/how-to-set-up-wordpress-seo-2026/) covers the rest of your on-page settings) so every page declares the new domain as its canonical home.

## Step 8: Update Everything That Points at Your Old Domain

Your website isn't the only thing that knows your old URL. Work through this checklist:

<table class="comparison-table">
  <thead>
    <tr>
      <th>Where</th>
      <th>What to Update</th>
      <th>Priority</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Social profiles</td>
      <td>Bio links, pinned posts, link-in-bio tools</td>
      <td>High</td>
    </tr>
    <tr>
      <td>Email signature &amp; newsletters</td>
      <td>Signature URL, saved email templates, automation links</td>
      <td>High</td>
    </tr>
    <tr>
      <td>Payment providers</td>
      <td>Stripe, PayPal, WooCommerce return/cancel URLs</td>
      <td>High</td>
    </tr>
    <tr>
      <td>Business listings</td>
      <td>Google Business Profile, Yelp, directories</td>
      <td>Medium</td>
    </tr>
    <tr>
      <td>CDN &amp; email delivery</td>
      <td>Cloudflare zone, SPF/DKIM records, newsletter provider domain</td>
      <td>Medium</td>
    </tr>
    <tr>
      <td>Old blog posts</td>
      <td>Update internal links pointing to your own old domain</td>
      <td>Medium</td>
    </tr>
  </tbody>
</table>

Email deliverability deserves a special mention: your newsletter provider (Mailchimp, ConvertKit, etc.) keys deliverability to your sending domain. If you move to a new domain, re-verify it and update your SPF, DKIM, and DMARC records — otherwise your emails can land in spam and quietly destroy your list engagement.

## Step 9: Verify, Monitor, and Troubleshoot

After the cutover, run through this verification sequence:

1. **Browse your new site** in an incognito window — check the homepage, a blog post, a product page, and the search results page. Click every navigation link
2. **Test the old domain** — every old URL should land on its new-destination 301. Use `curl -I https://olddomain.com/any-page` and confirm a `301` status with the `Location` header pointing at the new URL
3. **Check for 404s** — Google Search Console's Coverage report will surface pages that fell through the redirect cracks over the next few days. Fix them as they appear
4. **Compare traffic** — check Google Analytics (here's how to [set up Google Analytics for WordPress](/2026/07/how-to-set-up-google-analytics-wordpress-2026/) if you haven't) and Search Console performance a week after the move. A short dip is normal; a cliff is a sign a redirect or search-and-replace step was missed
5. **Verify images and assets** — view source on a few pages and confirm media URLs point at the new domain

**Common post-migration problems and their causes:**

- **White screen / 500 error** — Usually a database connection issue (wrong credentials in `wp-config.php`) or a search-and-replace that corrupted serialized data
- **Images broken on HTTPS** — Mixed content; re-run the search-and-replace with `https://` included
- **Redirect loop** — A redirect rule on the old domain pointing back to itself, or the old domain's DNS still resolving to the new server
- **Login page redirecting to old domain** — The site URL in `wp_options` is still the old one; fix it directly in the database or via WP-CLI
- **Rankings dropping after 2-4 weeks** — Confirm the change of address in Search Console and check that you submitted the new sitemap

## How Long Does SEO Recovery Take?

Most sites see rankings stabilize within **4-8 weeks** of a clean domain migration, provided the 301s are in place, the change of address is submitted, and the new site is technically sound (fast, secure, crawlable). Smaller, less competitive keywords can recover in days; heavily competitive head terms can take a couple of months.

What you're doing during that window matters more than the calendar: keep publishing, keep building backlinks to the new domain, and keep an eye on the Coverage report. Google transfers authority through the redirects, but it also needs to see that the new domain is an active, legitimate home for the content.

## Final Checklist Before You Cut Over

- [ ] Full backup of files and database stored off-server
- [ ] New hosting account ready, new domain pointing at it
- [ ] WordPress migrated (files + database), URLs search-and-replaced
- [ ] 301 wildcard redirect live on the old domain, old domain renewed for another year
- [ ] SSL enabled and force-HTTPS working on the new domain
- [ ] Both domains verified in Google Search Console, change of address submitted
- [ ] Sitemap resubmitted, top pages re-crawled
- [ ] Analytics, email, payment, and social integrations updated
- [ ] Old site still live (don't delete it for 6-12 months)

## The Bottom Line

Moving WordPress to a new domain is a real project, but it's a mechanical one. Back up, migrate, search-and-replace, redirect, verify — five steps, each with well-worn tooling. The sites that lose SEO during a domain change are the ones that skipped the 301s or never told Google what happened. Do those two things properly and your new domain starts from a position of strength, not from zero.

If you're doing this as part of a rebrand, pair the migration with a hosting upgrade while you're at it. A <a href="https://www.cloudways.com/en/?id=2179745" rel="nofollow sponsored" target="_blank">managed platform like Cloudways</a> (staging makes the cutover nearly risk-free) or a <a href="https://www.siteground.com/go/affiliate" rel="nofollow sponsored" target="_blank">host like SiteGround</a> (free migration plugin and domain parking) both smooth the transition. Prefer a hands-off move? <a href="https://scalahosting.com/?aid=7ff57600" rel="nofollow sponsored" target="_blank">ScalaHosting's migration team</a> takes it off your plate, and <a href="https://www.interserver.net/r/1155259" rel="nofollow sponsored" target="_blank">InterServer</a> keeps the ongoing cost down. Whichever you choose, follow the steps above in order, and your rankings will follow you to the new domain.

**Related guides:**
- [How to Migrate Your WordPress Site to a New Host in 2026](/2026/07/how-to-migrate-wordpress-site-new-host-2026/) — Host-level migration methods
- [How to Set Up WordPress SEO in 2026](/2026/07/how-to-set-up-wordpress-seo-2026/) — On-page SEO settings after the move
- [How to Back Up Your WordPress Site in 2026](/2026/07/how-to-back-up-wordpress-site-2026/) — The backup strategy you need before touching anything

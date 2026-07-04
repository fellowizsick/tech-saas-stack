---
layout: post
title: "How to Set Up SSL for Your WordPress Site in 2026 (Step-by-Step Guide)"
date: 2026-07-03 14:00:00 -0500
categories: [tutorials, wordpress, web-hosting]
---

<div class="disclosure-bar">Disclosure: Some links in this post are affiliate links. If you purchase through them, I may earn a commission at no additional cost to you.</div>

If you're running a WordPress site and haven't set up SSL yet, you're leaving money, trust, and search rankings on the table. An SSL certificate encrypts the connection between your visitors and your server — the green padlock in the address bar that says "this site is secure." In 2026, Google Chrome flags every HTTP site as "Not Secure," and that warning alone can cut your conversion rate by 30% or more.

The good news? **Setting up SSL for WordPress is easier and cheaper than ever.** Almost every modern web host includes a free SSL certificate via Let's Encrypt or AutoSSL, and you can get it configured in under 15 minutes.

In this guide, I'll walk you through:

- What SSL actually does and why WordPress needs it
- How to check if your site already has SSL
- Four methods to set up SSL depending on your hosting provider
- How to configure WordPress to use HTTPS properly
- How to fix mixed content warnings (the most common SSL headache)
- How to verify your SSL setup is working correctly

Let's secure your site.

## What Is SSL and Why Does Your WordPress Site Need It?

SSL (Secure Sockets Layer) and its modern successor TLS (Transport Layer Security) create an encrypted tunnel between your visitor's browser and your web server. When SSL is active, any data exchanged — passwords, credit card numbers, form submissions, even browsing behavior — is scrambled and unreadable to anyone trying to intercept it.

Here's what happens when SSL is missing vs. present on a WordPress site:

<table class="comparison-table">
  <thead>
    <tr><th>Factor</th><th>Without SSL (HTTP)</th><th>With SSL (HTTPS)</th></tr>
  </thead>
  <tbody>
    <tr><td>Browser warning</td><td>"Not Secure" in address bar</td><td>Green padlock</td></tr>
    <tr><td>SEO ranking</td><td>Penalized by Google</td><td>Light ranking boost</td></tr>
    <tr><td>Form submissions</td><td>Data sent in plain text</td><td>Encrypted end-to-end</td></tr>
    <tr><td>Login security</td><td>Credentials visible on network</td><td>Encrypted transmission</td></tr>
    <tr><td>HTTP/2 support</td><td>Not available</td><td>Faster page loads</td></tr>
    <tr><td>Visitor trust</td><td>~85% of users would leave</td><td>Green padlock = trusted</td></tr>
    <tr><td>Payment processing</td><td>PCI compliance failure</td><td>PCI compliant</td></tr>
  </tbody>
</table>

Beyond the security and trust benefits, SSL also unlocks **HTTP/2** — a faster network protocol that multiplexes requests, reduces latency, and improves page load times. Without SSL, you cannot use HTTP/2, which means your site loads slower than it could.

## Prerequisites

Before we start the SSL setup, make sure you have:

- **A WordPress site** running on a web hosting plan (shared, VPS, or managed WordPress)
- **Access to your hosting control panel** (cPanel, Site Tools, or custom dashboard)
- **Admin access to your WordPress dashboard**
- **About 15 minutes** for the full setup

Already have a host but no WordPress yet? Check out our guide on [how to create a website from scratch](/2026/07/how-to-create-website-from-scratch-2026/) first.

## Step 1: Check If Your Site Already Has SSL

Before doing any work, check whether SSL is already active. Many hosts enable it automatically.

**Quick check:** Open your site in a browser and look at the address bar. If you see a padlock icon next to your URL, SSL is active. If you see "Not Secure," it's not.

**To verify programmatically:**

```bash
curl -sI https://yoursite.com | head -5
```

If this returns HTTP headers and your site loads, you have SSL available. If it returns nothing or a connection error, SSL is not set up yet.

You can also check with an online SSL checker like SSL Labs — enter your domain and it will show you the certificate details, expiry date, and any configuration issues.

## Method 1: Free SSL via Let's Encrypt (Works with Most Hosts)

Let's Encrypt is a free, automated, and open certificate authority. It's the most common way to add SSL to WordPress sites in 2026, and it's built into most modern hosting control panels.

### Method 1a: SiteGround (One-Click SSL)

<a href="https://www.siteground.com/go/affiliate" rel="nofollow sponsored" target="_blank">SiteGround</a> includes free Let's Encrypt SSL with all hosting plans through their custom Site Tools dashboard. It takes about 30 seconds to enable.

**Step-by-step:**

1. **Log into your SiteGround Client Area** and click your hosting account
2. **Go to Site Tools → Security → SSL Manager**
3. **Select Let's Encrypt** from the certificate type dropdown
4. **Choose your domain** (and any subdomains you want to secure)
5. **Click "Get"** — SiteGround automatically provisions and installs the certificate

SiteGround also offers an optional **Wildcard SSL** (covers all subdomains like blog.yoursite.com and shop.yoursite.com) if your plan supports it.

### Method 1b: InterServer (AutoSSL Included)

<a href="https://www.interserver.net/r/1155259" rel="nofollow sponsored" target="_blank">InterServer</a> includes cPanel with every hosting plan, which comes with AutoSSL — it provisions Let's Encrypt certificates automatically.

**Step-by-step:**

1. **Log into your InterServer cPanel** at my.interserver.net
2. **Find the "SSL/TLS Status"** icon under the Security section
3. **Click "Run AutoSSL"** — cPanel scans your domains and provisions certificates for any that are missing them
4. **Wait 30–60 seconds** for the process to complete
5. **Verify** — you should see a green "SSL installed" indicator next to each domain

The AutoSSL feature runs daily, so any new domains or subdomains you add will automatically get SSL within 24 hours with no manual action needed.

### Method 1c: ScalaHosting (SPanel SSL Manager)

<a href="https://scalahosting.com/?aid=7ff57600" rel="nofollow sponsored" target="_blank">ScalaHosting</a> uses their custom SPanel control panel, which includes a built-in SSL manager with free Let's Encrypt certificates.

**Step-by-step:**

1. **Log into SPanel** (yourdomain.com:8080 or the IP provided during setup)
2. **Go to SSL Certificates → Let's Encrypt**
3. **Select your domain** from the list
4. **Choose the SSL type** — single domain is sufficient for most sites
5. **Click "Issue"** — SPanel provisions the certificate automatically
6. **Enable "Auto-renewal"** (which is on by default) to ensure the certificate never expires

ScalaHosting also supports **AutoSSL** by default, so certificates are provisioned automatically when you first set up a domain.

### Method 1d: Cloudways (One-Click SSL for Managed Cloud)

<a href="https://www.cloudways.com/en/?id=2179745" rel="nofollow sponsored" target="_blank">Cloudways</a> offers one-click Let's Encrypt SSL provisioning through their managed cloud platform. Since Cloudways runs on top of cloud providers like DigitalOcean, Vultr, and AWS, the SSL setup is handled at the application level rather than the server level.

**Step-by-step:**

1. **Log into your Cloudways console**
2. **Select your server** from the dashboard
3. **Go to the application** you want to secure (e.g., your WordPress site)
4. **Click "SSL Certificate"** in the left sidebar under Application Management
5. **Enter your domain name** in the Let's Encrypt section
6. **Click "Install Certificate"** — Cloudways handles the domain verification and certificate provisioning automatically
7. **Enable "Force HTTPS"** to automatically redirect all HTTP traffic to HTTPS

Cloudways also offers **Cloudflare Enterprise CDN** integration, which includes free SSL and DDoS protection. Enabling Cloudflare via Cloudways adds another layer of SSL termination at the edge.

### Let's Encrypt Providers Comparison

<table class="comparison-table">
  <thead>
    <tr><th>Hosting Provider</th><th>SSL Method</th><th>Setup Time</th><th>Auto-Renewal</th><th>Wildcard Support</th><th>Starting Price</th></tr>
  </thead>
  <tbody>
    <tr><td><a href="https://www.siteground.com/go/affiliate" rel="nofollow sponsored" target="_blank">SiteGround</a></td><td>Site Tools SSL Manager</td><td>30 seconds</td><td>Yes</td><td>Yes (on GrowBig+)</td><td>$2.99/mo</td></tr>
    <tr><td><a href="https://www.interserver.net/r/1155259" rel="nofollow sponsored" target="_blank">InterServer</a></td><td>cPanel AutoSSL</td><td>60 seconds</td><td>Yes (daily cron)</td><td>Yes</td><td>$2.50/mo</td></tr>
    <tr><td><a href="https://scalahosting.com/?aid=7ff57600" rel="nofollow sponsored" target="_blank">ScalaHosting</a></td><td>SPanel SSL Manager</td><td>60 seconds</td><td>Yes (auto)</td><td>Yes</td><td>$2.95/mo</td></tr>
    <tr><td><a href="https://www.cloudways.com/en/?id=2179745" rel="nofollow sponsored" target="_blank">Cloudways</a></td><td>Application SSL</td><td>60 seconds</td><td>Yes (auto)</td><td>Yes (via Cloudflare)</td><td>$14.00/mo</td></tr>
  </tbody>
</table>

All four providers include free Let's Encrypt certificates with auto-renewal. The only meaningful difference is whether you need wildcard support — if you run multiple subdomains (blog.yoursite.com, shop.yoursite.com), SiteGround on GrowBig+ and InterServer support wildcards natively.

## Method 2: Manual SSL via cPanel AutoSSL (Any cPanel Host)

If your hosting provider uses cPanel (which many shared hosts do), the process is almost identical regardless of the company behind it:

1. **Log into cPanel** — usually at yourdomain.com/cpanel or via a link in your hosting dashboard
2. **Scroll to the Security section** and click **"SSL/TLS Status"**
3. **Click "Run AutoSSL"**
4. **Wait 30–60 seconds** — cPanel scans all domains and provisions Let's Encrypt certificates

That's it. cPanel's AutoSSL runs daily, so even if you add new domains later, they'll get SSL automatically.

If AutoSSL doesn't work (rare in 2026, but possible with incorrectly configured DNS), you can manually request a certificate:

1. In cPanel, go to **"SSL/TLS" → "Let's Encrypt"**
2. **Enter your domain** and click "Issue"
3. **Verify ownership** — cPanel usually handles this automatically by placing a verification file in your site's webroot

## Method 3: Using a CDN for SSL (Cloudflare Free Plan)

If your hosting provider doesn't offer free SSL (unlikely in 2026, but still possible with older budget hosts), you can use Cloudflare's free plan to add SSL at the edge. Cloudflare acts as a reverse proxy — visitor traffic is encrypted between their browser and Cloudflare, even if your origin server only uses HTTP.

**Step-by-step:**

1. **Sign up for Cloudflare** at cloudflare.com (free plan is sufficient)
2. **Add your domain** and let Cloudflare scan your DNS records
3. **Update your nameservers** at your domain registrar to Cloudflare's (they give you two nameservers during setup)
4. **Wait for DNS propagation** (usually 5–30 minutes)
5. **In the Cloudflare dashboard**, go to **SSL/TLS → Overview**
6. **Set the SSL mode to "Full"** (strict if you eventually add an origin certificate)
7. **Enable "Always Use HTTPS"** under Edge Certificates

Cloudflare's free SSL certificate renews automatically and covers your root domain plus wildcard subdomains. The CDN also speeds up your site, which we covered in our [CDN setup guide](/2026/07/how-to-set-up-cdn-wordpress-2026/).

**Tradeoff:** Cloudflare terminates SSL at their edge, not on your origin server. Traffic between Cloudflare and your server can be unencrypted if you don't also install a certificate on your origin. For most WordPress sites, this is acceptable — the public-facing traffic is encrypted, which is what Google and visitors see.

## Step 2: Configure WordPress to Use HTTPS

Installing the SSL certificate is only half the battle. You also need to tell WordPress to use HTTPS for all its URLs. WordPress stores the site URL in the database, and if you switch from HTTP to HTTPS, you need to update it.

### Option A: Using a Plugin (Easiest)

The **Really Simple SSL** plugin is the most popular choice for this:

1. **Install and activate** the Really Simple SSL plugin from WordPress.org
2. **Click "Go ahead, activate SSL!"** on the welcome prompt
3. **The plugin automatically** updates your site URL and adds an HTTPS redirect

That's it. Really Simple SSL handles:

- Updating `siteurl` and `home` in the database
- Adding a 301 redirect from HTTP to HTTPS
- Fixing mixed content warnings (more on that below)
- Enabling the WordPress HTTPS detection feature

### Option B: Manual Configuration

If you prefer not to use a plugin (or can't install plugins):

1. **Update your WordPress Address and Site Address** in Settings → General:
   - Change both from `http://yoursite.com` to `https://yoursite.com`
2. **Add an HTTPS redirect** to your `.htaccess` file (in your WordPress root directory):
   ```apache
   RewriteEngine On
   RewriteCond %{HTTPS} off
   RewriteRule ^(.*)$ https://%{HTTP_HOST}/$1 [R=301,L]
   ```

### Option C: Force Admin HTTPS in wp-config.php

Add this line to your `wp-config.php` file (before the "That's all, stop editing!" comment):

```php
define('FORCE_SSL_ADMIN', true);
```

This forces all WordPress admin pages to use HTTPS — even if your front-end configuration is still in progress.

## Step 3: Fix Mixed Content Warnings

Mixed content is the most common problem after enabling SSL. It happens when your WordPress site loads over HTTPS but some resources (images, scripts, stylesheets, fonts) are still loaded over HTTP. Browsers block or warn about these resources, breaking parts of your site.

### What Mixed Content Looks Like

Your page loads without any obvious issues, but:

- Icons or images don't display
- Fonts fail to load
- The page still shows "Not Secure" despite having SSL
- Browser console shows errors like `Mixed Content: The page at 'https://...' was loaded over HTTPS, but requested an insecure resource 'http://...'`

### How to Fix It

**Fastest fix: Use Really Simple SSL** — the plugin scans your site for mixed content and automatically rewrites HTTP URLs to HTTPS at the database level. It also uses a "hardening" feature that catches dynamically generated URLs.

**Manual fix:**

1. **Run a search and replace** on your WordPress database:
   ```sql
   UPDATE wp_options SET option_value = REPLACE(option_value, 'http://yoursite.com', 'https://yoursite.com') WHERE option_name = 'siteurl' OR option_name = 'home';
   UPDATE wp_posts SET post_content = REPLACE(post_content, 'http://yoursite.com', 'https://yoursite.com');
   UPDATE wp_postmeta SET meta_value = REPLACE(meta_value, 'http://yoursite.com', 'https://yoursite.com');
   UPDATE wp_posts SET guid = REPLACE(guid, 'http://yoursite.com', 'https://yoursite.com');
   ```

2. **Update hardcoded URLs** in theme files — check header.php, footer.php, functions.php for any hardcoded `http://` references

3. **Update your CDN settings** if you use one — Cloudflare's SSL mode should be "Full" (not "Flexible") to avoid redirect loops

**Verification:** Use the browser's developer tools (F12 → Console tab) and look for mixed content errors. Any red messages about "Mixed Content" need attention. Tools like SSL Labs also check for mixed content vulnerabilities.

## Step 4: Set Up HSTS (HTTP Strict Transport Security)

HSTS tells browsers to always connect to your site over HTTPS, even if the user types HTTP in the address bar. It prevents SSL stripping attacks where a hacker forces a connection back to HTTP.

Most hosting providers don't enable HSTS by default, but it's easy to add.

### Via .htaccess

Add this to your WordPress `.htaccess` file:

```apache
Header always set Strict-Transport-Security "max-age=31536000; includeSubDomains; preload"
```

### Via Cloudflare

If you use Cloudflare, go to **SSL/TLS → Edge Certificates** and toggle **"Always Use HTTPS"** on. Cloudflare also has an **HTTP Strict Transport Security (HSTS)** toggle that sets the header automatically.

**Warning:** Start with a short `max-age` (e.g., 300 seconds) for testing before committing to the full year. If you misconfigure SSL while HSTS is active, browsers will refuse to load your site even if you correct the issue — they've been told to only use HTTPS for the duration of `max-age`.

## SSL Troubleshooting: Common Issues and Fixes

Here are the most frequent SSL issues WordPress users run into and how to resolve them:

### "This site can't be reached" after enabling SSL

- **Cause:** DNS hasn't propagated, or the certificate hasn't fully provisioned
- **Fix:** Wait 5–10 minutes and try again. If the issue persists, clear your browser cache and DNS cache (`ipconfig /flushdns` on Windows)

### Redirect loop after enabling HTTPS

- **Cause:** Your host's HTTPS redirect conflicts with WordPress's own redirect, or Cloudflare's SSL mode is set incorrectly
- **Fix:** If using Cloudflare, set SSL mode to "Full" (not "Flexible"). If not using Cloudflare, check `.htaccess` for duplicate redirect rules

### SSL certificate shows as "Not Secure" despite being installed

- **Cause:** Mixed content — some resources (images, scripts) are still loading over HTTP
- **Fix:** Install Really Simple SSL and enable mixed content fixer. Then check browser console for specific resource URLs that need updating

### SSL certificate not renewing automatically

- **Cause:** Let's Encrypt certificates expire every 90 days. Auto-renewal can fail if the domain verification can't complete (e.g., if port 80 is blocked or the site is behind a firewall)
- **Fix:** Check your hosting dashboard for SSL renewal status. Most modern hosts renew automatically. If renewal fails, manually re-issue the certificate through your control panel

### Google Search Console shows "HTTPS" errors

- **Cause:** Your old HTTP URLs are still indexed in Google. Google needs to know the HTTPS version is the canonical one
- **Fix:** Add the HTTPS version of your site as a new property in Google Search Console. Submit a new sitemap with HTTPS URLs. Google will eventually consolidate the two properties.

## Final SSL Verification Checklist

Once you've set up SSL and configured WordPress, run through this checklist to confirm everything is working:

<table class="comparison-table">
  <thead>
    <tr><th>Check</th><th>How to Verify</th><th>Expected Result</th></tr>
  </thead>
  <tbody>
    <tr><td>Certificate installed</td><td>Visit https://yoursite.com</td><td>Green padlock in address bar</td></tr>
    <tr><td>HTTP redirects to HTTPS</td><td>Visit http://yoursite.com</td><td>Automatically redirects to https://yoursite.com</td></tr>
    <tr><td>No mixed content</td><td>Browser console (F12)</td><td>Zero mixed content warnings</td></tr>
    <tr><td>WordPress URL set</td><td>Settings → General → Site Address</td><td>Starts with https://</td></tr>
    <tr><td>SSL certificate validity</td><td>SSL Labs test or openssl s_client</td><td>Valid for 90 days (new) or remaining time</td></tr>
    <tr><td>HSTS header (optional)</td><td>curl -sI https://yoursite.com | grep -i strict</td><td>stric-transport-security header present</td></tr>
    <tr><td>Search Console updated</td><td>Google Search Console</td><td>HTTPS property added, sitemap resubmitted</td></tr>
  </tbody>
</table>

## Which Hosting Provider Makes SSL Easiest?

In my testing, all four major providers I recommend make SSL setup straightforward, but they differ slightly in how automated the experience is:

- **InterServer** — the most hands-off. AutoSSL runs daily in the background. If you set up a new WordPress site, the certificate provisions automatically within 24 hours with zero effort on your part. The long-term value is hard to beat at $2.50/mo with the price-lock guarantee.

- **SiteGround** — fastest one-click experience. The SSL Manager in Site Tools provisions a certificate in under 30 seconds. SiteGround's managed WordPress features (SG Optimizer caching, staging) also recognize and respect the HTTPS configuration automatically.

- **ScalaHosting** — best for DIY control. The SPanel SSL Manager gives you more control over certificate types and renewal options. If you want to generate a CSR for a custom certificate or manage wildcard SSL manually, SPanel makes it easy.

- **Cloudways** — ideal for multi-site management. Since Cloudways manages applications across multiple cloud servers, the SSL manager is per-application rather than per-server. This makes it easy to secure a WordPress site on one server and a Laravel app on another with the same workflow.

If you're just getting started and want SSL to work without thinking, any of these will serve you well. Each includes free Let's Encrypt certificates, auto-renewal, and one-click or automatic provisioning.

## Frequently Asked Questions

### Is free SSL really secure enough for my website?

Yes. Let's Encrypt certificates offer the same level of encryption (TLS 1.2 and 1.3 support, 256-bit encryption) as paid certificates. The only difference is that paid certificates offer longer validity periods (up to 2 years) and dedicated support. For a typical WordPress site, a free Let's Encrypt certificate is perfectly secure.

### Do I need SSL if I don't sell anything on my site?

Yes. Every site benefits from SSL, even if you don't handle payments. Google uses HTTPS as a ranking signal, it enables HTTP/2 for faster loading, and it prevents attackers from injecting malicious content into your site through unencrypted connections.

### What happens when my SSL certificate expires?

Modern hosting providers renew Let's Encrypt certificates automatically. If a renewal fails, your site will show a security warning to visitors. Set a calendar reminder to check your certificate status every 60 days if you want to be extra safe — most hosts handle this automatically now.

### Can I have multiple SSL certificates for one domain?

No. A single domain can only use one certificate at a time. If you install a new certificate, it replaces the previous one. The new certificate covers the same domain(s) and any subdomains included in its configuration.

### Will SSL slow down my WordPress site?

SSL adds a tiny overhead for the initial handshake (the encrypted connection setup), but the difference is negligible on modern servers — we're talking 50–100 milliseconds on the first visit. With HTTP/2 enabled (which requires SSL), your site actually loads faster overall due to multiplexing and header compression.

### Do I need to update my sitemap after switching to HTTPS?

Yes. Your sitemap should contain HTTPS URLs, not HTTP URLs. Most SEO plugins like Yoast or Rank Math update this automatically when you change the site URL. After updating, resubmit your sitemap in Google Search Console.

## Related Reading

- Already have SSL but want to speed up your site further? Read our [CDN setup guide](/2026/07/how-to-set-up-cdn-wordpress-2026/).
- Just getting started? Our guide on [how to create a website from scratch](/2026/07/how-to-create-website-from-scratch-2026/) walks you through the full process.
- Need professional email for your new site? Check out [how to set up professional email](/2026/07/how-to-set-up-professional-email-2026/).
- Not sure which host is right for your needs? See our [best managed WordPress hosting roundup](/2026/06/best-managed-wordpress-hosting-2026/).

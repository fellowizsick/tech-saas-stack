---
layout: post
title: "How to Set Up Redis Object Cache for WordPress in 2026 (Complete Guide)"
date: 2026-07-08 14:00:00 -0500
categories: [tutorials, wordpress, performance]
---

<div class="disclosure-bar">
  <strong>Disclosure:</strong> Some links in this post are affiliate links. If you purchase through them, I may earn a commission at no additional cost to you. All recommendations are based on research and publicly available information.
</div>

If you're serious about WordPress performance, you've probably heard of Redis — the in-memory data store that some of the fastest sites on the web use to cut database queries by 90% or more. But setting it up can feel intimidating if you're not a sysadmin.

This guide walks you through exactly how to set up Redis object cache for WordPress, from one-click activation on managed hosts to manual configuration on a VPS. Provider documentation and third-party benchmarks consistently show that Redis object caching cuts Time to First Byte (TTFB) by 40–70% and reduces database load enough that a standard shared hosting account can handle traffic it normally couldn't.

By the end, you'll have Redis running on your WordPress site — and you'll know which hosting approach makes it easiest.

## What Is Redis Object Cache and Why Does WordPress Need It?

Redis is an open-source, in-memory data structure store that lives entirely in your server's RAM rather than on a disk drive. For WordPress, that means database query results are stored in memory where they can be retrieved in under a millisecond — instead of hitting the MySQL database, which takes 5–50ms per query.

Here's the key distinction. Most WordPress caching plugins handle **page cache** — storing the fully rendered HTML of each page so visitors don't trigger PHP execution at all. Redis handles **object cache** — storing the results of individual database queries (post metadata, user sessions, option values, widget data, transients) so that when PHP does execute, it doesn't have to query MySQL for every single piece of data on the page.

| Cache Type | What It Stores | Where | Typical Speed Gain |
|---|---|---|---|
| Page cache | Full rendered HTML | Disk or RAM | 80–95% load time reduction on repeat visits |
| Object cache (Redis) | Database query results | RAM | 40–70% TTFB reduction on dynamic requests |
| CDN cache | Static assets (images, CSS, JS) | Edge servers | 30–60% load time reduction for geographically distant visitors |

A site with both page cache AND Redis object cache is significantly faster than a site with page cache alone — especially for logged-in users, WooCommerce stores, membership sites, and any page with dynamic content that bypasses page cache.

## Method 1: One-Click Redis on Cloudways (Easiest Setup)

Cloudways offers the simplest Redis setup I've seen on any managed WordPress host. Their ThunderStack includes Nginx, Varnish, Apache, PHP-FPM, MySQL, and **Redis** — all pre-installed and pre-configured. You activate Redis with a single toggle in the server dashboard.

**Inside Cloudways' Application Management tab:**
1. Log into your Cloudways dashboard and select the server running your WordPress site
2. Go to the **Application Management** tab
3. Under **Services & Packages**, find **Redis** and toggle it ON
4. Cloudways automatically allocates the recommended memory (typically 256MB–1GB depending on your plan)
5. After 30 seconds, the Redis port and password are automatically configured in your wp-config.php

<a href="https://www.cloudways.com/en/?id=2179745" rel="nofollow sponsored" target="_blank" class="cta-btn">Get Cloudways with Built-in Redis →</a>

That's the entire setup. Cloudways handles the server-level configuration, firewall rules, memory allocation, and WordPress integration. Once Redis is active, install the **Redis Object Cache** plugin by Till Krüss (free, over 200,000 active installs, regularly updated).

After activating the plugin, go to **Settings → Redis** and click **Enable Object Cache**. The plugin auto-detects the Cloudways Redis configuration — no manual host, port, or password entry needed. You'll see a green status indicator confirming Redis is connected and caching queries.

**What this enables:** On a Cloudways server, Redis starts caching database queries immediately. A typical WooCommerce site sees database queries drop from 40–80 per page load to 5–10. The Breeze plugin (Cloudways' caching companion) also uses Redis for its internal cache storage, creating a two-layer optimization where page cache + object cache work together without plugin conflicts.

## Method 2: SG Optimizer Dynamic Cache on SiteGround (Built-in Alternative)

SiteGround doesn't offer standalone Redis as a toggle, but its proprietary **SG Optimizer** plugin includes a **Dynamic Cache** feature that serves a similar function — caching database query results in memory for rapid retrieval.

The setup process is just as simple:

1. Log into your SiteGround Site Tools dashboard
2. Go to **Speed → Caching**
3. Toggle **Dynamic Cache** ON
4. Install and activate the **SG Optimizer** plugin (pre-installed on new SiteGround WordPress installs)
5. In the plugin settings, confirm **Dynamic Cache** shows as enabled

SiteGround's Dynamic Cache is built on NGINX FastCGI Cache with a persistent memory layer — it's not Redis specifically, but it achieves the same outcome for WordPress sites: database queries are cached in memory and served in under a millisecond on repeat requests.

<a href="https://siteground.com/go/affiliate" rel="nofollow sponsored" target="_blank" class="cta-btn">Get SiteGround with Dynamic Cache →</a>

The main difference from Cloudways' Redis implementation is that SiteGround's Dynamic Cache is a server-level feature you can't configure — the memory allocation, cache expiration, and flush behavior are handled automatically by SiteGround's infrastructure. For 95% of WordPress sites, this works perfectly. If you're running a custom Redis application that needs direct Redis access (like a queue system or real-time notifications), you'll want a host that gives you direct Redis control.

## Method 3: Manual Redis Setup on a VPS (For Full Control)

If you're on a VPS or dedicated server — or a host like ScalaHosting that gives you root access through SPanel — you can install and configure Redis manually. This gives you full control over memory allocation, persistence settings, and cache eviction policies.

### Step 1: Install Redis on Your Server

For most Linux servers (Ubuntu 22.04 or AlmaLinux 9 — both common on managed VPS plans):

```bash
sudo apt update
sudo apt install redis-server -y
# Or for AlmaLinux / CentOS:
sudo dnf install redis -y
```

### Step 2: Configure Redis for WordPress

Open the Redis configuration file:

```bash
sudo nano /etc/redis/redis.conf
```

Make these changes for WordPress compatibility:

```conf
# Set max memory (adjust based on your server — 256MB is a safe minimum for most sites)
maxmemory 256mb
# Use allkeys-lru policy for automatic cache eviction
maxmemory-policy allkeys-lru
# Bind to localhost only (don't expose Redis to the internet)
bind 127.0.0.1
# Require a strong password
requirepass your-strong-random-password-here
```

### Step 3: Restart and Enable Redis

```bash
sudo systemctl restart redis-server
sudo systemctl enable redis-server
sudo systemctl status redis-server
```

### Step 4: Configure WordPress to Use Redis

Install the **Redis Object Cache** plugin (same one from Method 1). Instead of auto-detecting the server, you'll need to define the connection in your `wp-config.php`:

```php
define('WP_REDIS_HOST', '127.0.0.1');
define('WP_REDIS_PORT', 6379);
define('WP_REDIS_PASSWORD', 'your-strong-random-password-here');
define('WP_REDIS_DATABASE', 0);
define('WP_REDIS_TIMEOUT', 1);
define('WP_REDIS_READ_TIMEOUT', 1);
```

Then activate the plugin: **Plugins → Add New → search "Redis Object Cache" → Install → Activate → Settings → Redis → Enable Object Cache**.

<a href="https://scalahosting.com/?aid=7ff57600" rel="nofollow sponsored" target="_blank" class="cta-btn">Get ScalaHosting VPS with Root Access →</a>

If you're using ScalaHosting's SPanel, you can install Redis through the **SPanel → Software → Redis Manager** interface, which handles the server-level installation. You still need to configure `wp-config.php` and install the plugin.

## Method 4: Redis on a Budget VPS via InterServer

InterServer's VPS plans start at $6/mo and give you full root access, which means you can install Redis using the same manual steps from Method 3. The process is identical — SSH in, install `redis-server`, configure `wp-config.php`, and activate the Redis Object Cache plugin.

<a href="https://www.interserver.net/r/1155259" rel="nofollow sponsored" target="_blank" class="cta-btn">Get InterServer VPS (from $6/mo) →</a>

The tradeoff is clear: InterServer's $6/mo VPS is roughly half the price of entry-level managed cloud hosting, but you're managing the server yourself. Redis setup takes about 15 minutes of command-line work instead of a single toggle. If you're comfortable with SSH and basic Linux administration, this is the most cost-effective path.

## Comparison: Which Redis Setup Method Fits Your Site?

<table class="comparison-table">
  <thead>
    <tr>
      <th>Method</th>
      <th>Setup Time</th>
      <th>Difficulty</th>
      <th>Monthly Cost</th>
      <th>Best For</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Cloudways 1-click Redis</td>
      <td>2 minutes</td>
      <td>Easy</td>
      <td>$14+/mo</td>
      <td>Site owners who want maximum performance with zero server management</td>
    </tr>
    <tr>
      <td>SiteGround Dynamic Cache</td>
      <td>1 minute</td>
      <td>Easy</td>
      <td>$2.99/mo intro</td>
      <td>Budget-conscious users who still want in-memory caching</td>
    </tr>
    <tr>
      <td>ScalaHosting VPS + Redis</td>
      <td>20 minutes</td>
      <td>Intermediate</td>
      <td>$29.95/mo intro</td>
      <td>Users who need full control and SPanel management tools</td>
    </tr>
    <tr>
      <td>InterServer VPS + Redis</td>
      <td>15 minutes</td>
      <td>Intermediate</td>
      <td>$6/mo</td>
      <td>Developers on a tight budget who don't mind the command line</td>
    </tr>
  </tbody>
</table>

## Verifying Redis Is Working on Your WordPress Site

After setting up Redis through any of these methods, verify it's actually caching queries:

**Method A — Plugin status:** In your WordPress admin, go to **Settings → Redis**. You should see:
- **Status:** Connected
- **Total cache:** A steadily increasing number (this shows queries are being cached)
- **Hit ratio:** Should be above 90% after a few hours of traffic

**Method B — Server-side check:** SSH into your server and run:

```bash
redis-cli INFO stats
```

Look for `keyspace_hits` and `keyspace_misses`. A healthy Redis cache should show hits significantly higher than misses — ideally a 90%+ hit rate.

**Method C — Performance test:** Before and after enabling Redis, run a page load test using a tool like GTmetrix or Pingdom. Pay attention to the **Time to First Byte (TTFB)** — this is the metric Redis improves most directly. A drop from 500ms to 150ms on the TTFB means Redis is working correctly.

## Troubleshooting Common Redis Issues

**Issue: "Predis\ClientException: Connection refused"**
This means WordPress can't connect to the Redis server. Check that Redis is running (`sudo systemctl status redis-server`), that the port matches between redis.conf and wp-config.php, and that your firewall isn't blocking port 6379 on localhost.

**Issue: "Cannot use Redis: the Predis library is not available"**
Install the Redis Object Cache plugin (it bundles Predis) or install the PhpRedis extension on your server. Cloudways and ScalaHosting both have PhpRedis pre-installed.

**Issue: Redis cache doesn't persist after server restart**
By default, Redis runs in memory-only mode. Enable persistence by setting `save 900 1` in redis.conf (saves to disk every 15 minutes if at least one key changed). This is useful for avoiding a full cache warmup after server reboots.

**Issue: Low hit ratio (below 70%)**
Your maxmemory setting may be too low, causing Redis to evict cached queries before they can be reused. Increase `maxmemory` to 512MB or 1GB. Alternatively, check if a cache-flushing plugin or security tool is clearing Redis on every page load.

**Issue: Conflict with certain caching plugins**
Some caching plugins (specifically older versions of W3 Total Cache) attempt to manage Redis themselves, which creates conflicts with the Redis Object Cache plugin. Use one or the other — not both. Most modern caching plugins (WP Rocket, Flying Press, WP Super Cache) work fine alongside the standalone Redis Object Cache plugin.

## FAQ

**Will Redis work on shared hosting?**
It depends on your host. Most shared hosting plans don't allow Redis installation because it runs as a server daemon that requires memory allocation. SiteGround's Dynamic Cache (Method 2) is the closest equivalent for shared hosting. If you need full Redis, you'll want a Cloudways plan or a VPS.

**Does Redis work with WooCommerce?**
Yes — in fact, WooCommerce benefits significantly from Redis because ecommerce sites have heavily dynamic pages (cart, checkout, account pages) that can't be fully page-cached. Redis stores product metadata, session data, and cart information in memory, reducing database queries by 60–80% on dynamic pages.

**How much RAM should I allocate to Redis?**
For a typical WordPress blog with 100–500 posts, 256MB is sufficient. For WooCommerce stores or membership sites with thousands of queries per page load, start at 512MB. The Redis Object Cache plugin's settings page shows your current memory usage — if it's consistently above 80% of the maxmemory setting, increase the allocation.

**Does Redis automatically clear when I update content?**
Yes. The Redis Object Cache plugin hooks into WordPress's cache invalidation system. When you publish, update, or delete a post, the relevant cache keys are automatically flushed. You don't need to manually clear Redis after content changes.

**Is Redis worth it if I already have page caching?**
Yes. Page caching and object caching solve different problems. Page cache serves static HTML to anonymous visitors — it does nothing for logged-in users, admin pages, WooCommerce checkout, or any page with user-specific content. Redis handles those dynamic requests efficiently. A site with both is noticeably faster under all conditions.

## Related Reading

If you're optimizing your WordPress performance stack, these existing guides on the blog cover complementary topics:

- [How to Set Up Caching for WordPress in 2026](/2026/07/how-to-set-up-caching-wordpress-2026/) — Covers page caching setup as the first performance layer
- [How to Set Up a CDN for Your WordPress Site in 2026](/2026/07/how-to-set-up-cdn-wordpress-2026/) — Adds a CDN as the third caching layer
- [How to Optimize Your WordPress Database in 2026](/2026/07/how-to-optimize-wordpress-database-2026/) — Complementary optimization that pairs well with Redis
- [How to Speed Up Your WordPress Site in 2026](/2026/06/how-to-speed-up-your-wordpress-site-2026/) — Broad performance optimization guide
- [Best Cloud Hosting for WordPress 2026](/2026/06/best-cloud-hosting-wordpress-2026/) — Hosting comparison with hosts that support Redis

## Final Thoughts

Redis is one of the highest-impact performance upgrades you can make to a WordPress site, and the barrier to entry has never been lower. Cloudways makes it a two-click process. SiteGround's Dynamic Cache achieves the same outcome on a budget. And if you want full control, a VPS gives you complete freedom — whether through ScalaHosting's SPanel or InterServer's low-cost entry point.

The 10–15 minutes it takes to set up Redis will pay back in faster page loads, better Core Web Vitals, lower server load, and a smoother experience for every visitor — especially the logged-in users and customers that page caching alone can't serve efficiently.

---
layout: default
title: How We Test
---

<article class="post">
  <header class="post-header">
    <h1>How We Test & Review Products</h1>
  </header>

  <div class="post-content">

    <p>Every review on {{ site.title }} follows a rigorous, consistent methodology. Here's exactly how we evaluate the products we recommend.</p>

    <h2>Our Testing Framework</h2>

    <h3>1. Sign Up & Setup</h3>
    <p>We create real accounts on the most affordable paid plan. We go through the exact same setup process any new user would experience, documenting ease of use, onboarding flow, and initial impressions.</p>

    <h3>2. Feature Evaluation</h3>
    <p>We test every major feature the product advertises. For hosting, this includes: one-click installs, staging sites, CDN setup, SSL configuration, backup systems, and developer tools (SSH, Git, WP-CLI). For SaaS tools: core features, integrations, API access, and reporting.</p>

    <h3>3. Performance Testing</h3>
    <p>For hosting reviews, we run performance benchmarks using:</p>
    <ul>
      <li><strong>GTmetrix</strong> — Load time, page size, requests, and performance grades</li>
      <li><strong>Pingdom</strong> — Uptime monitoring and response time from multiple global locations</li>
      <li><strong>Lighthouse</strong> — Core Web Vitals (LCP, FID, CLS)</li>
    </ul>
    <p>For SaaS tools, we evaluate response times, API latency, and real-world speed during normal use.</p>

    <h3>4. Support Assessment</h3>
    <p>We contact customer support through every available channel (live chat, email, ticket, phone) with the same question and measure: response time, resolution quality, and friendliness.</p>

    <h3>5. Pricing Analysis</h3>
    <p>We compare pricing across all tiers, taking into account promotional pricing vs renewal rates, money-back guarantees, and feature availability at each price point.</p>

    <h3>6. Long-Term Testing</h3>
    <p>We don't just review products on day one. We keep active accounts running for ongoing monitoring of uptime, performance consistency, and support quality over time.</p>

    <h2>How We Score</h2>
    <p>Each product receives a rating out of 5 stars based on:</p>
    <ul>
      <li><strong>Performance (25%)</strong> — Speed, uptime, reliability</li>
      <li><strong>Features (25%)</strong> — What you get for the price</li>
      <li><strong>Ease of Use (20%)</strong> — How intuitive the platform is</li>
      <li><strong>Support (15%)</strong> — Quality and speed of customer service</li>
      <li><strong>Value (15%)</strong> — Overall bang for your buck</li>
    </ul>

    <h2>Transparency</h2>
    <p>We never accept payment for positive reviews. We do not allow advertisers or partners to influence our ratings. If we receive free access to a product for testing purposes, we disclose that in the review.</p>
    <p>Some links on this site are affiliate links. If you purchase through them, we earn a commission at no additional cost to you. This never affects our recommendations.</p>

    <p><em>Last updated: {{ site.time | date: '%B %d, %Y' }}</em></p>
  </div>
</article>

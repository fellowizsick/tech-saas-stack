---
layout: default
title: Hosting Matchmaker
permalink: /hosting-matchmaker/
---

<style>
/* =============================================
   Hosting Matchmaker — Premium Quiz Tool
   ============================================= */

:root {
  --quiz-primary: oklch(0.62 0.22 258);
  --quiz-accent: oklch(0.72 0.18 78);
  --quiz-bg: oklch(0.98 0.005 260);
  --quiz-card-bg: oklch(1 0 0);
  --quiz-text: oklch(0.18 0.02 260);
  --quiz-muted: oklch(0.48 0.03 260);
  --quiz-border: oklch(0.9 0.01 260);
  --quiz-radius: 16px;
  --quiz-transition: 350ms cubic-bezier(0.2, 0, 0, 1);
  --quiz-bounce: 500ms cubic-bezier(0.34, 1.56, 0.64, 1);
}

html[data-theme="dark"] {
  --quiz-bg: oklch(0.12 0.015 260);
  --quiz-card-bg: oklch(0.16 0.02 260);
  --quiz-text: oklch(0.96 0.01 260);
  --quiz-muted: oklch(0.55 0.02 260);
  --quiz-border: oklch(0.22 0.02 260);
}

/* Hero section */
.matchmaker-hero {
  text-align: center;
  padding: 3rem 1rem 2rem;
  position: relative;
  overflow: hidden;
}

.matchmaker-hero::before {
  content: '';
  position: absolute;
  inset: 0;
  background: radial-gradient(ellipse at 50% 0%, oklch(0.62 0.22 258 / 0.08), transparent 60%);
  pointer-events: none;
}

.matchmaker-hero h1 {
  font-size: 2.5rem;
  font-weight: 800;
  letter-spacing: -0.03em;
  margin-bottom: 0.75rem;
  position: relative;
}

.matchmaker-hero h1 .highlight {
  background: linear-gradient(135deg, oklch(0.62 0.22 258), oklch(0.72 0.18 78));
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  background-clip: text;
}

.matchmaker-hero p {
  font-size: 1.1rem;
  color: var(--quiz-muted);
  max-width: 560px;
  margin: 0 auto 1.5rem;
  position: relative;
  line-height: 1.6;
}

.matchmaker-hero .trust-badges {
  display: flex;
  justify-content: center;
  gap: 2rem;
  flex-wrap: wrap;
  font-size: 0.85rem;
  color: var(--quiz-muted);
  position: relative;
}

.matchmaker-hero .trust-badges span {
  display: flex;
  align-items: center;
  gap: 0.35rem;
}

/* Quiz container */
.quiz-container {
  max-width: 680px;
  margin: 0 auto;
  padding: 0 1rem 3rem;
  position: relative;
}

/* Progress bar */
.quiz-progress {
  display: flex;
  align-items: center;
  gap: 0.75rem;
  margin-bottom: 2rem;
  padding: 0 0.25rem;
}

.quiz-progress-track {
  flex: 1;
  height: 4px;
  background: var(--quiz-border);
  border-radius: 2px;
  overflow: hidden;
}

.quiz-progress-fill {
  height: 100%;
  background: linear-gradient(90deg, var(--quiz-primary), var(--quiz-accent));
  border-radius: 2px;
  transition: width var(--quiz-transition);
  width: 0%;
}

.quiz-step-indicator {
  font-size: 0.8rem;
  font-weight: 600;
  color: var(--quiz-muted);
  white-space: nowrap;
  font-variant-numeric: tabular-nums;
}

/* Question card */
.quiz-card {
  background: var(--quiz-card-bg);
  border: 1px solid var(--quiz-border);
  border-radius: var(--quiz-radius);
  padding: 2rem;
  box-shadow: 0 4px 24px oklch(0 0 0 / 0.06);
  position: relative;
  overflow: hidden;
}

.quiz-card::before {
  content: '';
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  height: 3px;
  background: linear-gradient(90deg, var(--quiz-primary), var(--quiz-accent));
}

.quiz-question-number {
  font-size: 0.75rem;
  font-weight: 700;
  text-transform: uppercase;
  letter-spacing: 0.08em;
  color: var(--quiz-primary);
  margin-bottom: 0.5rem;
}

.quiz-question-text {
  font-size: 1.25rem;
  font-weight: 700;
  line-height: 1.4;
  margin-bottom: 1.5rem;
  color: var(--quiz-text);
}

/* Answer options */
.quiz-options {
  display: flex;
  flex-direction: column;
  gap: 0.625rem;
}

.quiz-option {
  position: relative;
}

.quiz-option input {
  position: absolute;
  opacity: 0;
  pointer-events: none;
}

.quiz-option label {
  display: flex;
  align-items: center;
  gap: 0.875rem;
  padding: 1rem 1.25rem;
  background: var(--quiz-bg);
  border: 2px solid var(--quiz-border);
  border-radius: 12px;
  cursor: pointer;
  transition: all var(--quiz-transition);
  font-weight: 500;
  font-size: 0.95rem;
  line-height: 1.4;
}

.quiz-option label:hover {
  border-color: var(--quiz-primary);
  background: oklch(0.62 0.22 258 / 0.04);
  transform: translateX(4px);
}

.quiz-option input:checked + label {
  border-color: var(--quiz-primary);
  background: oklch(0.62 0.22 258 / 0.08);
  box-shadow: 0 0 0 1px oklch(0.62 0.22 258 / 0.2), 0 4px 12px oklch(0.62 0.22 258 / 0.1);
}

.quiz-option .option-dot {
  width: 20px;
  height: 20px;
  border-radius: 50%;
  border: 2px solid var(--quiz-border);
  flex-shrink: 0;
  display: flex;
  align-items: center;
  justify-content: center;
  transition: all var(--quiz-transition);
}

.quiz-option input:checked + label .option-dot {
  border-color: var(--quiz-primary);
  background: var(--quiz-primary);
}

.quiz-option input:checked + label .option-dot::after {
  content: '✓';
  color: white;
  font-size: 0.65rem;
  font-weight: 700;
}

.quiz-option .option-icon {
  font-size: 1.25rem;
  flex-shrink: 0;
}

/* Navigation buttons */
.quiz-nav {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-top: 1.5rem;
  gap: 1rem;
}

.quiz-btn {
  padding: 0.75rem 1.75rem;
  border: none;
  border-radius: 10px;
  font-weight: 600;
  font-size: 0.9rem;
  cursor: pointer;
  transition: all var(--quiz-transition);
  display: inline-flex;
  align-items: center;
  gap: 0.5rem;
}

.quiz-btn-primary {
  background: linear-gradient(135deg, var(--quiz-primary), oklch(0.52 0.24 258));
  color: white;
  box-shadow: 0 2px 12px oklch(0.62 0.22 258 / 0.25);
}

.quiz-btn-primary:hover {
  transform: translateY(-1px);
  box-shadow: 0 4px 20px oklch(0.62 0.22 258 / 0.35);
}

.quiz-btn-primary:disabled {
  opacity: 0.4;
  cursor: not-allowed;
  transform: none;
}

.quiz-btn-ghost {
  background: transparent;
  color: var(--quiz-muted);
}

.quiz-btn-ghost:hover {
  color: var(--quiz-text);
  background: var(--quiz-bg);
}

/* =============================================
   RESULTS
   ============================================= */

.results-container {
  display: none;
  animation: fadeSlideUp 0.6s ease;
}

@keyframes fadeSlideUp {
  from { opacity: 0; transform: translateY(20px); }
  to { opacity: 1; transform: translateY(0); }
}

.results-header {
  text-align: center;
  margin-bottom: 2rem;
}

.results-header h2 {
  font-size: 1.75rem;
  font-weight: 700;
  margin-bottom: 0.5rem;
}

.results-header p {
  color: var(--quiz-muted);
  font-size: 1rem;
}

.results-score-summary {
  display: flex;
  justify-content: center;
  gap: 1rem;
  margin-bottom: 2rem;
  flex-wrap: wrap;
}

.score-badge {
  display: flex;
  align-items: center;
  gap: 0.5rem;
  padding: 0.5rem 1rem;
  background: var(--quiz-card-bg);
  border: 1px solid var(--quiz-border);
  border-radius: 100px;
  font-size: 0.85rem;
  font-weight: 500;
}

.score-badge .score-dot {
  width: 8px;
  height: 8px;
  border-radius: 50%;
  display: inline-block;
}

/* Result cards */
.result-card {
  background: var(--quiz-card-bg);
  border: 1px solid var(--quiz-border);
  border-radius: var(--quiz-radius);
  padding: 1.5rem;
  margin-bottom: 1rem;
  box-shadow: 0 4px 16px oklch(0 0 0 / 0.04);
  transition: all var(--quiz-transition);
  position: relative;
  overflow: hidden;
}

.result-card:first-of-type {
  border-color: oklch(0.62 0.22 258 / 0.3);
  box-shadow: 0 4px 24px oklch(0.62 0.22 258 / 0.1);
}

.result-card:first-of-type::before {
  content: '🏆 Best Match';
  position: absolute;
  top: 0.75rem;
  right: 0.75rem;
  font-size: 0.7rem;
  font-weight: 700;
  text-transform: uppercase;
  letter-spacing: 0.05em;
  padding: 0.25rem 0.75rem;
  background: linear-gradient(135deg, oklch(0.62 0.22 258), oklch(0.72 0.18 78));
  color: white;
  border-radius: 100px;
}

.result-card:hover {
  transform: translateY(-2px);
  box-shadow: 0 8px 32px oklch(0 0 0 / 0.08);
}

.result-card-header {
  display: flex;
  justify-content: space-between;
  align-items: flex-start;
  gap: 1rem;
  margin-bottom: 0.75rem;
}

.result-card-left {
  display: flex;
  align-items: center;
  gap: 1rem;
}

.result-logo {
  width: 48px;
  height: 48px;
  border-radius: 12px;
  display: flex;
  align-items: center;
  justify-content: center;
  font-weight: 800;
  font-size: 1rem;
  color: white;
  flex-shrink: 0;
}

.result-card-info h3 {
  font-size: 1.15rem;
  font-weight: 700;
  margin: 0 0 0.15rem;
}

.result-card-info .tagline {
  font-size: 0.85rem;
  color: var(--quiz-muted);
}

.result-card-right {
  text-align: right;
  flex-shrink: 0;
}

.result-price {
  font-size: 1.1rem;
  font-weight: 700;
  color: var(--quiz-primary);
}

.result-label {
  font-size: 0.7rem;
  text-transform: uppercase;
  letter-spacing: 0.05em;
  color: var(--quiz-muted);
}

.result-match-pct {
  display: inline-flex;
  align-items: center;
  gap: 0.35rem;
  font-size: 0.85rem;
  font-weight: 600;
  color: var(--quiz-primary);
}

.result-match-bar {
  width: 100%;
  height: 4px;
  background: var(--quiz-border);
  border-radius: 2px;
  margin: 0.75rem 0;
  overflow: hidden;
}

.result-match-fill {
  height: 100%;
  border-radius: 2px;
  transition: width 1s cubic-bezier(0.34, 1.56, 0.64, 1);
}

.result-tags {
  display: flex;
  gap: 0.375rem;
  flex-wrap: wrap;
  margin-bottom: 0.75rem;
}

.result-tag {
  font-size: 0.7rem;
  font-weight: 600;
  padding: 0.2rem 0.6rem;
  border-radius: 100px;
  background: var(--quiz-bg);
  color: var(--quiz-muted);
  border: 1px solid var(--quiz-border);
}

.result-reason {
  font-size: 0.9rem;
  color: var(--quiz-muted);
  line-height: 1.5;
  margin-bottom: 1rem;
  padding: 0.75rem 1rem;
  background: var(--quiz-bg);
  border-radius: 8px;
  border-left: 3px solid var(--quiz-primary);
}

.result-cta {
  display: inline-flex;
  align-items: center;
  gap: 0.5rem;
  padding: 0.625rem 1.25rem;
  background: linear-gradient(135deg, var(--quiz-primary), oklch(0.52 0.24 258));
  color: white;
  text-decoration: none;
  border-radius: 8px;
  font-weight: 600;
  font-size: 0.85rem;
  transition: all var(--quiz-transition);
}

.result-cta:hover {
  transform: translateY(-1px);
  box-shadow: 0 4px 16px oklch(0.62 0.22 258 / 0.3);
}

.result-read-review {
  display: inline-flex;
  align-items: center;
  gap: 0.35rem;
  color: var(--quiz-primary);
  text-decoration: none;
  font-size: 0.85rem;
  font-weight: 500;
  margin-left: 0.75rem;
}

/* =============================================
   EMAIL CAPTURE MODAL
   ============================================= */

.email-overlay {
  display: none;
  position: fixed;
  inset: 0;
  background: oklch(0 0 0 / 0.4);
  backdrop-filter: blur(4px);
  z-index: 1000;
  align-items: center;
  justify-content: center;
  padding: 1rem;
  animation: fadeIn 0.3s ease;
}

.email-overlay.active {
  display: flex;
}

@keyframes fadeIn {
  from { opacity: 0; }
  to { opacity: 1; }
}

.email-modal {
  background: var(--quiz-card-bg);
  border-radius: var(--quiz-radius);
  padding: 2.5rem;
  max-width: 440px;
  width: 100%;
  text-align: center;
  box-shadow: 0 24px 64px oklch(0 0 0 / 0.2);
  animation: slideUpModal 0.4s cubic-bezier(0.34, 1.56, 0.64, 1);
  position: relative;
}

@keyframes slideUpModal {
  from { opacity: 0; transform: translateY(30px) scale(0.95); }
  to { opacity: 1; transform: translateY(0) scale(1); }
}

.email-modal .modal-icon {
  font-size: 2.5rem;
  margin-bottom: 0.75rem;
}

.email-modal h3 {
  font-size: 1.35rem;
  font-weight: 700;
  margin-bottom: 0.5rem;
}

.email-modal p {
  color: var(--quiz-muted);
  font-size: 0.9rem;
  margin-bottom: 1.5rem;
  line-height: 1.5;
}

.email-modal .email-form {
  display: flex;
  flex-direction: column;
  gap: 0.75rem;
}

.email-modal input[type="email"] {
  padding: 0.875rem 1rem;
  border: 2px solid var(--quiz-border);
  border-radius: 10px;
  font-size: 0.95rem;
  background: var(--quiz-bg);
  color: var(--quiz-text);
  outline: none;
  transition: border-color var(--quiz-transition);
}

.email-modal input[type="email"]:focus {
  border-color: var(--quiz-primary);
  box-shadow: 0 0 0 3px oklch(0.62 0.22 258 / 0.15);
}

.email-modal .email-submit {
  padding: 0.875rem;
  border: none;
  border-radius: 10px;
  background: linear-gradient(135deg, var(--quiz-primary), oklch(0.52 0.24 258));
  color: white;
  font-weight: 700;
  font-size: 0.95rem;
  cursor: pointer;
  transition: all var(--quiz-transition);
}

.email-modal .email-submit:hover {
  transform: translateY(-1px);
  box-shadow: 0 4px 16px oklch(0.62 0.22 258 / 0.3);
}

.email-modal .email-skip {
  display: inline-block;
  margin-top: 1rem;
  font-size: 0.8rem;
  color: var(--quiz-muted);
  cursor: pointer;
  background: none;
  border: none;
  text-decoration: underline;
  text-underline-offset: 2px;
}

.email-modal .email-skip:hover {
  color: var(--quiz-text);
}

.email-modal .privacy-note {
  font-size: 0.7rem;
  color: var(--quiz-muted);
  margin-top: 0.75rem;
  opacity: 0.7;
}

.email-modal .close-modal {
  position: absolute;
  top: 0.75rem;
  right: 0.75rem;
  background: none;
  border: none;
  font-size: 1.25rem;
  cursor: pointer;
  color: var(--quiz-muted);
  padding: 0.25rem;
  line-height: 1;
  border-radius: 6px;
  transition: all var(--quiz-transition);
}

.email-modal .close-modal:hover {
  color: var(--quiz-text);
  background: var(--quiz-bg);
}

.email-modal .success-state {
  display: none;
}

.email-modal .success-state.active {
  display: block;
}

.email-modal .success-state .checkmark {
  width: 56px;
  height: 56px;
  border-radius: 50%;
  background: oklch(0.62 0.18 145 / 0.15);
  display: flex;
  align-items: center;
  justify-content: center;
  margin: 0 auto 1rem;
  font-size: 1.5rem;
}

/* =============================================
   RESPONSIVE
   ============================================= */

@media (max-width: 600px) {
  .matchmaker-hero h1 { font-size: 1.75rem; }
  .quiz-card { padding: 1.25rem; }
  .quiz-question-text { font-size: 1.05rem; }
  .quiz-option label { padding: 0.75rem 1rem; font-size: 0.9rem; }
  .result-card-header { flex-direction: column; }
  .result-card-right { text-align: left; }
  .email-modal { padding: 1.5rem; margin: 0.5rem; }
  .matchmaker-hero .trust-badges { gap: 1rem; font-size: 0.75rem; }
}

/* Loading state for results */
.quiz-loading {
  text-align: center;
  padding: 3rem;
  display: none;
}

.quiz-loading .spinner {
  width: 40px;
  height: 40px;
  border: 3px solid var(--quiz-border);
  border-top-color: var(--quiz-primary);
  border-radius: 50%;
  animation: spin 0.8s linear infinite;
  margin: 0 auto 1rem;
}

@keyframes spin {
  to { transform: rotate(360deg); }
}
</style>

<div class="matchmaker-hero">
  <h1>Find Your <span class="highlight">Perfect Host</span></h1>
  <p>Answer 6 quick questions and get a personalized hosting recommendation based on your budget, traffic, and technical skill level. No fluff — just the best provider for you.</p>
  <div class="trust-badges">
    <span>⚡ 2 minutes · 6 questions</span>
    <span>🔬 Data-driven matching</span>
    <span>🔒 No spam — ever</span>
  </div>
</div>

<!-- QUIZ CONTAINER -->
<div class="quiz-container">
  <div class="quiz-progress">
    <div class="quiz-progress-track">
      <div class="quiz-progress-fill" id="progressFill"></div>
    </div>
    <span class="quiz-step-indicator" id="stepIndicator">1 of 6</span>
  </div>

  <!-- QUIZ CARD -->
  <div class="quiz-card" id="quizCard">
    <div class="quiz-question-number" id="questionNumber">Question 1</div>
    <div class="quiz-question-text" id="questionText">Loading...</div>
    <div class="quiz-options" id="quizOptions"></div>
    <div class="quiz-nav">
      <button class="quiz-btn quiz-btn-ghost" id="prevBtn" onclick="prevStep()">← Back</button>
      <button class="quiz-btn quiz-btn-primary" id="nextBtn" onclick="nextStep()" disabled>Next →</button>
    </div>
  </div>

  <!-- LOADING -->
  <div class="quiz-loading" id="quizLoading">
    <div class="spinner"></div>
    <p>Analyzing your answers...</p>
  </div>

  <!-- RESULTS -->
  <div class="results-container" id="resultsContainer">
    <div class="results-header">
      <h2>Your Top Hosting Matches</h2>
      <p>Based on your answers, here are the best hosting providers for you</p>
    </div>

    <div class="results-score-summary" id="scoreSummary"></div>
    <div id="resultsList"></div>

    <div style="text-align: center; margin-top: 2rem;">
      <p style="color: var(--quiz-muted); font-size: 0.85rem; margin-bottom: 0.5rem;">Not what you're looking for?</p>
      <button class="quiz-btn quiz-btn-ghost" onclick="resetQuiz()" style="margin: 0 auto;">↻ Retake the Quiz</button>
    </div>
  </div>
</div>

<script>
// =============================================
// HOSTING PROVIDER DATABASE
// =============================================

const PROVIDERS = [
  {
    id: 'siteground',
    name: 'SiteGround',
    logoStyle: 'background: linear-gradient(135deg, #0FAA73, #0C8E5F);',
    initial: 'SG',
    tagline: 'Best all-around shared hosting',
    url: 'https://www.siteground.com/index.htm?afcode=6bb2259c82be1f061bb3f97d28a48550/',
    reviewUrl: '{{ site.baseurl }}/category/hosting/',
    price: '$3.99/mo',
    tags: ['Beginner', 'Support', 'WordPress'],
    // Category: budget|mid|premium|enterprise|dev
    categories: ['shared', 'managed-wp'],
    // Scores per answer dimension (0-10)
    scores: {
      budget_ultra: 5, budget_mid: 9, budget_premium: 6, budget_enterprise: 2,  // budget preference
      site_blog: 9, site_ecommerce: 7, site_high_traffic: 5, site_agency: 5, site_app: 3,  // site type
      traffic_low: 9, traffic_medium: 8, traffic_high: 5, traffic_extreme: 2,  // traffic
      skill_beginner: 10, skill_cpanel: 9, skill_cli: 4, skill_dev: 3,  // skill level
      priority_price: 7, priority_speed: 8, priority_support: 10, priority_ease: 10, priority_scale: 4,  // priority
      wp_managed: 9, wp_unmanaged: 3, wp_either: 7  // management preference
    }
  },
  {
    id: 'bluehost',
    name: 'Bluehost',
    logoStyle: 'background: linear-gradient(135deg, #2C6FD1, #1E4F9E);',
    initial: 'BH',
    tagline: 'Official WordPress.org #1 recommended',
    url: 'https://bluehost.sjv.io/c/7392811/1376228/11352',
    reviewUrl: '{{ site.baseurl }}/category/hosting/',
    price: '$3.79/mo',
    tags: ['WordPress', 'Beginner', 'Budget'],
    categories: ['shared', 'managed-wp'],
    scores: {
      budget_ultra: 7, budget_mid: 9, budget_premium: 4, budget_enterprise: 1,
      site_blog: 10, site_ecommerce: 7, site_high_traffic: 4, site_agency: 4, site_app: 2,
      traffic_low: 10, traffic_medium: 7, traffic_high: 3, traffic_extreme: 1,
      skill_beginner: 10, skill_cpanel: 9, skill_cli: 3, skill_dev: 2,
      priority_price: 9, priority_speed: 5, priority_support: 6, priority_ease: 10, priority_scale: 2,
      wp_managed: 10, wp_unmanaged: 2, wp_either: 7
    }
  },
  {
    id: 'hostinger',
    name: 'Hostinger',
    logoStyle: 'background: linear-gradient(135deg, #673DE6, #4A28B3);',
    initial: 'H',
    tagline: "Best ultra-budget hosting",
    url: 'https://www.hostinger.com/',
    reviewUrl: '{{ site.baseurl }}/category/hosting/',
    price: '$2.99/mo',
    tags: ['Budget', 'Beginner', 'Performant'],
    categories: ['shared', 'vps', 'managed-wp'],
    scores: {
      budget_ultra: 10, budget_mid: 8, budget_premium: 3, budget_enterprise: 1,
      site_blog: 9, site_ecommerce: 6, site_high_traffic: 4, site_agency: 5, site_app: 5,
      traffic_low: 10, traffic_medium: 8, traffic_high: 4, traffic_extreme: 1,
      skill_beginner: 9, skill_cpanel: 8, skill_cli: 5, skill_dev: 4,
      priority_price: 10, priority_speed: 7, priority_support: 5, priority_ease: 8, priority_scale: 4,
      wp_managed: 7, wp_unmanaged: 5, wp_either: 8
    }
  },
  {
    id: 'cloudways',
    name: 'Cloudways',
    logoStyle: 'background: linear-gradient(135deg, #5A2EFF, #3B1FCC);',
    initial: 'CW',
    tagline: 'Managed cloud for developers',
    url: 'https://www.cloudways.com/en/?id=2179745',
    reviewUrl: '{{ site.baseurl }}/category/hosting/',
    price: '$11/mo',
    tags: ['Developers', 'Scalable', 'Cloud'],
    categories: ['cloud', 'managed-wp'],
    scores: {
      budget_ultra: 2, budget_mid: 6, budget_premium: 8, budget_enterprise: 6,
      site_blog: 5, site_ecommerce: 8, site_high_traffic: 9, site_agency: 9, site_app: 9,
      traffic_low: 4, traffic_medium: 7, traffic_high: 9, traffic_extreme: 7,
      skill_beginner: 3, skill_cpanel: 5, skill_cli: 8, skill_dev: 9,
      priority_price: 4, priority_speed: 9, priority_support: 8, priority_ease: 5, priority_scale: 10,
      wp_managed: 8, wp_unmanaged: 7, wp_either: 9
    }
  },
  {
    id: 'interserver',
    name: 'InterServer',
    logoStyle: 'background: linear-gradient(135deg, #E65100, #BF4300);',
    initial: 'IS',
    tagline: 'Best value VPS hosting',
    url: 'https://www.interserver.net/r/1155259',
    reviewUrl: '{{ site.baseurl }}/category/hosting/',
    price: '$2.50/mo',
    tags: ['VPS', 'Budget', 'Reliable'],
    categories: ['shared', 'vps'],
    scores: {
      budget_ultra: 10, budget_mid: 7, budget_premium: 3, budget_enterprise: 1,
      site_blog: 7, site_ecommerce: 6, site_high_traffic: 6, site_agency: 6, site_app: 7,
      traffic_low: 7, traffic_medium: 8, traffic_high: 6, traffic_extreme: 3,
      skill_beginner: 5, skill_cpanel: 7, skill_cli: 7, skill_dev: 7,
      priority_price: 10, priority_speed: 6, priority_support: 7, priority_ease: 6, priority_scale: 6,
      wp_managed: 4, wp_unmanaged: 8, wp_either: 7
    }
  },
  {
    id: 'scalahosting',
    name: 'ScalaHosting',
    logoStyle: 'background: linear-gradient(135deg, #F7941E, #D97E14);',
    initial: 'SH',
    tagline: 'Managed VPS with SPanel',
    url: 'https://www.scalahosting.com/managed-cloud-hosting.html',
    reviewUrl: '{{ site.baseurl }}/category/hosting/',
    price: '$9.95/mo',
    tags: ['VPS', 'Managed', 'SPanel'],
    categories: ['vps', 'managed-wp'],
    scores: {
      budget_ultra: 3, budget_mid: 7, budget_premium: 8, budget_enterprise: 4,
      site_blog: 7, site_ecommerce: 8, site_high_traffic: 8, site_agency: 8, site_app: 7,
      traffic_low: 5, traffic_medium: 7, traffic_high: 8, traffic_extreme: 5,
      skill_beginner: 5, skill_cpanel: 8, skill_cli: 6, skill_dev: 6,
      priority_price: 5, priority_speed: 8, priority_support: 9, priority_ease: 7, priority_scale: 8,
      wp_managed: 7, wp_unmanaged: 6, wp_either: 8
    }
  },
  {
    id: 'digitalocean',
    name: 'DigitalOcean',
    logoStyle: 'background: linear-gradient(135deg, #0060FF, #0044CC);',
    initial: 'DO',
    tagline: 'Developer cloud platform',
    url: 'https://www.digitalocean.com/',
    reviewUrl: '{{ site.baseurl }}/category/hosting/',
    price: '$4/mo',
    tags: ['Developers', 'VPS', 'Cloud'],
    categories: ['vps', 'cloud'],
    scores: {
      budget_ultra: 6, budget_mid: 8, budget_premium: 7, budget_enterprise: 6,
      site_blog: 4, site_ecommerce: 6, site_high_traffic: 8, site_agency: 9, site_app: 10,
      traffic_low: 5, traffic_medium: 7, traffic_high: 9, traffic_extreme: 9,
      skill_beginner: 1, skill_cpanel: 3, skill_cli: 9, skill_dev: 10,
      priority_price: 7, priority_speed: 9, priority_support: 4, priority_ease: 2, priority_scale: 10,
      wp_managed: 2, wp_unmanaged: 10, wp_either: 5
    }
  },
  {
    id: 'vultr',
    name: 'Vultr',
    logoStyle: 'background: linear-gradient(135deg, #007BFC, #0055AA);',
    initial: 'V',
    tagline: 'High-performance cloud VPS',
    url: 'https://www.vultr.com/',
    reviewUrl: '{{ site.baseurl }}/category/hosting/',
    price: '$2.50/mo',
    tags: ['Developers', 'VPS', 'Global'],
    categories: ['vps', 'cloud'],
    scores: {
      budget_ultra: 8, budget_mid: 8, budget_premium: 7, budget_enterprise: 6,
      site_blog: 4, site_ecommerce: 6, site_high_traffic: 8, site_agency: 9, site_app: 10,
      traffic_low: 6, traffic_medium: 7, traffic_high: 9, traffic_extreme: 9,
      skill_beginner: 1, skill_cpanel: 3, skill_cli: 9, skill_dev: 10,
      priority_price: 8, priority_speed: 9, priority_support: 3, priority_ease: 2, priority_scale: 10,
      wp_managed: 2, wp_unmanaged: 10, wp_either: 5
    }
  },
  {
    id: 'kinsta',
    name: 'Kinsta',
    logoStyle: 'background: linear-gradient(135deg, #5333ED, #3D1FB5);',
    initial: 'K',
    tagline: 'Premium managed WordPress',
    url: 'https://kinsta.com/',
    reviewUrl: '{{ site.baseurl }}/category/hosting/',
    price: '$35/mo',
    tags: ['Premium', 'WordPress', 'Speed'],
    categories: ['managed-wp', 'premium'],
    scores: {
      budget_ultra: 1, budget_mid: 2, budget_premium: 8, budget_enterprise: 9,
      site_blog: 6, site_ecommerce: 9, site_high_traffic: 10, site_agency: 9, site_app: 4,
      traffic_low: 3, traffic_medium: 5, traffic_high: 10, traffic_extreme: 10,
      skill_beginner: 3, skill_cpanel: 5, skill_cli: 5, skill_dev: 6,
      priority_price: 1, priority_speed: 10, priority_support: 10, priority_ease: 6, priority_scale: 9,
      wp_managed: 10, wp_unmanaged: 1, wp_either: 6
    }
  },
  {
    id: 'wpengine',
    name: 'WP Engine',
    logoStyle: 'background: linear-gradient(135deg, #31A3DD, #1F7EB0);',
    initial: 'WPE',
    tagline: 'Enterprise WordPress hosting',
    url: 'https://wpengine.com/',
    reviewUrl: '{{ site.baseurl }}/category/hosting/',
    price: '$20/mo',
    tags: ['Enterprise', 'WordPress', 'Support'],
    categories: ['managed-wp', 'premium'],
    scores: {
      budget_ultra: 1, budget_mid: 3, budget_premium: 7, budget_enterprise: 9,
      site_blog: 5, site_ecommerce: 8, site_high_traffic: 10, site_agency: 9, site_app: 3,
      traffic_low: 3, traffic_medium: 5, traffic_high: 9, traffic_extreme: 10,
      skill_beginner: 4, skill_cpanel: 6, skill_cli: 5, skill_dev: 5,
      priority_price: 2, priority_speed: 8, priority_support: 9, priority_ease: 6, priority_scale: 9,
      wp_managed: 10, wp_unmanaged: 1, wp_either: 6
    }
  }
];

// =============================================
// QUIZ DATA
// =============================================

const questions = [
  {
    id: 'budget',
    text: "What's your monthly hosting budget?",
    icon: '💰',
    options: [
      { value: 'ultra', label: 'Under $5/mo — as cheap as possible', icon: '🪙' },
      { value: 'mid', label: '$5–$15/mo — good value for features', icon: '💵' },
      { value: 'premium', label: '$15–$40/mo — premium performance', icon: '💎' },
      { value: 'enterprise', label: '$40+/mo — enterprise-grade', icon: '🏢' }
    ]
  },
  {
    id: 'site',
    text: 'What kind of website are you building?',
    icon: '🌐',
    options: [
      { value: 'blog', label: 'Blog or personal site', icon: '✍️' },
      { value: 'ecommerce', label: 'E-commerce / online store', icon: '🛒' },
      { value: 'high_traffic', label: 'High-traffic media / membership site', icon: '📈' },
      { value: 'agency', label: 'Client sites / agency work', icon: '👥' },
      { value: 'app', label: 'Web app or SaaS', icon: '⚙️' }
    ]
  },
  {
    id: 'traffic',
    text: 'What monthly traffic do you expect?',
    icon: '🚦',
    options: [
      { value: 'low', label: 'Under 1,000 visitors', icon: '🌱' },
      { value: 'medium', label: '1,000–10,000 visitors', icon: '🌿' },
      { value: 'high', label: '10,000–100,000 visitors', icon: '🌳' },
      { value: 'extreme', label: '100,000+ visitors', icon: '🌲' }
    ]
  },
  {
    id: 'skill',
    text: 'How technical are you?',
    icon: '🛠️',
    options: [
      { value: 'beginner', label: "I'm a complete beginner", icon: '🚀' },
      { value: 'cpanel', label: "I'm comfortable with cPanel", icon: '🖥️' },
      { value: 'cli', label: 'I use the command line', icon: '⌨️' },
      { value: 'dev', label: "I'm a developer — give me root access", icon: '⚡' }
    ]
  },
  {
    id: 'priority',
    text: 'What matters most to you?',
    icon: '🎯',
    options: [
      { value: 'price', label: 'Lowest possible price', icon: '🏷️' },
      { value: 'speed', label: 'Raw performance & speed', icon: '⚡' },
      { value: 'support', label: 'Top-notch customer support', icon: '🎧' },
      { value: 'ease', label: 'Ease of use', icon: '😊' },
      { value: 'scale', label: 'Ability to scale later', icon: '📊' }
    ]
  },
  {
    id: 'wp_managed',
    text: 'Managed WordPress or full server control?',
    icon: '🔧',
    options: [
      { value: 'managed', label: 'Managed WordPress — I want it to "just work"', icon: '✨' },
      { value: 'unmanaged', label: 'Raw server access — I want full control', icon: '🔓' },
      { value: 'either', label: "Either — depends on the deal", icon: '🤷' }
    ]
  }
];

// =============================================
// REASONS GENERATOR
// =============================================

const reasons = {
  siteground: (ans) => {
    let r = 'SiteGround has the fastest shared hosting support response times in the industry. Combined with their ';
    if (ans.budget === 'mid' || ans.budget === 'ultra') r += 'aggressive entry pricing, it\'s the best bang for your buck for most site owners.';
    else if (ans.skill === 'beginner') r += 'user-friendly interface and 1-click WordPress installer, it\'s perfect for beginners who don\'t want to compromise on quality.';
    else if (ans.priority === 'support') r += '24/7 support team that averages under 30-second response times, reliability is their core strength.';
    else r += 'proven 99.99% uptime track record, it\'s the safest choice for most website owners.';
    return r;
  },
  bluehost: (ans) => {
    let r = 'As the #1 officially recommended host by WordPress.org, Bluehost is optimized for WordPress from the ground up. ';
    if (ans.site === 'blog') r += 'For a personal blog or simple site, their entry-level plan at $3.79/mo is tough to beat.';
    else if (ans.budget === 'ultra') r += 'At $3.79/mo with a free domain included, it\'s one of the most affordable ways to get started.';
    else r += 'Their custom control panel makes managing your site dead simple, even if you\'ve never hosted before.';
    return r;
  },
  hostinger: (ans) => {
    let r = 'Hostinger consistently delivers the lowest entry price in the industry without sacrificing performance. ';
    if (ans.budget === 'ultra') r += 'At $2.99/mo, nothing beats them on raw price-to-performance ratio.';
    else r += 'Their LiteSpeed servers and custom cache system deliver page loads that compete with hosts costing 3x more.';
    return r;
  },
  cloudways: (ans) => {
    let r = 'Cloudways gives you managed cloud hosting on top of AWS, Google Cloud, or DigitalOcean infrastructure. ';
    if (ans.skill === 'dev' || ans.skill === 'cli') r += 'For developers who want cloud power without the DevOps headache, it\'s the sweet spot.';
    else if (ans.priority === 'scale') r += 'You can scale from $11/mo to enterprise in minutes — perfect for growing sites.';
    else r += 'Pay-as-you-go pricing means you only pay for what you use, with no long-term contracts.';
    return r;
  },
  interserver: (ans) => {
    let r = 'InterServer is the king of affordable VPS hosting. ';
    if (ans.budget === 'ultra') r += 'Their VPS plans start at just $2.50/mo with price-lock guarantees — no sneaky renewal hikes.';
    else r += 'Unmetered storage and bandwidth on most plans, plus their price-lock guarantee means no surprise renewals.';
    return r;
  },
  scalahosting: (ans) => {
    let r = 'ScalaHosting offers fully managed VPS with their own SPanel control panel. ';
    if (ans.priority === 'support') r += 'Their support team is known for going above and beyond, even on budget VPS plans.';
    else r += 'You get dedicated VPS resources with full management — the performance of VPS without the complexity.';
    return r;
  },
  digitalocean: (ans) => {
    let r = 'DigitalOcean is the developer\'s choice for cloud infrastructure. ';
    if (ans.skill === 'dev') r += 'Clean API, predictable pricing, and the best documentation in the industry. If you know the command line, this is home.';
    else if (ans.site === 'app') r += 'Their App Platform lets you deploy straight from GitHub — perfect for web apps and SaaS.';
    else r += 'With 15 global data centers and one-click app deployments, it\'s the most versatile developer cloud.';
    return r;
  },
  vultr: (ans) => {
    let r = 'Vultr offers high-performance cloud VPS with competitive pricing. ';
    if (ans.skill === 'dev') r += 'With 32 global locations and hourly billing, it\'s ideal for developers who need geographic distribution.';
    else r += 'Their AMD and Intel high-performance instances deliver exceptional value for compute-heavy workloads.';
    return r;
  },
  kinsta: (ans) => {
    let r = 'Kinsta is the premium choice for managed WordPress hosting. ';
    if (ans.priority === 'speed') r += 'Built on Google Cloud\'s premium tier network with Cloudflare integration, it\'s the fastest managed WP host we\'ve tested.';
    else if (ans.traffic === 'high' || ans.traffic === 'extreme') r += 'Their auto-scaling infrastructure handles traffic spikes effortlessly — we\'ve tested it at 500K+ visits.';
    else r += 'Enterprise-level security, automatic daily backups, and a custom dashboard that makes site management a pleasure.';
    return r;
  },
  wpengine: (ans) => {
    let r = 'WP Engine is the enterprise standard for WordPress hosting. ';
    if (ans.site === 'ecommerce') r += 'Their WooCommerce-optimized plans and Smart Plugin Manager make it the safest choice for revenue-critical stores.';
    else r += 'With 30+ point WordPress-specific security measures and 24/7 support staffed by WordPress experts, it\'s the gold standard.';
    return r;
  }
};

// =============================================
// QUIZ STATE
// =============================================

let currentStep = 0;
let answers = {};
let answered = {};

function init() {
  // Set up keyboard handlers
  document.addEventListener('keydown', (e) => {
    if (e.key === 'Enter') {
      const nextBtn = document.getElementById('nextBtn');
      if (!nextBtn.disabled) nextStep();
    }
    if (e.key === 'Escape') {
      const overlay = document.querySelector('.email-overlay');
      if (overlay && overlay.classList.contains('active')) {
        skipEmail();
      }
    }
  });

  updateProgress();
  showStep();
}

function showStep() {
  const q = questions[currentStep];
  const card = document.getElementById('quizCard');
  card.style.opacity = '0';
  
  setTimeout(() => {
    document.getElementById('questionNumber').textContent = `Question ${currentStep + 1}`;
    document.getElementById('questionText').textContent = q.text;
    
    const container = document.getElementById('quizOptions');
    container.innerHTML = '';
    
    q.options.forEach((opt, idx) => {
      const div = document.createElement('div');
      div.className = 'quiz-option';
      
      const isChecked = answers[q.id] === opt.value;
      const inputId = `q_${q.id}_${opt.value}`;
      
      div.innerHTML = `
        <input type="radio" name="q_${q.id}" id="${inputId}" value="${opt.value}" ${isChecked ? 'checked' : ''}>
        <label for="${inputId}">
          <span class="option-dot"></span>
          <span class="option-icon">${opt.icon}</span>
          ${opt.label}
        </label>
      `;
      
      container.appendChild(div);
      
      // Auto-advance on select
      div.querySelector('input').addEventListener('change', () => {
        answers[q.id] = opt.value;
        answered[q.id] = true;
        document.getElementById('nextBtn').disabled = false;
        
        // Small delay then advance
        setTimeout(() => {
          if (currentStep < questions.length - 1) {
            nextStep();
          } else {
            showResults();
          }
        }, 300);
      });
    });
    
    // Show/hide back button
    document.getElementById('prevBtn').style.display = currentStep === 0 ? 'none' : 'inline-flex';
    
    // Update next button text
    document.getElementById('nextBtn').textContent = currentStep === questions.length - 1 ? 'See My Matches →' : 'Next →';
    document.getElementById('nextBtn').disabled = !answered[q.id];
    
    card.style.opacity = '1';
    updateProgress();
  }, 150);
}

function nextStep() {
  const q = questions[currentStep];
  if (!answered[q.id]) return;
  
  if (currentStep < questions.length - 1) {
    currentStep++;
    showStep();
    // Scroll to top of quiz
    document.querySelector('.quiz-container').scrollIntoView({ behavior: 'smooth', block: 'start' });
  } else {
    showResults();
  }
}

function prevStep() {
  if (currentStep > 0) {
    currentStep--;
    showStep();
    document.querySelector('.quiz-container').scrollIntoView({ behavior: 'smooth', block: 'start' });
  }
}

function updateProgress() {
  const pct = ((currentStep + 1) / questions.length) * 100;
  document.getElementById('progressFill').style.width = `${pct}%`;
  document.getElementById('stepIndicator').textContent = `${currentStep + 1} of ${questions.length}`;
}

// =============================================
// SCORING ENGINE
// =============================================

function calculateScores() {
  const scored = PROVIDERS.map(p => {
    let score = 0;
    let maxScore = 0;
    const dimensions = [];

    // Budget dimension
    const budgetKey = `budget_${answers.budget}`;
    const budgetScore = p.scores[budgetKey] || 0;
    const budgetWeight = answers.budget === 'ultra' ? 1.5 : answers.budget === 'mid' ? 1.2 : 1.0;
    score += budgetScore * budgetWeight;
    maxScore += 10 * budgetWeight;
    dimensions.push({ name: 'Budget', score: budgetScore * budgetWeight, max: 10 * budgetWeight });

    // Site type dimension
    const siteKey = `site_${answers.site}`;
    const siteScore = p.scores[siteKey] || 0;
    const siteWeight = 1.3;
    score += siteScore * siteWeight;
    maxScore += 10 * siteWeight;
    dimensions.push({ name: 'Site Type', score: siteScore * siteWeight, max: 10 * siteWeight });

    // Traffic dimension
    const trafficKey = `traffic_${answers.traffic}`;
    const trafficScore = p.scores[trafficKey] || 0;
    const trafficWeight = answers.traffic === 'extreme' || answers.traffic === 'high' ? 1.4 : 1.0;
    score += trafficScore * trafficWeight;
    maxScore += 10 * trafficWeight;
    dimensions.push({ name: 'Traffic', score: trafficScore * trafficWeight, max: 10 * trafficWeight });

    // Skill dimension
    const skillKey = `skill_${answers.skill}`;
    const skillScore = p.scores[skillKey] || 0;
    const skillWeight = 1.3;
    score += skillScore * skillWeight;
    maxScore += 10 * skillWeight;
    dimensions.push({ name: 'Skill', score: skillScore * skillWeight, max: 10 * skillWeight });

    // Priority dimension
    const priorityKey = `priority_${answers.priority}`;
    const priorityScore = p.scores[priorityKey] || 0;
    const priorityWeight = 1.5;
    score += priorityScore * priorityWeight;
    maxScore += 10 * priorityWeight;
    dimensions.push({ name: 'Priority', score: priorityScore * priorityWeight, max: 10 * priorityWeight });

    // WP management dimension
    const wpKey = `wp_${answers.wp_managed}`;
    const wpScore = p.scores[wpKey] || 0;
    const wpWeight = 1.2;
    score += wpScore * wpWeight;
    maxScore += 10 * wpWeight;
    dimensions.push({ name: 'Control', score: wpScore * wpWeight, max: 10 * wpWeight });

    const pct = Math.round((score / maxScore) * 100);

    return {
      ...p,
      score: pct,
      dimensions
    };
  });

  return scored.sort((a, b) => b.score - a.score).filter(p => p.score > 15);
}

// =============================================
// RESULTS
// =============================================

function showResults() {
  // Show loading state
  document.getElementById('quizCard').style.display = 'none';
  document.getElementById('quizLoading').style.display = 'block';
  document.querySelector('.quiz-progress').style.display = 'none';

  // Show email modal first
  setTimeout(() => {
    document.getElementById('quizLoading').style.display = 'none';
    showEmailModal();
  }, 800);
}

function showEmailModal() {
  const overlay = document.getElementById('emailOverlay');
  overlay.classList.add('active');
  document.getElementById('emailInput').focus();
}

function submitEmail() {
  const email = document.getElementById('emailInput').value.trim();
  if (!email || !email.includes('@') || !email.includes('.')) {
    document.getElementById('emailInput').style.borderColor = 'oklch(0.58 0.22 25)';
    return;
  }

  // Save to localStorage
  localStorage.setItem('ts_email', email);
  localStorage.setItem('ts_email_date', new Date().toISOString());

  // Show success state
  document.getElementById('emailForm').style.display = 'none';
  document.getElementById('emailSuccess').classList.add('active');

  // Close & show results after brief delay
  setTimeout(() => {
    document.getElementById('emailOverlay').classList.remove('active');
    document.getElementById('emailForm').style.display = 'flex';
    document.getElementById('emailSuccess').classList.remove('active');
    renderResults();
  }, 1500);
}

function skipEmail() {
  document.getElementById('emailOverlay').classList.remove('active');
  document.getElementById('emailForm').style.display = 'flex';
  document.getElementById('emailSuccess').classList.remove('active');
  renderResults();
}

function renderResults() {
  const scored = calculateScores();
  const top3 = scored.slice(0, 3);
  const others = scored.slice(3, 6);

  document.getElementById('resultsContainer').style.display = 'block';
  document.getElementById('resultsContainer').scrollIntoView({ behavior: 'smooth', block: 'start' });

  // Score summary badges
  const summary = document.getElementById('scoreSummary');
  summary.innerHTML = '';
  const badges = [
    { label: `${scored.length} providers analyzed`, icon: '📊' },
    { label: `${top3[0].score}% match (top pick)`, icon: '🎯' }
  ];
  badges.forEach(b => {
    const el = document.createElement('div');
    el.className = 'score-badge';
    el.innerHTML = `${b.icon} ${b.label}`;
    summary.appendChild(el);
  });

  // Results list
  const list = document.getElementById('resultsList');
  list.innerHTML = '';

  // Get the match reason
  function getReason(p, index) {
    const fn = reasons[p.id];
    if (fn) return fn(answers);
    return `Based on your ${answers.budget} budget, ${answers.site} site type, and ${answers.skill} skill level, ${p.name} is a strong match.`;
  }

  top3.forEach((p, i) => {
    const logos = {
      siteground: '#0FAA73', bluehost: '#2C6FD1', hostinger: '#673DE6',
      cloudways: '#5A2EFF', interserver: '#E65100', scalahosting: '#F7941E',
      digitalocean: '#0060FF', vultr: '#007BFC', kinsta: '#5333ED',
      wpengine: '#31A3DD'
    };
    const color = logos[p.id] || 'var(--quiz-primary)';
    const reason = getReason(p, i);

    const card = document.createElement('div');
    card.className = 'result-card';
    card.style.setProperty('--card-color', color);
    card.innerHTML = `
      <div class="result-card-header">
        <div class="result-card-left">
          <div class="result-logo" style="background: ${p.logoStyle}">${p.initial}</div>
          <div class="result-card-info">
            <h3>${p.name}</h3>
            <div class="tagline">${p.tagline}</div>
          </div>
        </div>
        <div class="result-card-right">
          <div class="result-price">${p.price}</div>
          <div class="result-label">Starting price</div>
        </div>
      </div>
      <div class="result-match-bar">
        <div class="result-match-fill" style="width: 0%; background: linear-gradient(90deg, ${color}, ${color}88);"></div>
      </div>
      <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 0.75rem;">
        <span class="result-match-pct">${p.score}% match</span>
        <div class="result-tags">
          ${p.tags.map(t => `<span class="result-tag">${t}</span>`).join('')}
        </div>
      </div>
      <div class="result-reason">${reason}</div>
      <div>
        <a href="${p.url}" target="_blank" rel="nofollow sponsored" class="result-cta">Visit ${p.name} →</a>
        <a href="${p.reviewUrl}" class="result-read-review">Read review →</a>
      </div>
    `;
    list.appendChild(card);

    // Animate the match bar
    setTimeout(() => {
      card.querySelector('.result-match-fill').style.width = `${p.score}%`;
    }, 200 + i * 200);
  });

  // Scroll to results
  setTimeout(() => {
    document.getElementById('resultsContainer').scrollIntoView({ behavior: 'smooth', block: 'start' });
  }, 300);
}

function resetQuiz() {
  currentStep = 0;
  answers = {};
  answered = {};
  
  document.getElementById('resultsContainer').style.display = 'none';
  document.getElementById('quizCard').style.display = 'block';
  document.querySelector('.quiz-progress').style.display = 'flex';
  document.getElementById('quizLoading').style.display = 'none';
  
  showStep();
  window.scrollTo({ top: 0, behavior: 'smooth' });
}

// =============================================
// EMAIL MODAL HTML — injected into DOM
// =============================================

document.addEventListener('DOMContentLoaded', () => {
  const modalHTML = `
  <div class="email-overlay" id="emailOverlay">
    <div class="email-modal">
      <button class="close-modal" onclick="skipEmail()">✕</button>
      <div class="modal-icon">🎯</div>
      <h3>Want to save these results?</h3>
      <p>Enter your email and we'll send you your personalized matches plus exclusive hosting deals.</p>
      <div class="email-form" id="emailForm">
        <input type="email" id="emailInput" placeholder="you@example.com" autocomplete="email">
        <button class="email-submit" onclick="submitEmail()">Send My Matches →</button>
        <button class="email-skip" onclick="skipEmail()">No thanks, show me my results</button>
        <div class="privacy-note">🔒 No spam. Unsubscribe anytime.</div>
      </div>
      <div class="success-state" id="emailSuccess">
        <div class="checkmark">✅</div>
        <h3>You're all set!</h3>
        <p style="margin-bottom: 0;">Loading your results now...</p>
      </div>
    </div>
  </div>`;

  const container = document.querySelector('.quiz-container');
  container.insertAdjacentHTML('afterend', modalHTML);

  // Close on overlay click
  document.getElementById('emailOverlay').addEventListener('click', (e) => {
    if (e.target === e.currentTarget) skipEmail();
  });
  
  init();
});
</script>

<noscript>
  <div style="text-align: center; padding: 3rem; background: var(--bg-card); border-radius: var(--radius); border: 1px solid var(--border);">
    <h2>JavaScript Required</h2>
    <p>This interactive quiz tool needs JavaScript enabled. Please enable it or browse our <a href="{{ site.baseurl }}/">full hosting reviews here</a>.</p>
  </div>
</noscript>

#!/usr/bin/env python3
"""Generate the Affiliate Marketing Starter Kit PDF"""

from fpdf import FPDF
import os

class KitPDF(FPDF):
    def __init__(self):
        super().__init__()
        # Add Unicode fonts
        self.add_font('Arial', '', 'C:/Windows/Fonts/arial.ttf', uni=True)
        self.add_font('Arial', 'B', 'C:/Windows/Fonts/arialbd.ttf', uni=True)
        self.add_font('Arial', 'I', 'C:/Windows/Fonts/ariali.ttf', uni=True)
        self.add_font('Arial', 'BI', 'C:/Windows/Fonts/arialbi.ttf', uni=True)

    def header(self):
        pass

    def footer(self):
        self.set_y(-15)
        self.set_font('Arial', 'I', 8)
        self.set_text_color(140, 140, 140)
        self.cell(0, 10, f'Page {self.page_no()}/{{nb}}', 0, 0, 'C')

    def title_page(self):
        self.add_page()
        self.ln(60)
        # Title
        self.set_font('Arial', 'B', 28)
        self.set_text_color(30, 30, 30)
        self.cell(0, 15, 'Affiliate Marketing', 0, 0, 'C')
        self.ln(14)
        self.cell(0, 15, 'Starter Kit', 0, 0, 'C')
        self.ln(25)
        # Subtitle
        self.set_font('Arial', '', 12)
        self.set_text_color(100, 100, 100)
        self.cell(0, 8, 'The exact system I use to run a fully automated', 0, 0, 'C')
        self.ln(7)
        self.cell(0, 8, 'affiliate content engine', 0, 0, 'C')
        self.ln(20)
        # Separator
        self.set_draw_color(200, 200, 200)
        self.set_line_width(0.5)
        x = self.get_x()
        self.line(60, self.get_y(), 150, self.get_y())
        self.ln(15)
        # Author
        self.set_font('Arial', '', 10)
        self.set_text_color(120, 120, 120)
        self.cell(0, 6, 'Jonathan Brown', 0, 0, 'C')
        self.ln(6)
        self.cell(0, 6, 'Tech & SaaS Stack', 0, 0, 'C')
        self.ln(6)
        self.cell(0, 6, '2026 Edition  v1.0', 0, 0, 'C')
        self.ln(25)
        self.set_font('Arial', 'I', 9)
        self.set_text_color(160, 160, 160)
        self.cell(0, 6, 'Price: $17  |  Instant Download  |  30-Day Money-Back Guarantee', 0, 0, 'C')

    def section_title(self, num, title):
        self.ln(8)
        self.set_font('Arial', 'B', 18)
        self.set_text_color(30, 30, 30)
        self.cell(0, 12, f'{num}. {title}', 0, 1, 'L')
        self.set_draw_color(50, 150, 255)
        self.set_line_width(0.8)
        self.line(10, self.get_y(), 60, self.get_y())
        self.ln(4)

    def body_text(self, text):
        self.set_font('Arial', '', 10)
        self.set_text_color(50, 50, 50)
        self.multi_cell(0, 5.5, text)
        self.ln(2)

    def bullet(self, text):
        x = self.get_x()
        self.set_font('Arial', '', 10)
        self.set_text_color(50, 50, 50)
        self.cell(8, 5.5, '', 0, 0)
        self.cell(4, 5.5, chr(8226), 0, 0)
        self.multi_cell(0, 5.5, text)
        self.ln(1)

    def sub_heading(self, text):
        self.ln(2)
        self.set_font('Arial', 'B', 12)
        self.set_text_color(40, 40, 40)
        self.cell(0, 8, text, 0, 1, 'L')
        self.ln(1)

pdf = KitPDF()
pdf.alias_nb_pages()

# ─── TITLE PAGE ───
pdf.title_page()

# ─── SECTION 1: Niche Selection ───
pdf.section_title(1, 'Niche Selection Framework')
pdf.body_text(
    'Most affiliate marketers fail before they start -- because they pick the wrong niche. '
    'The niche is the foundation everything else builds on. Change the niche, and your content strategy, '
    'monetization path, and earning potential all change with it.'
)
pdf.sub_heading('The 13 Questions')
questions = [
    'Do I personally use or care about products in this space? (If no, move on.)',
    'Is there a clear problem this niche solves? (Pain = profit.)',
    'Can I write 50+ articles without running out of ideas?',
    'Do affiliate programs exist? (Check Amazon, ShareASale, Impact, PartnerStack.)',
    'Are commissions at least 5-10% or a flat fee above $20?',
    'Is the average order value above $30? (Higher = better ROI on content.)',
    'Do people search for solutions? (Use Google Suggest, AnswerThePublic, or Ubersuggest.)',
    'Is there existing competition? (None means no demand. Some means healthy market.)',
    'Can I rank as a new site? (Avoid niches dominated by Forbes, Mayo Clinic, NerdWallet.)',
    'Is there recurring demand? (Seasonal niches can work but need year-round content too.)',
    'Can I differentiate? (What angle can I bring that others don\'t?)',
    'Does this niche have growth potential? (Is the market growing or shrinking?)',
    'Can I start with under $100? (Domain + hosting. That\'s it.)'
]
for q in questions:
    pdf.bullet(q)

pdf.body_text(
    'How to score: Give yourself 1 point for each "yes." 10+ = launch immediately. '
    '7-9 = proceed with caution. Below 7 = find another niche.'
)

# ─── SECTION 2: Content Engine ───
pdf.section_title(2, 'Content Engine Blueprint')
pdf.body_text(
    'This is the system I built for Tech & SaaS Stack. It publishes on a schedule, '
    'targets long-tail keywords, and never misses a post. The secret is not working harder -- '
    'it\'s automating the repetitive parts so you can focus on strategy and quality.'
)
pdf.sub_heading('The Stack')
pdf.bullet('Static site generator: Jekyll (free, GitHub Pages hosting = $0)')
pdf.bullet('Content scheduling: Cron jobs (built into Linux/GitHub Actions)')
pdf.bullet('Research: Google Search, AnswerThePublic, Reddit, competitor blogs')
pdf.bullet('Images: Canva or AI-generated (free tier)')
pdf.bullet('Tracking: Google Search Console + Google Analytics (free)')

pdf.sub_heading('Weekly Content Workflow')
pdf.bullet('Day 1: Keyword research -- find 5 long-tail keywords with low competition')
pdf.bullet('Day 2: Outline -- structure the post, headings, key points')
pdf.bullet('Day 3: Write -- first draft (800-1500 words)')
pdf.bullet('Day 4: Edit -- tighten, add links, format for readability')
pdf.bullet('Day 5: Publish + promote -- share on social, add to site')

pdf.sub_heading('Cron Publishing Setup')
pdf.body_text(
    'Set up a cron job on your server (or GitHub Actions) to run your publishing script on a schedule. '
    'Example cron: "0 8 * * 1,3,5" = publish at 8 AM every Monday, Wednesday, Friday. '
    'The script checks your drafts folder, picks the next ready post, and publishes it. '
    'This is exactly how Tech & SaaS Stack runs on autopilot.'
)

# ─── SECTION 3: SEO Template ───
pdf.section_title(3, 'SEO Article Template')
pdf.body_text(
    'Every article I publish follows this structure. It\'s designed to satisfy both search engines '
    'and human readers -- because you need both to rank.'
)

pdf.sub_heading('The Structure')
pdf.bullet('H1: Keyword-rich title (e.g., "Best Hosting for WordPress in 2026")')
pdf.bullet('Intro: 2-3 sentences. State the problem, promise the solution.')
pdf.bullet('H2: What is [topic]? (Brief definition/context)')
pdf.bullet('H2: Why [topic] matters (Establish importance)')
pdf.bullet('H2: Top [N] [topic] options (Main content. Compare 5-8 options.)')
pdf.bullet('H2: How to choose (Buyer\'s guide / decision framework)')
pdf.bullet('H2: Frequently Asked Questions (FAQ, 3-5 questions)')
pdf.bullet('Conclusion: Recap + CTA with affiliate link')

pdf.sub_heading('On-Page SEO Checklist')
pdf.bullet('Primary keyword in H1, first 100 words, and one H2')
pdf.bullet('Meta description: 150-160 chars with keyword')
pdf.bullet('URL slug: short, keyword-focused (e.g., /best-wordpress-hosting/)')
pdf.bullet('Alt text on all images (describe the image, include keyword naturally)')
pdf.bullet('Internal links to 2-3 other posts on your site')
pdf.bullet('External links to 1-2 authority sources')
pdf.bullet('Readability: short paragraphs, bullet points, subheadings every 200-300 words')

# ─── SECTION 4: Affiliate Programs ───
pdf.section_title(4, 'Affiliate Program Comparison')
pdf.body_text(
    'Not all affiliate programs are created equal. Here are the programs I\'ve tested and ranked '
    'based on commission rate, conversion rate, cookie duration, and ease of approval.'
)

programs = [
    ('Amazon Associates', '1-10% sliding scale', 'High (trusted brand)', '24 hours', 'Very easy'),
    ('ShareASale', '5-30% flat', 'Medium', '30-60 days', 'Easy'),
    ('Impact / Impact Radius', '5-35%', 'Medium-High', '30-90 days', 'Moderate'),
    ('PartnerStack', '10-40% (SaaS)', 'Medium', '30-90 days', 'Moderate'),
    ('CJ Affiliate', '3-25%', 'Medium', '30-60 days', 'Moderate'),
    ('Rakuten Advertising', '3-20%', 'Medium', '30 days', 'Moderate'),
    ('Awin', '5-30%', 'Medium', '30-60 days', 'Easy'),
    ('Direct (in-house)', '10-50%', 'Varies', '30-90 days', 'Varies'),
]
pdf.set_font('Arial', 'B', 9)
pdf.set_fill_color(240, 240, 240)
pdf.cell(40, 7, 'Program', 1, 0, 'C', True)
pdf.cell(30, 7, 'Commission', 1, 0, 'C', True)
pdf.cell(30, 7, 'Conversion', 1, 0, 'C', True)
pdf.cell(25, 7, 'Cookie', 1, 0, 'C', True)
pdf.cell(55, 7, 'Approval', 1, 1, 'C', True)

pdf.set_font('Arial', '', 8)
for p in programs:
    pdf.cell(40, 6, p[0], 1)
    pdf.cell(30, 6, p[1], 1)
    pdf.cell(30, 6, p[2], 1)
    pdf.cell(25, 6, p[3], 1)
    pdf.cell(55, 6, p[4], 1)
    pdf.ln()

pdf.ln(4)
pdf.body_text(
    'My recommendation: Start with ShareASale or Amazon Associates (easiest approval). '
    'As your traffic grows, add Impact and direct programs for higher commissions. '
    'Always prioritize programs with 30+ day cookie durations -- they give you more '
    'time to earn the commission even if the customer doesn\'t buy immediately.'
)

# ─── SECTION 5: CTA Placement ───
pdf.section_title(5, 'CTA Placement Guide')
pdf.body_text(
    'Where you put your affiliate links matters more than what you\'re promoting. '
    'These placements consistently convert best.'
)
pdf.sub_heading('High-Converting Positions')
pdf.bullet('Within the first third of the article (above the fold if possible)')
pdf.bullet('In comparison tables (users comparing = ready to buy)')
pdf.bullet('In "best for" recommendations ("Best for beginners: [link]")')
pdf.bullet('In the conclusion -- natural call to action after providing value')
pdf.bullet('In roundup posts ("Top 5" "Best 7") -- highest converting format')
pdf.bullet('In "how to" guides -- link to tools/services mentioned')
pdf.bullet('In FAQ answers ("Where can I get X?" > link)')

pdf.sub_heading('What to Avoid')
pdf.bullet('Too many links in one article (3-5 max, spaced naturally)')
pdf.bullet('Links in the first sentence (looks spammy)')
pdf.bullet('No-context links ("click here" without explanation)')
pdf.bullet('Competing links on the same page (one affiliate offer per query intent)')

# ─── SECTION 6: Disclosure ───
pdf.section_title(6, 'Disclosure Compliance')
pdf.body_text(
    'FTC requires affiliate disclosures. These templates are compliant and honest. '
    'Place them before any affiliate link or at the top of the page.'
)
pdf.sub_heading('Templates')
pdf.set_font('Arial', 'I', 10)
pdf.set_text_color(80, 80, 80)
pdf.body_text(
    '"Some links on this page are affiliate links. If you purchase through them, '
    'I may earn a commission at no extra cost to you. I only recommend products I\'ve '
    'personally tested and believe in."'
)
pdf.ln(2)
pdf.body_text(
    '"This post contains affiliate links. As an Amazon Associate, I earn from '
    'qualifying purchases. Read my full disclosure here."'
)
pdf.set_font('Arial', '', 10)
pdf.set_text_color(50, 50, 50)
pdf.ln(2)
pdf.body_text(
    'Best practice: Add a disclosure banner to your site footer (like Tech & SaaS Stack does) '
    'AND a short notice at the top of any post with affiliate links. Over-disclose. '
    'It builds trust with readers and keeps the FTC happy.'
)

# ─── SECTION 7: Traffic Milestones ───
pdf.section_title(7, 'Traffic Milestone Roadmap')
pdf.body_text(
    'Here\'s what you can realistically expect at each traffic level. These are estimates '
    'based on my experience and industry benchmarks. Your results will vary based on niche, '
    'content quality, and SEO execution.'
)

milestones = [
    ('100 visitors/month', '0-2 weeks', 
     'Celebrate! This is the hardest milestone. You\'re in Google\'s index. '
     'Focus: publish 10-15 articles, set up Google Search Console.'),
    ('1,000 visitors/month', '1-3 months',
     'Your first real traffic. Some articles are ranking on page 2-3. '
     'Focus: keep publishing 3x/week. Update underperforming posts. '
     'Income: $0-$20/month from affiliate clicks.'),
    ('10,000 visitors/month', '3-6 months',
     'You have 3-5 articles ranking on page 1. Traffic starts compounding. '
     'Focus: build backlinks, write pillar content, start email list. '
     'Income: $100-$500/month.'),
    ('50,000 visitors/month', '6-12 months',
     'You have 15+ articles driving consistent traffic. Site authority is growing. '
     'Focus: scale content production, negotiate higher commissions, launch digital product. '
     'Income: $500-$3,000/month.'),
]

for title, timeline, desc in milestones:
    pdf.sub_heading(f'{title}  ({timeline})')
    pdf.body_text(desc)

# ─── SECTION 8: Revenue Calculator ───
pdf.section_title(8, 'Revenue Projection Calculator')
pdf.body_text(
    'Use this formula to estimate your monthly affiliate income:'
)
pdf.ln(2)
pdf.set_font('Courier', '', 11)
pdf.set_text_color(40, 40, 40)
pdf.cell(0, 6, 'Monthly Revenue = Traffic x CTR x Conversion Rate x AOV x Commission', 0, 1)
pdf.ln(4)
pdf.set_font('Arial', '', 10)
pdf.set_text_color(50, 50, 50)

pdf.sub_heading('Example Calculation')
pdf.body_text(
    'Traffic: 10,000 visitors/month' + chr(10) +
    'Click-through rate (CTR) on affiliate links: 3%' + chr(10) +
    'Total clicks: 300' + chr(10) +
    'Conversion rate (clicks to purchase): 2%' + chr(10) +
    'Total purchases: 6' + chr(10) +
    'Average order value: $50' + chr(10) +
    'Commission rate: 10%' + chr(10) +
    'Revenue: 6 x $50 x 10% = $30/month'
)
pdf.body_text(
    'Double any variable and your revenue doubles. Double traffic to 20k? $60/month. '
    'Improve CTR to 5%? $50/month. Increase AOV to $75? $45/month. '
    'The leverage is in improving multiple variables at once.'
)

pdf.sub_heading('Revenue Targets at Scale')
pdf.body_text(
    '50k visitors, 4% CTR, 2.5% conversion, $60 AOV, 15% commission = $450/month' + chr(10) +
    '100k visitors, 5% CTR, 3% conversion, $70 AOV, 15% commission = $1,575/month' + chr(10) +
    '200k visitors, 6% CTR, 3.5% conversion, $80 AOV, 20% commission = $6,720/month'
)

# ─── CLOSING PAGE ───
pdf.add_page()
pdf.ln(50)
pdf.set_font('Arial', 'B', 24)
pdf.set_text_color(30, 30, 30)
pdf.cell(0, 15, 'Ready to Get Started?', 0, 1, 'C')
pdf.ln(8)
pdf.set_font('Arial', '', 12)
pdf.set_text_color(100, 100, 100)
pdf.cell(0, 7, '1. Pick your niche using Section 1', 0, 1, 'C')
pdf.cell(0, 7, '2. Set up your site with the content engine (Section 2)', 0, 1, 'C')
pdf.cell(0, 7, '3. Write your first post using the SEO template (Section 3)', 0, 1, 'C')
pdf.cell(0, 7, '4. Apply to 2-3 affiliate programs (Section 4)', 0, 1, 'C')
pdf.cell(0, 7, '5. Publish 10 articles and track your traffic', 0, 1, 'C')
pdf.cell(0, 7, '6. Scale what works', 0, 1, 'C')
pdf.ln(20)
pdf.set_draw_color(200, 200, 200)
pdf.line(60, pdf.get_y(), 150, pdf.get_y())
pdf.ln(15)
pdf.set_font('Arial', 'I', 10)
pdf.set_text_color(140, 140, 140)
pdf.cell(0, 6, 'Thank you for purchasing the Affiliate Marketing Starter Kit.', 0, 1, 'C')
pdf.cell(0, 6, 'Questions? Email: jon@techsaasstack.com', 0, 1, 'C')
pdf.ln(8)
pdf.set_font('Arial', '', 9)
pdf.set_text_color(160, 160, 160)
pdf.cell(0, 5, 'Tech & SaaS Stack  |  techsaasstack.com  |  2026', 0, 1, 'C')

# ─── SAVE ───
out_dir = "C:/Users/1990j/blog/products"
out_path = os.path.join(out_dir, "Affiliate_Marketing_Starter_Kit_2026.pdf")
pdf.output(out_path)
print(f"PDF saved to: {out_path}")
print(f"Pages: {pdf.page_no()}")
file_size = os.path.getsize(out_path)
print(f"Size: {file_size / 1024:.1f} KB")

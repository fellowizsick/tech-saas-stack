from fpdf import FPDF
import os

pdf = FPDF()
pdf.add_page()
pdf.set_auto_page_break(auto=True, margin=20)

# Title
pdf.set_font('Helvetica', 'B', 24)
pdf.cell(0, 12, 'Best Hosting Cheat Sheet', ln=True, align='C')
pdf.set_font('Helvetica', '', 12)
pdf.cell(0, 8, 'By Tech & SaaS Stack -- Independent hosting reviews since 2025', ln=True, align='C')
pdf.ln(5)

# Quick Decision Framework
pdf.set_font('Helvetica', 'B', 16)
pdf.cell(0, 10, 'Quick Decision Framework', ln=True)
pdf.ln(2)

pdf.set_font('Helvetica', '', 9)
col_w = [60, 40, 90]
headers = ['If You Need...', 'Best Choice', 'Why']
rows = [
    ['Budget shared hosting', 'SiteGround', 'WP.org recommended, free SSL/backups, great support'],
    ['Price lock guarantee', 'InterServer', '$2.50/mo forever, unlimited NVMe/bandwidth'],
    ['Pay-as-you-go cloud', 'Cloudways', 'Hourly billing, DO/Vultr/Linode/AWS/GCP, free migrations'],
    ['Managed VPS + custom panel', 'ScalaHosting', 'SPanel (cPanel alt), SShield security, NVMe'],
    ['Premium managed WP', 'Kinsta', 'Google Cloud C2, 260+ PoPs, auto-scaling, free migrations'],
]

pdf.set_font('Helvetica', 'B', 9)
for i, h in enumerate(headers):
    pdf.cell(col_w[i], 8, h, border=1, align='C')
pdf.ln()

pdf.set_font('Helvetica', '', 8)
for row in rows:
    for i, cell in enumerate(row):
        pdf.cell(col_w[i], 8, cell, border=1)
    pdf.ln()

pdf.ln(5)

# Hosting Comparison
pdf.set_font('Helvetica', 'B', 16)
pdf.cell(0, 10, 'Hosting Comparison at a Glance', ln=True)
pdf.ln(2)

col_w2 = [30, 25, 30, 50, 50]
headers2 = ['Provider', 'Type', 'Price', 'Key Feature', 'Best For']
rows2 = [
    ['SiteGround', 'Shared', '$2.99/mo', 'WP.org recommended', 'Beginners, small sites'],
    ['InterServer', 'Shared/VPS', '$2.50/mo', 'Price lock forever', 'Long-term savings'],
    ['Cloudways', 'Cloud/VPS', '$11/mo', 'Hourly billing, any cloud', 'Developers, agencies'],
    ['ScalaHosting', 'Managed VPS', '$29.95/mo', 'SPanel + SShield', 'Privacy, control'],
    ['Kinsta', 'Managed WP', '$35/mo', 'Google Cloud C2, 35k visits', 'High-traffic, ecommerce'],
]

pdf.set_font('Helvetica', 'B', 8)
for i, h in enumerate(headers2):
    pdf.cell(col_w2[i], 8, h, border=1, align='C')
pdf.ln()

pdf.set_font('Helvetica', '', 7.5)
for row in rows2:
    for i, cell in enumerate(row):
        pdf.cell(col_w2[i], 7, cell, border=1)
    pdf.ln()

pdf.ln(5)

# Red Flags
pdf.set_font('Helvetica', 'B', 16)
pdf.cell(0, 10, 'Red Flags to Avoid', ln=True)
pdf.ln(2)

pdf.set_font('Helvetica', '', 9)
flags = [
    'Unlimited everything (usually means throttled)',
    'No free SSL (Let\'s Encrypt is free)',
    'No staging environment (critical for safe updates)',
    'Forced annual contracts (no monthly option)',
    'Hidden renewal pricing (intro vs. renewal gap > 50%)',
    'No free migrations (you\'ll pay $100-300)',
    'EIG-owned brands (Bluehost, HostGator, iPage -- often overloaded)',
]
for f in flags:
    pdf.cell(5, 5, '')
    pdf.cell(0, 6, f, ln=True)

pdf.ln(3)

# Essentials
pdf.set_font('Helvetica', 'B', 16)
pdf.cell(0, 10, 'Essential Features Checklist', ln=True)
pdf.ln(2)

pdf.set_font('Helvetica', '', 9)
ess = [
    ('Free SSL (Let\'s Encrypt)', 'Yes', 'Auto-renew'),
    ('Daily automated backups', 'Yes', '14-30 day retention'),
    ('Staging environment', 'Yes', 'One-click push to live'),
    ('Free site migrations', 'Yes', 'Saves $100-300'),
    ('24/7 expert support', 'Yes', 'Chat preferred'),
    ('CDN included', 'Yes', 'Cloudflare or similar'),
    ('Malware scanning', 'Yes', 'Automated'),
    ('PHP 8.2+ support', 'Yes', 'Performance + security'),
    ('WP-CLI / SSH access', 'For devs', 'Essential for workflow'),
]

col_w3 = [55, 20, 115]
pdf.set_font('Helvetica', 'B', 8)
pdf.cell(col_w3[0], 8, 'Feature', border=1)
pdf.cell(col_w3[1], 8, 'Must Have?', border=1)
pdf.cell(col_w3[2], 8, 'Notes', border=1)
pdf.ln()

pdf.set_font('Helvetica', '', 8)
for f, m, n in ess:
    pdf.cell(col_w3[0], 7, f, border=1)
    pdf.cell(col_w3[1], 7, m, border=1, align='C')
    pdf.cell(col_w3[2], 7, n, border=1)
    pdf.ln()

pdf.ln(3)

# Questions
pdf.set_font('Helvetica', 'B', 16)
pdf.cell(0, 10, 'Quick Questions to Ask Before Buying', ln=True)
pdf.ln(2)

pdf.set_font('Helvetica', '', 9)
qs = [
    'What\'s the REAL renewal price? (Not intro price)',
    'Is staging included on ALL plans?',
    'How many CPU cores / RAM guaranteed? (Not "shared")',
    'What\'s the backup retention period?',
    'Can I pay monthly?',
    'Do you own your data centers or resell?',
    'What\'s your uptime SLA? (99.9% minimum)',
    'Free migrations -- any limits?',
]
for i, q in enumerate(qs, 1):
    pdf.cell(0, 6, f'{i}. {q}', ln=True)

pdf.ln(3)

# Top 3
pdf.set_font('Helvetica', 'B', 16)
pdf.cell(0, 10, 'My Top 3 Recommendations', ln=True)
pdf.ln(2)

recs = [
    ('SiteGround -- Best Overall Value', [
        'WP.org officially recommended',
        'Free SSL, daily backups, SuperCacher, staging',
        '$2.99/mo intro, ~$14.99/mo renewal',
        'Best for: Beginners, small business, blogs',
    ]),
    ('InterServer -- Best Price Lock', [
        '$2.50/mo FOREVER (shared), VPS from $6/mo',
        'Unlimited NVMe SSD, bandwidth, email',
        '30-day money-back, price lock guarantee',
        'Best for: Long-term projects, budget-conscious',
    ]),
    ('Cloudways -- Best for Developers/Agencies', [
        'Hourly billing on DO/Vultr/Linode/AWS/GCP',
        'Free migrations, staging, Cloudflare CDN, SSL',
        '$11/mo (1GB RAM), pay only for what you use',
        'Best for: Agencies, high-traffic, multi-site',
    ]),
]

pdf.set_font('Helvetica', '', 9)
for title, items in recs:
    pdf.set_font('Helvetica', 'B', 11)
    pdf.cell(0, 8, title, ln=True)
    pdf.set_font('Helvetica', '', 9)
    for item in items:
        pdf.cell(5, 5, '')
        pdf.cell(0, 5, f'- {item}', ln=True)
    pdf.ln(2)

pdf.ln(3)

# Quick Links
pdf.set_font('Helvetica', 'B', 16)
pdf.cell(0, 10, 'Quick Links', ln=True)
pdf.ln(2)

pdf.set_font('Helvetica', '', 9)
links = [
    ('Full Hosting Reviews', 'https://techsaasstack.com'),
    ('Best Deals Page', 'https://techsaasstack.com/best-deals/'),
    ('How We Test', 'https://techsaasstack.com/how-we-test/'),
    ('Privacy Policy', 'https://techsaasstack.com/privacy/'),
    ('Contact', 'jon.techsaasstack@gmail.com'),
]
for label, url in links:
    pdf.cell(0, 6, f'{label}: {url}', ln=True)

pdf.ln(5)

# Footer
pdf.set_font('Helvetica', 'I', 8)
pdf.cell(0, 5, 'Last updated: June 2025', ln=True)
pdf.cell(0, 5, 'This cheat sheet is free. If you found it useful, consider using our affiliate links when you buy -- it supports independent reviews at no cost to you.', ln=True)

output_path = 'C:/Users/1990j/tech-saas-stack/assets/hosting-cheat-sheet.pdf'
pdf.output(output_path)
print(f'PDF generated: {os.path.getsize(output_path)} bytes')
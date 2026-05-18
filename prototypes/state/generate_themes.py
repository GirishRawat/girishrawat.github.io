import json
import random
import re

themes_data = [
    {
        "id": "healthcare-wait-times",
        "title": "Healthcare Wait Times",
        "subtitle": "Significant increase in complaints regarding GP appointment availability.",
        "icon": "https://picsum.photos/seed/healthcare/100/100",
        "minister_name": "Wes Streeting",
        "minister_role": "Health Secretary",
        "minister_avatar": "https://randomuser.me/api/portraits/men/32.jpg",
        "trend": "+12%",
        "trend_class": "trend-positive",
        "total_talking": "12,450",
        "total_joining": "342",
        "tags": ["GP Access", "NHS Waitlists", "Urgent Care"],
        "motions": [
            {"title": "Guarantee GP appointments within 48 hours for urgent cases", "comments": "124", "votes": "890"},
            {"title": "Increase funding for out-of-hours pharmacy services", "comments": "45", "votes": "312"},
            {"title": "Review the NHS 111 triage system in London", "comments": "89", "votes": "560"}
        ]
    },
    {
        "id": "business-rates",
        "title": "High Street Business Rates",
        "subtitle": "Local shop owners petitioning for rate reductions to prevent closures.",
        "icon": "https://picsum.photos/seed/businessrates/100/100",
        "minister_name": "Jonathan Reynolds",
        "minister_role": "Business Secretary",
        "minister_avatar": "https://randomuser.me/api/portraits/men/44.jpg",
        "trend": "+8%",
        "trend_class": "trend-positive",
        "total_talking": "8,320",
        "total_joining": "156",
        "tags": ["Retail", "Local Economy", "Taxation"],
        "motions": [
            {"title": "Implement an immediate freeze on high street business rates", "comments": "88", "votes": "430"},
            {"title": "Introduce an online sales tax to level the playing field", "comments": "150", "votes": "920"},
            {"title": "Provide emergency grants for independent retailers", "comments": "34", "votes": "210"}
        ]
    },
    {
        "id": "transport",
        "title": "Local Transport Delays",
        "subtitle": "Bus routes facing frequent cancellations impacting daily commuters.",
        "icon": "https://picsum.photos/seed/transport/100/100",
        "minister_name": "Louise Haigh",
        "minister_role": "Transport Secretary",
        "minister_avatar": "https://randomuser.me/api/portraits/women/68.jpg",
        "trend": "-3%",
        "trend_class": "trend-negative",
        "total_talking": "5,912",
        "total_joining": "89",
        "tags": ["Bus Routes", "Commuting", "Infrastructure"],
        "motions": [
            {"title": "Restore cancelled bus services on the central transit routes", "comments": "210", "votes": "1150"},
            {"title": "Implement real-time tracking at all major bus stops", "comments": "65", "votes": "420"},
            {"title": "Review penalty fines for delayed operator services", "comments": "42", "votes": "280"}
        ]
    },
    {
        "id": "arts",
        "title": "Arts, Media and Sport",
        "subtitle": "Public voices on local venues, sports funding and media access",
        "icon": "https://picsum.photos/seed/arts/100/100",
        "minister_name": "Lisa Nandy",
        "minister_role": "Culture Secretary",
        "minister_avatar": "https://randomuser.me/api/portraits/women/44.jpg",
        "trend": "+6%",
        "trend_class": "trend-positive",
        "total_talking": "92,219",
        "total_joining": "7",
        "tags": ["Media Technology", "Employment", "Animal Licensing"],
        "motions": [
            {"title": "Do not ban social media for under 16s", "comments": "8", "votes": "77"},
            {"title": "Stop social media posts being shown with dogs that have cropped ears", "comments": "1", "votes": "4"},
            {"title": "Recognise circus and fairgrounds in the UK inventory of ICH", "comments": "1", "votes": "4"}
        ]
    },
    {
        "id": "benefits",
        "title": "Benefits and Jobs",
        "subtitle": "What people are saying about work, welfare and living costs",
        "icon": "https://picsum.photos/seed/benefits/100/100",
        "minister_name": "Liz Kendall",
        "minister_role": "Work and Pensions Secretary",
        "minister_avatar": "https://randomuser.me/api/portraits/women/33.jpg",
        "trend": "+15%",
        "trend_class": "trend-positive",
        "total_talking": "163,190",
        "total_joining": "1,205",
        "tags": ["Universal Credit", "Living Wage", "Childcare"],
        "motions": [
            {"title": "Abolish the two-child benefit cap immediately", "comments": "340", "votes": "2100"},
            {"title": "Increase the minimum wage to match the real living wage", "comments": "512", "votes": "4500"},
            {"title": "Reform PIP assessments to use medical evidence rather than interviews", "comments": "289", "votes": "1850"}
        ]
    },
    {
        "id": "business",
        "title": "Business and Trade",
        "subtitle": "Community views on high streets, local business and fair trade",
        "icon": "https://picsum.photos/seed/business/100/100",
        "minister_name": "Jonathan Reynolds",
        "minister_role": "Business and Trade Secretary",
        "minister_avatar": "https://randomuser.me/api/portraits/men/44.jpg",
        "trend": "+2%",
        "trend_class": "trend-positive",
        "total_talking": "68,522",
        "total_joining": "412",
        "tags": ["Exports", "Small Business", "Supply Chains"],
        "motions": [
            {"title": "Simplify customs paperwork for small exporters to the EU", "comments": "145", "votes": "890"},
            {"title": "Ban the import of goods produced using forced labor", "comments": "310", "votes": "2300"},
            {"title": "Create a national strategy to protect independent manufacturing", "comments": "88", "votes": "540"}
        ]
    },
    {
        "id": "courts",
        "title": "Courts and Prisons",
        "subtitle": "Public calls for justice reform, safer streets and sentencing change",
        "icon": "https://picsum.photos/seed/courts/100/100",
        "minister_name": "Shabana Mahmood",
        "minister_role": "Justice Secretary",
        "minister_avatar": "https://randomuser.me/api/portraits/women/22.jpg",
        "trend": "+9%",
        "trend_class": "trend-positive",
        "total_talking": "383,931",
        "total_joining": "2,150",
        "tags": ["Sentencing", "Prison Reform", "Victim Support"],
        "motions": [
            {"title": "Increase sentences for repeat violent offenders", "comments": "670", "votes": "5100"},
            {"title": "Fund community rehabilitation programs to reduce reoffending", "comments": "210", "votes": "1400"},
            {"title": "Clear the crown court backlog within 24 months", "comments": "180", "votes": "950"}
        ]
    },
    {
        "id": "education",
        "title": "Education",
        "subtitle": "What parents and communities want from schools and education policy",
        "icon": "https://picsum.photos/seed/education/100/100",
        "minister_name": "Bridget Phillipson",
        "minister_role": "Education Secretary",
        "minister_avatar": "https://randomuser.me/api/portraits/women/55.jpg",
        "trend": "+18%",
        "trend_class": "trend-positive",
        "total_talking": "238,908",
        "total_joining": "1,890",
        "tags": ["SEND Provision", "School Meals", "Curriculum"],
        "motions": [
            {"title": "Provide free school meals for all primary school children", "comments": "890", "votes": "8200"},
            {"title": "Urgently increase funding for Special Educational Needs (SEND)", "comments": "1200", "votes": "10500"},
            {"title": "Remove VAT exemption for private schools", "comments": "1500", "votes": "12000"}
        ]
    },
    {
        "id": "energy",
        "title": "Energy",
        "subtitle": "Residents speaking out on energy bills, blackouts and green energy",
        "icon": "https://picsum.photos/seed/energy/100/100",
        "minister_name": "Ed Miliband",
        "minister_role": "Energy Secretary",
        "minister_avatar": "https://randomuser.me/api/portraits/men/55.jpg",
        "trend": "+4%",
        "trend_class": "trend-positive",
        "total_talking": "7,711",
        "total_joining": "54",
        "tags": ["Renewables", "Energy Bills", "Grid Capacity"],
        "motions": [
            {"title": "Ban new oil and gas licenses in the North Sea", "comments": "340", "votes": "2800"},
            {"title": "Introduce a social tariff for energy bills", "comments": "410", "votes": "3100"},
            {"title": "Fast-track planning for onshore wind farms", "comments": "190", "votes": "1200"}
        ]
    },
    {
        "id": "environment",
        "title": "Environment and Food",
        "subtitle": "Citizens raising concerns on pollution, food quality and climate",
        "icon": "https://picsum.photos/seed/environment/100/100",
        "minister_name": "Steve Reed",
        "minister_role": "Environment Secretary",
        "minister_avatar": "https://randomuser.me/api/portraits/men/66.jpg",
        "trend": "+22%",
        "trend_class": "trend-positive",
        "total_talking": "534,689",
        "total_joining": "3,400",
        "tags": ["Water Quality", "Farming", "Net Zero"],
        "motions": [
            {"title": "Hold water company executives criminally liable for sewage spills", "comments": "2100", "votes": "18000"},
            {"title": "Ban the use of neonicotinoid pesticides permanently", "comments": "850", "votes": "6400"},
            {"title": "Ensure post-Brexit farming subsidies prioritize nature recovery", "comments": "320", "votes": "2100"}
        ]
    },
    {
        "id": "government",
        "title": "Government Finances",
        "subtitle": "Taxpayer voices on public spending, budgets and accountability",
        "icon": "https://picsum.photos/seed/government/100/100",
        "minister_name": "Rachel Reeves",
        "minister_role": "Chancellor of the Exchequer",
        "minister_avatar": "https://randomuser.me/api/portraits/women/66.jpg",
        "trend": "+11%",
        "trend_class": "trend-positive",
        "total_talking": "172,644",
        "total_joining": "980",
        "tags": ["Taxation", "Public Spending", "National Debt"],
        "motions": [
            {"title": "Equalize capital gains tax with income tax rates", "comments": "560", "votes": "4200"},
            {"title": "Commit to the triple lock on state pensions", "comments": "1200", "votes": "8900"},
            {"title": "Increase the windfall tax on energy companies", "comments": "890", "votes": "7100"}
        ]
    },
    {
        "id": "healthcare",
        "title": "Health Care",
        "subtitle": "What the public demands from the NHS, GPs and mental health services",
        "icon": "https://picsum.photos/seed/healthcare/100/100",
        "minister_name": "Wes Streeting",
        "minister_role": "Health Secretary",
        "minister_avatar": "https://randomuser.me/api/portraits/men/32.jpg",
        "trend": "+25%",
        "trend_class": "trend-positive",
        "total_talking": "1,085,677",
        "total_joining": "8,900",
        "tags": ["NHS Dentistry", "Mental Health", "Staff Pay"],
        "motions": [
            {"title": "Deliver a fair pay settlement for junior doctors and nurses", "comments": "3100", "votes": "24000"},
            {"title": "Reform the NHS dental contract to stop the exodus of dentists", "comments": "1800", "votes": "15000"},
            {"title": "Guarantee mental health treatment within 4 weeks", "comments": "1400", "votes": "11000"}
        ]
    },
    {
        "id": "housing",
        "title": "Housing and Communities",
        "subtitle": "Residents pushing for affordable homes and better planning",
        "icon": "https://picsum.photos/seed/housing/100/100",
        "minister_name": "Angela Rayner",
        "minister_role": "Housing Secretary",
        "minister_avatar": "https://randomuser.me/api/portraits/women/77.jpg",
        "trend": "+14%",
        "trend_class": "trend-positive",
        "total_talking": "197,612",
        "total_joining": "1,150",
        "tags": ["Rent Controls", "Social Housing", "Planning"],
        "motions": [
            {"title": "Abolish Section 21 'no-fault' evictions immediately", "comments": "1500", "votes": "12000"},
            {"title": "Build 100,000 new social homes per year", "comments": "890", "votes": "7500"},
            {"title": "Introduce rent caps in high-demand urban areas", "comments": "1100", "votes": "9200"}
        ]
    },
    {
        "id": "immigration",
        "title": "Immigration and Policing",
        "subtitle": "Community perspectives on safety, borders and local policing",
        "icon": "https://picsum.photos/seed/immigration/100/100",
        "minister_name": "Yvette Cooper",
        "minister_role": "Home Secretary",
        "minister_avatar": "https://randomuser.me/api/portraits/women/88.jpg",
        "trend": "+19%",
        "trend_class": "trend-positive",
        "total_talking": "1,398,999",
        "total_joining": "11,200",
        "tags": ["Asylum", "Neighborhood Policing", "Border Control"],
        "motions": [
            {"title": "Clear the asylum backlog and process claims within 6 months", "comments": "2100", "votes": "16000"},
            {"title": "Return 13,000 neighborhood police officers to the streets", "comments": "1500", "votes": "12500"},
            {"title": "Scrap the Rwanda deportation scheme", "comments": "2800", "votes": "21000"}
        ]
    },
    {
        "id": "international",
        "title": "International Affairs",
        "subtitle": "Public opinion on foreign policy, defence and global issues",
        "icon": "https://picsum.photos/seed/international/100/100",
        "minister_name": "David Lammy",
        "minister_role": "Foreign Secretary",
        "minister_avatar": "https://randomuser.me/api/portraits/men/88.jpg",
        "trend": "-2%",
        "trend_class": "trend-negative",
        "total_talking": "211,524",
        "total_joining": "890",
        "tags": ["Gaza", "Ukraine", "Foreign Aid"],
        "motions": [
            {"title": "Call for an immediate ceasefire in Gaza", "comments": "4500", "votes": "35000"},
            {"title": "Maintain military and humanitarian support for Ukraine", "comments": "1200", "votes": "9500"},
            {"title": "Restore the international aid budget to 0.7% of GNI", "comments": "890", "votes": "6200"}
        ]
    }
]

def generate_bar_chart():
    bars = []
    for _ in range(20):
        height = random.randint(30, 100)
        bars.append(f'<div class="bar" style="height: {height}%"></div>')
    return '\n'.join(bars)

# Read the template
with open('theme-details.html', 'r') as f:
    template = f.read()

for theme in themes_data:
    content = template
    
    # Simple replacements
    content = re.sub(r'<h1>.*?</h1>', f'<h1>{theme["title"]}</h1>', content)
    content = re.sub(r'<p>Public voices on local venues, sports funding and media access</p>', f'<p>{theme["subtitle"]}</p>', content)
    content = re.sub(r'<img src="https://picsum.photos/seed/arts/100/100" alt="Arts" class="theme-large-icon">', f'<img src="{theme["icon"]}" alt="{theme["title"]}" class="theme-large-icon">', content)
    
    # Stats large
    content = re.sub(r'<span class="trending-up">.*?</span>', f'<span class="trending-up"><svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polyline points="23 6 13.5 15.5 8.5 10.5 1 18"></polyline><polyline points="17 6 23 6 23 12"></polyline></svg>{theme["trend"]} Trending</span>', content, flags=re.DOTALL)
    
    # Minister card
    content = re.sub(r'<h3>Lisa Nandy</h3>', f'<h3>{theme["minister_name"]}</h3>', content)
    content = re.sub(r'<p>Culture Secretary</p>', f'<p>{theme["minister_role"]}</p>', content)
    content = re.sub(r'<img src="https://randomuser.me/api/portraits/women/44.jpg" alt="Lisa Nandy" class="minister-avatar">', f'<img src="{theme["minister_avatar"]}" alt="{theme["minister_name"]}" class="minister-avatar">', content)
    
    # Tags
    tags_html = '\n'.join([f'<button class="tag tag-outline-pink">{tag}</button>' for tag in theme['tags']])
    content = re.sub(r'<button class="tag tag-outline-pink">Media Technology</button>[\s\S]*?<button class="tag tag-outline-pink">Other Policy</button>', tags_html, content)
    
    # Insight sentence
    sentence_html = f'The top motions in Bethnal Green and Stepney are about <span class="tag-teal-inline">{theme["tags"][0]}</span>, <span class="tag-teal-inline">{theme["tags"][1]}</span> and <span class="tag-teal-inline">{theme["tags"][2]}</span>.'
    content = re.sub(r'The top motions in Bethnal Green and Stepney are about.*?\.', sentence_html, content, flags=re.DOTALL)
    
    # Metrics
    content = re.sub(r'<span class="metric-value">92</span>', f'<span class="metric-value">{theme["total_talking"]}</span>', content)
    content = re.sub(r'<span class="metric-value">7</span>', f'<span class="metric-value">{theme["total_joining"]}</span>', content)
    content = re.sub(r'<span class="metric-value trend-positive">\+6%</span>', f'<span class="metric-value {theme["trend_class"]}">{theme["trend"]}</span>', content)
    
    # Bar chart
    content = re.sub(r'<div class="mini-bar-chart">.*?</div>\n                </div>', f'<div class="mini-bar-chart">\n{generate_bar_chart()}\n</div>\n                </div>', content, flags=re.DOTALL)
    
    # Motions list
    motions_html = []
    for m in theme['motions']:
        m_html = f'''<div class="motion-card">
    <div class="motion-card-content">
        <h4>{m["title"]}</h4>
        <div class="motion-metadata">
            <span class="meta-tag"><svg width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M21 15a2 2 0 0 1-2 2H7l-4 4V5a2 2 0 0 1 2-2h14a2 2 0 0 1 2 2z"></path></svg> {m["comments"]}</span>
            <span class="meta-tag"><svg width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M14 9V5a3 3 0 0 0-3-3l-4 9v11h11.28a2 2 0 0 0 2-1.7l1.38-9a2 2 0 0 0-2-2.3zM7 22H4a2 2 0 0 1-2-2v-7a2 2 0 0 1 2-2h3"></path></svg> {m["votes"]}</span>
            <span class="meta-scope">National</span>
        </div>
    </div>
</div>'''
        motions_html.append(m_html)
    
    content = re.sub(r'<div class="motion-list">.*?</div>\n        </div>', f'<div class="motion-list">\n{"".join(motions_html)}\n</div>\n        </div>', content, flags=re.DOTALL)
    
    # FAB tooltip
    content = re.sub(r'See what people care about<br>in Arts, Media and Sport', f'See what people care about<br>in {theme["title"]}', content)
    
    # Write to file
    with open(f'theme-{theme["id"]}.html', 'w') as f:
        f.write(content)

# Now update themes.html to point to these new pages
with open('themes.html', 'r') as f:
    themes_content = f.read()

for theme in themes_data:
    # We replace the generic link with the specific link for this card.
    # The title inside themes.html matches theme["title"]
    # Regex to find <a href="theme-details.html"...> ... <h2>Title</h2> ... </a>
    # We will just split by '<a href="theme-details.html"' and check if the title is inside
    
    pattern = r'<a href="theme-details.html"([^>]*>[\s\S]*?<h2>' + re.escape(theme["title"]) + r'</h2>[\s\S]*?</a>)'
    replacement = r'<a href="theme-' + theme["id"] + r'.html"\1'
    themes_content = re.sub(pattern, replacement, themes_content)
    
    # For featured issues (h3 instead of h2)
    pattern_feat = r'<a href="theme-details.html"([^>]*>[\s\S]*?<h3>' + re.escape(theme["title"]) + r'</h3>[\s\S]*?</a>)'
    replacement_feat = r'<a href="theme-' + theme["id"] + r'.html"\1'
    themes_content = re.sub(pattern_feat, replacement_feat, themes_content)

with open('themes.html', 'w') as f:
    f.write(themes_content)

print("Generated 15 theme pages and updated themes.html")

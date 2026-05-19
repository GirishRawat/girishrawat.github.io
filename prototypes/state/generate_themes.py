import json
import random
import re

def slugify(text):
    return re.sub(r'[^a-z0-9]+', '-', text.lower()).strip('-')

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

# Additional motions per theme (merged with core motions for random page selection)
EXTRA_MOTIONS = {
    "healthcare-wait-times": [
        {"title": "Recruit 5,000 additional GPs nationally within two years", "comments": "312", "votes": "2400"},
        {"title": "Expand same-day appointment slots at walk-in clinics", "comments": "178", "votes": "1100"},
        {"title": "Fund mobile health units for underserved estates", "comments": "94", "votes": "680"},
        {"title": "Cap waiting lists for routine referrals at 12 weeks", "comments": "256", "votes": "1900"},
        {"title": "Mandate annual publication of GP access statistics by postcode", "comments": "67", "votes": "420"},
        {"title": "Train more physician associates to support GP surgeries", "comments": "143", "votes": "980"},
        {"title": "Integrate community pharmacists into chronic care plans", "comments": "88", "votes": "610"},
    ],
    "business-rates": [
        {"title": "Create a digital portal to challenge business rate valuations", "comments": "56", "votes": "340"},
        {"title": "Offer 12-month rate holidays for new high street startups", "comments": "102", "votes": "780"},
        {"title": "Reform transitional relief for expanding retailers", "comments": "41", "votes": "290"},
        {"title": "Require transparency on how rate income is spent locally", "comments": "73", "votes": "510"},
        {"title": "Exempt charities running community shops from business rates", "comments": "29", "votes": "180"},
        {"title": "Pilot a turnover-based rates system for micro-businesses", "comments": "118", "votes": "860"},
        {"title": "Fund high street regeneration grants in deprived wards", "comments": "165", "votes": "1200"},
    ],
    "transport": [
        {"title": "Introduce a flat £2 bus fare cap across London", "comments": "890", "votes": "7200"},
        {"title": "Install covered shelters at every major stop in the ward", "comments": "134", "votes": "890"},
        {"title": "Prioritise bus lanes on congested commuter corridors", "comments": "201", "votes": "1450"},
        {"title": "Require operators to publish cancellation reasons daily", "comments": "76", "votes": "520"},
        {"title": "Extend night bus services on weekends", "comments": "312", "votes": "2100"},
        {"title": "Subsidise travel passes for apprentices and students", "comments": "98", "votes": "670"},
        {"title": "Audit TfL contracts for value and service reliability", "comments": "145", "votes": "980"},
    ],
    "arts": [
        {"title": "Protect funding for local libraries and community theatres", "comments": "234", "votes": "1800"},
        {"title": "Require age verification on all major social platforms", "comments": "156", "votes": "1100"},
        {"title": "Invest in grassroots sports facilities in inner cities", "comments": "89", "votes": "640"},
        {"title": "Ban gambling advertising during live sports broadcasts", "comments": "412", "votes": "3200"},
        {"title": "Support freelance artists with national insurance relief", "comments": "67", "votes": "480"},
        {"title": "Mandate local content quotas on streaming services", "comments": "123", "votes": "890"},
        {"title": "Fund after-school music programmes in state schools", "comments": "178", "votes": "1300"},
    ],
    "benefits": [
        {"title": "Remove the bedroom tax without replacement penalties", "comments": "445", "votes": "3600"},
        {"title": "Index benefits annually to actual inflation plus housing costs", "comments": "678", "votes": "5200"},
        {"title": "Simplify Universal Credit applications to a single form", "comments": "234", "votes": "1700"},
        {"title": "Guarantee childcare support for single parents returning to work", "comments": "312", "votes": "2400"},
        {"title": "End sanctions for administrative errors by claimants", "comments": "189", "votes": "1400"},
        {"title": "Raise carer's allowance to match minimum wage", "comments": "521", "votes": "4100"},
        {"title": "Fund debt advice services at every Jobcentre Plus", "comments": "98", "votes": "720"},
    ],
    "business": [
        {"title": "Cut red tape for businesses hiring their first employee", "comments": "112", "votes": "780"},
        {"title": "Negotiate mutual recognition of standards with key EU markets", "comments": "198", "votes": "1400"},
        {"title": "Expand export vouchers for firms under 50 staff", "comments": "76", "votes": "540"},
        {"title": "Ban unpaid internships longer than four weeks", "comments": "334", "votes": "2600"},
        {"title": "Create a public register of supply chain audits", "comments": "145", "votes": "1020"},
        {"title": "Support co-operatives with preferential loan guarantees", "comments": "67", "votes": "490"},
        {"title": "Fund digital skills training for high street retailers", "comments": "89", "votes": "630"},
    ],
    "courts": [
        {"title": "Increase legal aid eligibility for domestic abuse cases", "comments": "456", "votes": "3800"},
        {"title": "Expand drug treatment courts as an alternative to custody", "comments": "178", "votes": "1200"},
        {"title": "Fund victim liaison officers in every crown court", "comments": "134", "votes": "950"},
        {"title": "Mandate sentencing guidelines review for knife crime", "comments": "289", "votes": "2200"},
        {"title": "Improve prison education and vocational training", "comments": "98", "votes": "710"},
        {"title": "Reduce remand times for unconvicted defendants", "comments": "167", "votes": "1180"},
        {"title": "Publish quarterly data on court waiting times by region", "comments": "76", "votes": "540"},
    ],
    "education": [
        {"title": "Cap primary class sizes at 30 pupils nationally", "comments": "567", "votes": "4500"},
        {"title": "Fund breakfast clubs in all schools in deprived areas", "comments": "423", "votes": "3400"},
        {"title": "Require mental health counsellors in every secondary school", "comments": "678", "votes": "5600"},
        {"title": "Protect arts and music subjects in the national curriculum", "comments": "234", "votes": "1800"},
        {"title": "Increase teacher starting salaries in London weighting areas", "comments": "312", "votes": "2500"},
        {"title": "Expand free childcare for working parents to 30 hours", "comments": "489", "votes": "3900"},
        {"title": "Rebuild crumbling school buildings within five years", "comments": "198", "votes": "1500"},
    ],
    "energy": [
        {"title": "Insulate all social housing to EPC C standard by 2030", "comments": "267", "votes": "2100"},
        {"title": "Ban standing charges on domestic energy bills", "comments": "534", "votes": "4200"},
        {"title": "Fund community solar schemes on public buildings", "comments": "123", "votes": "890"},
        {"title": "Cap profits for energy suppliers during price spikes", "comments": "389", "votes": "3100"},
        {"title": "Accelerate heat pump grants for low-income households", "comments": "156", "votes": "1100"},
        {"title": "Nationalise grid infrastructure to reduce transmission costs", "comments": "278", "votes": "2200"},
        {"title": "Require smart meters to display real-time tariff breakdowns", "comments": "89", "votes": "640"},
    ],
    "environment": [
        {"title": "Plant one million urban trees in the next decade", "comments": "345", "votes": "2800"},
        {"title": "Ban single-use plastic packaging in supermarkets", "comments": "678", "votes": "5400"},
        {"title": "Create low-emission zones around schools", "comments": "234", "votes": "1800"},
        {"title": "Fund river cleanup volunteers with equipment grants", "comments": "112", "votes": "820"},
        {"title": "Require food labels to show carbon footprint", "comments": "198", "votes": "1400"},
        {"title": "Protect green belt land from speculative development", "comments": "456", "votes": "3600"},
        {"title": "Mandate recycling collection weekly in all boroughs", "comments": "167", "votes": "1200"},
    ],
    "government": [
        {"title": "Close tax loopholes used by non-domiciled residents", "comments": "534", "votes": "4200"},
        {"title": "Publish line-by-line departmental spending online", "comments": "198", "votes": "1400"},
        {"title": "Introduce a wealth tax on assets above £10 million", "comments": "678", "votes": "5500"},
        {"title": "Fund local councils fairly after years of cuts", "comments": "412", "votes": "3300"},
        {"title": "Cap pay ratios in companies receiving public contracts", "comments": "234", "votes": "1700"},
        {"title": "Reform council tax bands to reflect current property values", "comments": "389", "votes": "3000"},
        {"title": "Audit all pandemic-era contracts for value for money", "comments": "267", "votes": "2000"},
    ],
    "healthcare": [
        {"title": "Build 40 new hospitals by the end of the parliament", "comments": "890", "votes": "7200"},
        {"title": "Fund ambulance services to meet eight-minute response targets", "comments": "567", "votes": "4500"},
        {"title": "Expand screening programmes for common cancers", "comments": "423", "votes": "3400"},
        {"title": "Guarantee same-day cancer referrals where clinically urgent", "comments": "678", "votes": "5600"},
        {"title": "Recruit 10,000 mental health nurses nationally", "comments": "312", "votes": "2500"},
        {"title": "Cap NHS prescription charges for chronic conditions", "comments": "198", "votes": "1500"},
        {"title": "Improve palliative care access in community settings", "comments": "145", "votes": "1100"},
    ],
    "housing": [
        {"title": "Ban no-fault evictions in the private rented sector", "comments": "1200", "votes": "9800"},
        {"title": "Give councils powers to compulsory purchase empty homes", "comments": "678", "votes": "5400"},
        {"title": "Fund insulation grants for private renters", "comments": "234", "votes": "1800"},
        {"title": "Require landlords to register all properties nationally", "comments": "389", "votes": "3100"},
        {"title": "Expand right to buy restrictions on newly built social homes", "comments": "156", "votes": "1200"},
        {"title": "Cap letting agent fees for tenants", "comments": "445", "votes": "3600"},
        {"title": "Prioritise local applicants on social housing waiting lists", "comments": "267", "votes": "2100"},
    ],
    "immigration": [
        {"title": "Fund legal advice for all asylum applicants on arrival", "comments": "534", "votes": "4200"},
        {"title": "End indefinite immigration detention", "comments": "678", "votes": "5500"},
        {"title": "Increase community policing budgets in high-crime wards", "comments": "312", "votes": "2500"},
        {"title": "Mandate body-worn cameras for all frontline officers", "comments": "234", "votes": "1800"},
        {"title": "Reform visa routes for healthcare and social care workers", "comments": "189", "votes": "1400"},
        {"title": "Publish monthly statistics on stop-and-search by ethnicity", "comments": "267", "votes": "2000"},
        {"title": "Expand refuge places for victims of modern slavery", "comments": "145", "votes": "1100"},
    ],
    "international": [
        {"title": "Recognise Palestinian statehood at the United Nations", "comments": "2100", "votes": "16000"},
        {"title": "Increase defence spending to 2.5% of GDP for NATO commitments", "comments": "456", "votes": "3600"},
        {"title": "Ban arms sales to countries violating human rights", "comments": "678", "votes": "5400"},
        {"title": "Fund climate adaptation in developing nations", "comments": "234", "votes": "1800"},
        {"title": "Rejoin the Erasmus student exchange programme", "comments": "312", "votes": "2500"},
        {"title": "Sanction officials linked to election interference abroad", "comments": "189", "votes": "1400"},
        {"title": "Expand refugee resettlement quotas for vulnerable groups", "comments": "523", "votes": "4100"},
    ],
}

MIN_MOTIONS = 6
MAX_MOTIONS = 9

def get_motion_pool(theme):
    return theme["motions"] + EXTRA_MOTIONS.get(theme["id"], [])

def pick_motions_for_page(theme):
    pool = get_motion_pool(theme)
    count = random.randint(MIN_MOTIONS, min(MAX_MOTIONS, len(pool)))
    return random.sample(pool, count)

AI_SUMMARIES = {
    "healthcare-wait-times": {
        "short": "There is a strong consensus among residents regarding the unacceptable wait times for GP appointments. Many are advocating for a guaranteed 48-hour access window for urgent cases, alongside increased funding for out-of-hours services to alleviate pressure on primary care providers.",
        "long": "Residents across Bethnal Green and Stepney are reporting severe difficulty securing timely GP appointments, with many describing weeks-long waits even for conditions that require prompt attention. The frustration is not limited to routine check-ups: parents, carers, and older residents in particular describe being bounced between NHS 111, pharmacies, and overstretched surgeries without a clear path to in-person care.\n\nThe motion to guarantee GP appointments within 48 hours for urgent cases has attracted significant support because it offers a concrete, measurable standard rather than vague promises of improvement. Supporters argue that defining \"urgent\" clearly and publishing ward-level performance data would force accountability while giving patients confidence that escalation routes exist when symptoms worsen.\n\nComplementary motions on out-of-hours pharmacy funding and NHS 111 triage reform reflect a broader demand to relieve pressure on daytime GP capacity. Residents want evening and weekend pharmacy services expanded so minor ailments do not consume appointment slots, and they want 111 call handlers better integrated with local practices so fewer people end up in A&E by default.",
    },
    "business-rates": {
        "short": "Local shop owners are expressing severe financial strain due to current business rates. The community strongly supports an immediate freeze on high street business rates and the introduction of an online sales tax to create a fairer competitive environment for brick-and-mortar stores.",
        "long": "Independent retailers on the high street describe business rates as an existential threat, with several petitioners noting that their annual rate bills now exceed their rent in some cases. The emotional tone of submissions is one of exhaustion: owners who survived the pandemic now face energy costs, reduced footfall, and rate rises they say bear no relation to actual trading conditions.\n\nThe call for an immediate freeze on high street business rates is framed as a stop-gap to prevent further closures while longer-term reform is debated. Supporters want relief targeted at independents rather than large chains, and several motions explicitly ask for local discretion so councils can protect streets that still function as community hubs.\n\nParallel demand for an online sales tax and emergency grants reveals a fairness argument running through the debate. Residents believe digital retailers enjoy structural advantages that hollow out town centres, and they want government action that rebalances competition without punishing consumers—hence the pairing of rate relief with taxation on large e-commerce platforms.",
    },
    "transport": {
        "short": "Commuters are highly frustrated by frequent cancellations and delays on local bus routes. Motions are centered around demanding the restoration of cancelled services, implementing real-time tracking at stops, and imposing stricter penalties on operators failing to meet service standards.",
        "long": "Bus reliability has become a daily source of stress for commuters who depend on public transport to reach work, school, and hospital appointments. Cancellation notices sent with little warning, combined with overcrowded replacement services, have led many residents to describe the network as unreliable enough that they are reconsidering car ownership despite congestion charges.\n\nRestoring cancelled services on central transit routes is the highest-priority ask because those corridors connect Bethnal Green and Stepney to employment centres and healthcare facilities. Petitioners document specific route numbers and time bands where gaps have opened up, arguing that restoration should precede any new infrastructure spending.\n\nReal-time tracking at bus stops and stronger penalties for operators are seen as enforcement mechanisms rather than nice-to-haves. Residents want visible countdown boards at major stops and contractual consequences when operators miss frequency targets, reflecting a belief that transparency and accountability will improve outcomes faster than another round of consultation.",
    },
    "arts": {
        "short": "Discussions are largely focused on child safety online and animal welfare. The most active motions suggest keeping social media accessible but regulated for under-16s, and calling for bans on imagery promoting animal cruelty, specifically dogs with cropped ears.",
        "long": "Debate in this theme clusters around how digital platforms shape childhood experience and how cultural policy intersects with animal welfare standards. Parents and young residents are not speaking with one voice: some emphasise mental-health risks of unrestricted social media, while others resist blanket bans that would isolate teenagers from peers and educational content.\n\nThe motion opposing a ban on social media for under-16s argues for age-appropriate safeguards—verification, parental controls, and algorithmic transparency—rather than prohibition. Supporters contend that bans push usage underground and disproportionately affect young people who rely on social platforms for community, activism, and creative expression.\n\nAnimal welfare motions, including restrictions on imagery of dogs with cropped ears and recognition of circus and fairground heritage, show how cultural policy spans from online moderation to intangible heritage lists. Residents linking these issues often frame them as questions of what society normalises in public media and which traditions deserve formal protection.",
    },
    "benefits": {
        "short": "A major portion of the community is focusing on welfare reform and living standards. The most highly supported motions call for the immediate abolition of the two-child benefit cap and raising the minimum wage to match the real living wage to combat the cost of living crisis.",
        "long": "Welfare and employment policy dominate resident statements, with many describing a gap between official cost-of-living statistics and household reality. Families with three or more children feature prominently in submissions about the two-child benefit cap, often detailing how the policy forces impossible trade-offs between heating, food, and school costs.\n\nAbolishing the two-child cap is presented as an urgent moral and economic intervention. Supporters argue it would immediately lift thousands of children out of poverty and remove a perverse incentive structure that punishes larger families regardless of changing circumstances such as bereavement or relationship breakdown.\n\nMotions on raising the minimum wage to the real living wage and reforming PIP assessments reflect parallel concerns about dignity at work and fair disability support. Residents want wages indexed to actual living costs rather than CPI alone, and they want PIP decisions grounded in medical records rather than adversarial interviews that many describe as traumatic and opaque.",
    },
    "business": {
        "short": "There is significant support for protecting local businesses and ethical supply chains. Residents are advocating for the ban of goods produced via forced labor, simplifying post-Brexit customs for small exporters, and creating a robust national strategy to support independent manufacturing.",
        "long": "Trade and business ethics surface repeatedly in resident motions, with strong language about supply-chain accountability and the survival of small exporters. Several statements draw explicit links between consumer choices abroad and factory conditions overseas, arguing that UK markets should not profit from forced labour regardless of price advantages.\n\nThe forced-labour import ban motion is supported by residents who want clear enforcement mechanisms: border checks, corporate liability, and public procurement rules that exclude tainted goods. Supporters see this as aligning UK trade policy with stated human-rights values rather than adding bureaucracy for its own sake.\n\nSimplifying post-Brexit customs paperwork and protecting independent manufacturing address domestic competitiveness. Small business owners describe forms and delays that large firms can absorb but they cannot, while manufacturing advocates warn that without a national strategy, regional industrial bases will continue to erode in favour of financialised, low-investment models.",
    },
    "courts": {
        "short": "Public sentiment strongly leans towards stricter justice measures and system efficiency. Top motions demand harsher sentences for repeat violent offenders and immediate action to clear the crown court backlog, alongside funding for community rehabilitation.",
        "long": "Justice reform submissions combine demands for tougher consequences for repeat violent crime with frustration at court delays that leave victims and defendants in limbo for years. The tone is often personal: residents cite local incidents and ask why cases take so long to reach trial while expressing support for rehabilitation where it reduces reoffending.\n\nIncreasing sentences for repeat violent offenders resonates with communities that feel existing penalties do not reflect harm caused by habitual offenders. Supporters want sentencing guidelines reviewed so patterns of violence are treated cumulatively rather than as isolated incidents.\n\nClearing the crown court backlog within 24 months and funding community rehabilitation are presented as complementary rather than contradictory. Residents want faster justice for victims while investing in programmes that address root causes of crime, reflecting a pragmatic desire for both accountability and prevention.",
    },
    "education": {
        "short": "Parents and local residents are urgently calling for better school provisions. The dominant motions demand free school meals for all primary children, a significant increase in Special Educational Needs (SEND) funding, and the removal of VAT exemptions for private schools.",
        "long": "Education motions reflect acute pressure on families navigating rising costs and uneven support for children with additional needs. Free school meals for all primary pupils are framed as a universal entitlement that removes stigma and guarantees nutrition during the school day, with parents noting that means-tested schemes miss working families who still struggle.\n\nSEND funding increases are among the most emotionally charged submissions. Carers describe years-long waits for assessments, inadequate classroom support, and children falling behind despite clear diagnoses. Residents want ring-fenced funding and faster EHCP processes so schools are not forced to choose between statutory duties and balanced budgets.\n\nRemoving VAT exemption for private schools is debated as a fairness and revenue measure. Supporters argue the exemption subsidises institutions that already benefit from smaller class sizes and selective intake, and that redirected funds could support state schools serving the majority of local children.",
    },
    "energy": {
        "short": "The community is vocal about transitioning to green energy and addressing high utility costs. Key motions include demands for a social tariff to help vulnerable households with bills, banning new North Sea oil licenses, and accelerating onshore wind farm projects.",
        "long": "Energy policy submissions intertwine climate ambition with immediate bill anxiety. Residents describe choosing between heating and food during winter price spikes, and they want government intervention that protects vulnerable households without delaying the transition away from fossil fuels.\n\nA social tariff for energy bills is supported as a targeted lifeline for pensioners, disabled residents, and low-income families. Petitioners ask for automatic enrolment based on benefits data and clear communication so people do not have to navigate complex application processes while in crisis.\n\nBanning new North Sea oil licences and fast-tracking onshore wind reflect competing timelines within the same debate: stop locking in long-term extraction while accelerating renewables that can reduce bills over time. Supporters of wind expansion emphasise planning reform and community benefit funds so local areas see direct returns from infrastructure on their doorsteps.",
    },
    "environment": {
        "short": "Environmental protection, particularly regarding water quality, is a critical issue for residents. Overwhelming support exists for holding water company executives criminally liable for sewage spills, as well as permanently banning harmful neonicotinoid pesticides.",
        "long": "Environmental concern in this ward is visceral and local: residents describe rivers and canals fouled by sewage, parks sprayed with pesticides, and farming policy that feels disconnected from nature recovery goals. The volume of support for water-quality motions dwarfs many other issues, signalling deep distrust of privatised utilities.\n\nCriminal liability for executives over sewage spills is demanded as a deterrent, not symbolism. Supporters want prosecutions tied to measurable discharge volumes and repeat offences, arguing fines alone are treated as a cost of doing business while communities live with the health and ecological consequences.\n\nPermanent bans on neonicotinoid pesticides and post-Brexit farming subsidies that prioritise nature recovery extend the theme to land use and biodiversity. Residents want pollinator protection written into law and public money directed toward habitat restoration rather than intensive practices that degrade soil and water over decades.",
    },
    "government": {
        "short": "Taxpayer focus is centered on equitable taxation and protecting vulnerable groups. The community strongly supports equalizing capital gains tax with income tax, committing to the triple lock on state pensions, and increasing windfall taxes on energy giants.",
        "long": "Fiscal policy motions reveal a public appetite for tax fairness and predictable support for older residents. Equalising capital gains with income tax is argued on grounds that wealth derived from assets should not be taxed more lightly than wages earned by working households in the constituency.\n\nThe triple lock on state pensions attracts support from residents worried about pensioners falling behind inflation, particularly those without substantial private savings. Submissions often pair this with criticism of energy company profits, suggesting intergenerational solidarity in how windfalls and protections are distributed.\n\nIncreasing windfall taxes on energy companies is seen as a way to fund bill relief and public services without austerity-style cuts elsewhere. Supporters want temporary levies extended until wholesale prices stabilise and receipts ring-fenced for household support and grid investment.",
    },
    "healthcare": {
        "short": "The NHS workforce and service accessibility are major points of concern. Residents are actively campaigning for a fair pay settlement for junior doctors and nurses, urgent reforms to the NHS dental contract, and guaranteed mental health treatment within a 4-week window.",
        "long": "Healthcare submissions paint a system under strain across workforce, dentistry, and mental health. Junior doctor and nurse pay settlements are tied to retention and safety: residents argue that understaffed wards and burned-out clinicians directly affect care quality in local hospitals they rely on.\n\nDental reform motions highlight a postcode lottery where NHS dentists are increasingly unavailable and private fees are unaffordable. Families describe children and pensioners going without routine care until emergencies arise, and they want contract changes that make NHS dentistry viable for practices again.\n\nA four-week guarantee for mental health treatment addresses long waits that residents say exacerbate crises. Supporters want maximum waiting times enshrined with referral tracking published locally, so accountability is visible rather than buried in national statistics that mask regional shortfalls.",
    },
    "housing": {
        "short": "Housing affordability and tenant rights are leading the local debate. The most supported motions call for the immediate abolition of Section 21 no-fault evictions, a commitment to building 100,000 new social homes annually, and the introduction of rent caps.",
        "long": "Housing insecurity runs through a large share of resident statements, with renters describing Section 21 notices used to force moves despite paying rent on time. Abolition is demanded as an immediate protection so tenants can plan schooling, care, and employment without the threat of no-fault eviction hanging over them.\n\nBuilding 100,000 social homes per year is framed as the supply-side answer to overcrowding and homelessness. Supporters want genuinely affordable tenure with secure rights, arguing that market-rate build-to-rent and ownership schemes do not help households on waiting lists that stretch for years in Tower Hamlets.\n\nRent caps in high-demand urban areas complement eviction reform by limiting abrupt price shocks. Residents in Bethnal Green and Stepney describe annual increases that outpace wages, and they want caps linked to local median incomes with exemptions that still allow landlords reasonable returns on maintenance and investment.",
    },
    "immigration": {
        "short": "Border control and local policing are highly debated topics. Strong public support is evident for scrapping the Rwanda deportation scheme, clearing the asylum backlog efficiently, and returning 13,000 neighborhood police officers to local streets.",
        "long": "Immigration and policing motions reflect intense national debate with very local consequences for community cohesion and safety. Scrapping the Rwanda scheme is supported by residents who argue offshore processing is costly, legally contested, and damaging to the UK's humanitarian reputation without reducing irregular crossings.\n\nClearing the asylum backlog within six months is presented as a practical alternative: faster, fair determinations housed in the UK, with adequate legal support so people are not left in prolonged uncertainty that harms mental health and integration prospects.\n\nReturning neighbourhood police officers to the streets addresses feelings of visibility and trust. Petitioners want bobbies back on beats they recognise, with metrics published on response times and community engagement, rather than abstract national recruitment figures that do not translate into everyday presence.",
    },
    "international": {
        "short": "Global humanitarian issues and foreign policy dominate this theme. The community is significantly mobilized around calling for an immediate ceasefire in Gaza, while also maintaining steadfast military and humanitarian support for Ukraine.",
        "long": "International affairs motions show residents engaging with conflicts far beyond the ward while tying them to local values of humanitarianism and security. Calls for an immediate ceasefire in Gaza attract the highest engagement, with statements emphasising civilian protection, aid access, and diplomatic pressure rather than further military escalation.\n\nSupport for Ukraine combines military assistance with humanitarian relief, reflecting a view that sovereignty and civilian survival are linked. Residents want sustained aid with transparency about how funds are used, and several motions stress refugee support obligations at home as part of the same moral commitment.\n\nRestoring the international aid budget to 0.7% of GNI connects overseas policy to development goals residents say were downgraded during domestic fiscal tightening. Supporters argue UK leadership on aid reinforces soft power and addresses root causes of displacement, complementing rather than contradicting security priorities.",
    },
}

DISCLAIMER_SVG = '<svg fill="none" height="14" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" viewBox="0 0 24 24" width="14"><circle cx="12" cy="12" r="10"></circle><line x1="12" x2="12" y1="8" y2="12"></line><line x1="12" x2="12.01" y1="16" y2="16"></line></svg>'
LOGO_SVG = '<svg height="18" viewBox="0 0 120 120" width="18" xmlns="http://www.w3.org/2000/svg"><path d="M 35 35 H 75 V 50 H 90 V 65 H 105 V 105 H 65 V 90 H 50 V 75 H 35 Z" fill="#E63F7F"></path></svg>'

def generate_bar_chart():
    bars = []
    for _ in range(20):
        height = random.randint(30, 100)
        bars.append(f'<div class="bar" style="height: {height}%"></div>')
    return '\n'.join(bars)

def build_ai_summary_block(theme):
    summaries = AI_SUMMARIES[theme["id"]]
    short = summaries["short"]
    long_html = "".join(f"<p>{p.strip()}</p>" for p in summaries["long"].split("\n\n"))
    motions_items = "\n".join(
        f'            <li><a href="#" class="modal-motion-link">{m["title"]}</a></li>'
        for m in theme["motions"]
    )
    return f'''<div class="ai-summary-section">
<div class="ai-summary-header">
{LOGO_SVG}
<h3>AI Summary</h3>
</div>
<p class="ai-summary-text">{short}</p>
<div class="ai-summary-actions">
<button type="button" class="read-more-btn" id="ai-summary-read-more">Read more</button>
</div>
<div class="ai-summary-disclaimer">
{DISCLAIMER_SVG}
<span>This summary was created using a Large Language Model (LLM). Always be safe and proofread the linked motions, as LLMs can sometimes be inaccurate.</span>
</div>
</div>

<div id="ai-summary-modal" class="ai-summary-modal" aria-hidden="true" role="dialog" aria-labelledby="ai-summary-modal-title">
<div class="ai-summary-modal-backdrop"></div>
<div class="ai-summary-modal-dialog">
<button type="button" class="ai-summary-modal-close" id="ai-summary-modal-close" aria-label="Close">
<svg fill="none" height="20" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" viewBox="0 0 24 24" width="20"><line x1="18" x2="6" y1="6" y2="18"></line><line x1="6" x2="18" y1="6" y2="18"></line></svg>
</button>
<h2 class="ai-summary-modal-title" id="ai-summary-modal-title">AI Summary</h2>
<p class="ai-summary-modal-subtitle">Full analysis for {theme["title"]}</p>

<div class="ai-sentiment-section">
    <h4>Sentiment Breakdown</h4>
    <div class="sentiment-item">
        <span class="sentiment-label">Frustrated</span>
        <div class="sentiment-bar-container">
            <div class="sentiment-bar frustrated" style="width: 58%;"></div>
        </div>
        <span class="sentiment-value">58%</span>
    </div>
    <div class="sentiment-item">
        <span class="sentiment-label">Concerned</span>
        <div class="sentiment-bar-container">
            <div class="sentiment-bar concerned" style="width: 28%;"></div>
        </div>
        <span class="sentiment-value">28%</span>
    </div>
    <div class="sentiment-item">
        <span class="sentiment-label">Hopeful</span>
        <div class="sentiment-bar-container">
            <div class="sentiment-bar hopeful" style="style-width: 14%; width: 14%;"></div>
        </div>
        <span class="sentiment-value">14%</span>
    </div>
</div>

<div class="ai-summary-modal-body">
{long_html}
</div>

<div class="ai-summary-modal-sources">
<h4>Source motions</h4>
<p class="ai-summary-modal-source-note">These summaries were scraped and synthesised from the following motions. Always read the original motion text to verify claims.</p>
<ul class="ai-summary-modal-motions">
{motions_items}
</ul>
</div>
<div class="ai-summary-modal-disclaimer">
{DISCLAIMER_SVG}
<span>This summary was created using a Large Language Model (LLM). Always be safe and proofread the linked motions, as LLMs can sometimes be inaccurate.</span>
</div>
</div>
</div>'''

THEMES_DIR = "themes"

# Read the template
with open(f"{THEMES_DIR}/theme-details.html", "r") as f:
    template = f.read()

for theme in themes_data:
    theme_page = {**theme, "motions": pick_motions_for_page(theme)}
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
    
    # AI summary + modal
    content = content.replace("<!-- AI_SUMMARY_BLOCK -->", build_ai_summary_block(theme_page))

    # Bar chart
    content = re.sub(r'<div class="mini-bar-chart">.*?</div>\n                </div>', f'<div class="mini-bar-chart">\n{generate_bar_chart()}\n</div>\n                </div>', content, flags=re.DOTALL)
    
    # Motions list
    motions_html = []
    for m in theme_page['motions']:
        slug = slugify(m["title"])
        m_html = f'''<a class="motion-card" href="motion-{slug}.html" style="text-decoration: none; color: inherit; display: block;">
    <div class="motion-card-content">
        <h4>{m["title"]}</h4>
        <div class="motion-metadata">
            <span class="meta-tag"><svg width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M21 15a2 2 0 0 1-2 2H7l-4 4V5a2 2 0 0 1 2-2h14a2 2 0 0 1 2 2z"></path></svg> {m["comments"]}</span>
            <span class="meta-tag"><svg width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M14 9V5a3 3 0 0 0-3-3l-4 9v11h11.28a2 2 0 0 0 2-1.7l1.38-9a2 2 0 0 0-2-2.3zM7 22H4a2 2 0 0 1-2-2v-7a2 2 0 0 1 2-2h3"></path></svg> {m["votes"]}</span>
            <span class="meta-scope">National</span>
        </div>
    </div>
</a>'''
        motions_html.append(m_html)
    
    motions_section = (
        '<div class="motions-section">\n'
        '<h3 class="motions-section-title">Top motions</h3>\n'
        f'<div class="motion-list">\n{"".join(motions_html)}\n</div>\n'
        '</div>'
    )
    content = re.sub(
        r'<div class="motions-section">.*?</div>\s*</main>',
        f'{motions_section}\n</main>',
        content,
        flags=re.DOTALL,
    )
    
    # FAB tooltip
    content = re.sub(r'See what people care about<br>in Arts, Media and Sport', f'See what people care about<br>in {theme["title"]}', content)
    
    # Write to file
    with open(f'{THEMES_DIR}/theme-{theme["id"]}.html', 'w') as f:
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

# GENERATE MOTION PAGES
with open(f"{THEMES_DIR}/motion-template.html", "r") as f:
    motion_template = f.read()

# Gather all motions
all_motions = []
for theme in themes_data:
    all_motions.extend([(theme, m) for m in theme["motions"]])
    if theme["id"] in EXTRA_MOTIONS:
        all_motions.extend([(theme, m) for m in EXTRA_MOTIONS[theme["id"]]])

motions_generated = 0
for theme, m in all_motions:
    slug = slugify(m["title"])
    content = motion_template
    
    content = content.replace("{{THEME_ID}}", theme["id"])
    content = content.replace("{{TITLE}}", m["title"])
    
    # Generate generic contributor count based on votes
    try:
        contributors = f"{int(m['votes']) * 6:,}"
    except ValueError:
        contributors = "60,225"
        
    content = content.replace("{{CONTRIBUTORS}}", contributors)
    
    # Generic summary paragraph
    summary_text = f"This motion, titled '{m['title']}', has gathered significant attention with {m['votes']} votes and {m['comments']} comments. Supporters argue that this is a critical step forward for the community and urge the government to take immediate action. The proposal aims to address key concerns raised by citizens across the nation."
    content = content.replace("{{SUMMARY}}", summary_text)
    
    content = content.replace("{{MINISTER_NAME}}", theme["minister_name"])
    content = content.replace("{{MINISTER_ROLE}}", theme["minister_role"])
    content = content.replace("{{MINISTER_AVATAR}}", theme["minister_avatar"])
    
    # Bullet points
    bullets = f'''
    <div class="motion-bullet-item"><svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M14 9V5a3 3 0 0 0-3-3l-4 9v11h11.28a2 2 0 0 0 2-1.7l1.38-9a2 2 0 0 0-2-2.3zM7 22H4a2 2 0 0 1-2-2v-7a2 2 0 0 1 2-2h3"></path></svg> Strongly supports community growth</div>
    <div class="motion-bullet-item"><svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M14 9V5a3 3 0 0 0-3-3l-4 9v11h11.28a2 2 0 0 0 2-1.7l1.38-9a2 2 0 0 0-2-2.3zM7 22H4a2 2 0 0 1-2-2v-7a2 2 0 0 1 2-2h3"></path></svg> Addresses fundamental economic needs</div>
    <div class="motion-bullet-item"><svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M14 9V5a3 3 0 0 0-3-3l-4 9v11h11.28a2 2 0 0 0 2-1.7l1.38-9a2 2 0 0 0-2-2.3zM7 22H4a2 2 0 0 1-2-2v-7a2 2 0 0 1 2-2h3"></path></svg> Widely backed by local representatives</div>
    '''
    content = content.replace("{{BULLET_POINTS}}", bullets)
    
    # Similar motions (pick 1 random from same theme)
    similar = [sm for sm in get_motion_pool(theme) if sm["title"] != m["title"]]
    random.shuffle(similar)
    similar = similar[:1]
    
    similar_html = []
    for sm in similar:
        sm_slug = slugify(sm["title"])
        sm_html = f'''
        <a class="similar-motion-card" href="motion-{sm_slug}.html" style="text-decoration: none; display: block; margin-bottom: 1rem;">
            <h4>{sm["title"]}</h4>
            <div class="motion-metadata" style="color: var(--text-muted); font-size: 0.9rem; display: flex; gap: 1rem;">
                <span class="meta-tag"><svg width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M21 15a2 2 0 0 1-2 2H7l-4 4V5a2 2 0 0 1 2-2h14a2 2 0 0 1 2 2z"></path></svg> {sm["comments"]}</span>
                <span class="meta-tag"><svg width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M14 9V5a3 3 0 0 0-3-3l-4 9v11h11.28a2 2 0 0 0 2-1.7l1.38-9a2 2 0 0 0-2-2.3zM7 22H4a2 2 0 0 1-2-2v-7a2 2 0 0 1 2-2h3"></path></svg> {sm["votes"]}</span>
                <span class="meta-scope">National</span>
            </div>
        </a>
        '''
        similar_html.append(sm_html)
        
    content = content.replace("{{SIMILAR_MOTIONS}}", "".join(similar_html))
    
    with open(f"{THEMES_DIR}/motion-{slug}.html", "w") as f:
        f.write(content)
    motions_generated += 1

print(f"Generated 15 theme pages, {motions_generated} motion pages, and updated themes.html")

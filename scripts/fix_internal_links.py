#!/usr/bin/env python3
"""
Fix internal linking across the site for maximum local SEO impact.

Priority 1: Add "Cities We Serve" section to all 6 service pages
Priority 2: Add pricing + cost-guide links to city pages missing them
Priority 3: Add city area block to info/blog pages
Priority 4: Update original 6 city pages to cross-link to newer cities
"""

import re, os

PUBLIC = "public"
ROOT = "."

# ─── helpers ──────────────────────────────────────────────────────────────────

def read(path):
    with open(path, encoding="utf-8") as f:
        return f.read()

def write(path, content):
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"  ✓ {path}")

def insert_before(html, marker, block):
    """Insert block immediately before the first occurrence of marker."""
    idx = html.find(marker)
    if idx == -1:
        print(f"    WARNING: marker not found: {marker[:60]}")
        return html
    return html[:idx] + block + html[idx:]

def replace_once(html, old, new):
    return html.replace(old, new, 1)

def city_grid(cities, label_suffix="→"):
    """Build a .related-grid of city cards."""
    cards = "\n".join(
        f'        <a href="/{slug}.html" class="related-link">{name} &#{arrow}</a>'
        for name, slug in cities
    )
    return cards.replace("&#{arrow}", "&#8594;")

# ─── data ─────────────────────────────────────────────────────────────────────

# All 26 location pages
ALL_CITIES = [
    ("Hixson, TN",            "junk-removal-hixson-tn"),
    ("East Brainerd, TN",     "junk-removal-east-brainerd-tn"),
    ("Red Bank, TN",          "junk-removal-red-bank-tn"),
    ("Ooltewah, TN",          "junk-removal-ooltewah-tn"),
    ("Soddy-Daisy, TN",       "junk-removal-soddy-daisy-tn"),
    ("Signal Mountain, TN",   "junk-removal-signal-mountain-tn"),
    ("Harrison, TN",          "junk-removal-harrison-tn"),
    ("Collegedale, TN",       "junk-removal-collegedale-tn"),
    ("East Ridge, TN",        "junk-removal-east-ridge-tn"),
    ("Middle Valley, TN",     "junk-removal-middle-valley-tn"),
    ("Lakesite, TN",          "junk-removal-lakesite-tn"),
    ("Birchwood, TN",         "junk-removal-birchwood-tn"),
    ("Apison, TN",            "junk-removal-apison-tn"),
    ("Cleveland, TN",         "junk-removal-cleveland-tn"),
    ("Dunlap, TN",            "junk-removal-dunlap-tn"),
    ("Dayton, TN",            "junk-removal-dayton-tn"),
    ("Sale Creek, TN",        "junk-removal-sale-creek-tn"),
    ("Jasper, TN",            "junk-removal-jasper-tn"),
    ("Charleston, TN",        "junk-removal-charleston-tn"),
    ("Lookout Mountain, TN",  "junk-removal-lookout-mountain-tn"),
    ("Ringgold, GA",          "junk-removal-ringgold-ga"),
    ("Fort Oglethorpe, GA",   "junk-removal-fort-oglethorpe-ga"),
    ("Rossville, GA",         "junk-removal-rossville-ga"),
    ("Chickamauga, GA",       "junk-removal-chickamauga-ga"),
    ("LaFayette, GA",         "junk-removal-lafayette-ga"),
    ("Trenton, GA",           "junk-removal-trenton-ga"),
]

# Distributed so every city gets 2-3 inbound links from service pages
SERVICE_PAGES = {
    "furniture-removal-chattanooga-tn": {
        "label": "Furniture Removal",
        "desc": "furniture removal",
        "cities": [
            ("Hixson, TN",          "junk-removal-hixson-tn"),
            ("East Brainerd, TN",   "junk-removal-east-brainerd-tn"),
            ("Ooltewah, TN",        "junk-removal-ooltewah-tn"),
            ("Soddy-Daisy, TN",     "junk-removal-soddy-daisy-tn"),
            ("Harrison, TN",        "junk-removal-harrison-tn"),
            ("East Ridge, TN",      "junk-removal-east-ridge-tn"),
            ("Ringgold, GA",        "junk-removal-ringgold-ga"),
            ("Cleveland, TN",       "junk-removal-cleveland-tn"),
            ("Red Bank, TN",        "junk-removal-red-bank-tn"),
            ("Signal Mountain, TN", "junk-removal-signal-mountain-tn"),
            ("Collegedale, TN",     "junk-removal-collegedale-tn"),
            ("Fort Oglethorpe, GA", "junk-removal-fort-oglethorpe-ga"),
        ],
    },
    "appliance-removal-chattanooga-tn": {
        "label": "Appliance Removal",
        "desc": "appliance removal",
        "cities": [
            ("Hixson, TN",         "junk-removal-hixson-tn"),
            ("Red Bank, TN",       "junk-removal-red-bank-tn"),
            ("East Brainerd, TN",  "junk-removal-east-brainerd-tn"),
            ("Ooltewah, TN",       "junk-removal-ooltewah-tn"),
            ("Soddy-Daisy, TN",    "junk-removal-soddy-daisy-tn"),
            ("Rossville, GA",      "junk-removal-rossville-ga"),
            ("Harrison, TN",       "junk-removal-harrison-tn"),
            ("Middle Valley, TN",  "junk-removal-middle-valley-tn"),
            ("Lakesite, TN",       "junk-removal-lakesite-tn"),
            ("Dunlap, TN",         "junk-removal-dunlap-tn"),
            ("Cleveland, TN",      "junk-removal-cleveland-tn"),
            ("Collegedale, TN",    "junk-removal-collegedale-tn"),
        ],
    },
    "garage-cleanout-chattanooga-tn": {
        "label": "Garage Cleanout",
        "desc": "garage cleanout",
        "cities": [
            ("Hixson, TN",         "junk-removal-hixson-tn"),
            ("East Brainerd, TN",  "junk-removal-east-brainerd-tn"),
            ("Red Bank, TN",       "junk-removal-red-bank-tn"),
            ("Ooltewah, TN",       "junk-removal-ooltewah-tn"),
            ("Soddy-Daisy, TN",    "junk-removal-soddy-daisy-tn"),
            ("Signal Mountain, TN","junk-removal-signal-mountain-tn"),
            ("Collegedale, TN",    "junk-removal-collegedale-tn"),
            ("Apison, TN",         "junk-removal-apison-tn"),
            ("East Ridge, TN",     "junk-removal-east-ridge-tn"),
            ("Harrison, TN",       "junk-removal-harrison-tn"),
            ("Birchwood, TN",      "junk-removal-birchwood-tn"),
            ("Sale Creek, TN",     "junk-removal-sale-creek-tn"),
        ],
    },
    "yard-debris-removal-chattanooga-tn": {
        "label": "Yard Debris Removal",
        "desc": "yard debris removal",
        "cities": [
            ("Soddy-Daisy, TN",    "junk-removal-soddy-daisy-tn"),
            ("Signal Mountain, TN","junk-removal-signal-mountain-tn"),
            ("Harrison, TN",       "junk-removal-harrison-tn"),
            ("Birchwood, TN",      "junk-removal-birchwood-tn"),
            ("Sale Creek, TN",     "junk-removal-sale-creek-tn"),
            ("Lakesite, TN",       "junk-removal-lakesite-tn"),
            ("Dunlap, TN",         "junk-removal-dunlap-tn"),
            ("Cleveland, TN",      "junk-removal-cleveland-tn"),
            ("Dayton, TN",         "junk-removal-dayton-tn"),
            ("Charleston, TN",     "junk-removal-charleston-tn"),
            ("Red Bank, TN",       "junk-removal-red-bank-tn"),
            ("Hixson, TN",         "junk-removal-hixson-tn"),
        ],
    },
    "estate-cleanout-chattanooga-tn": {
        "label": "Estate Cleanout",
        "desc": "estate cleanout",
        "cities": [
            ("Hixson, TN",          "junk-removal-hixson-tn"),
            ("East Brainerd, TN",   "junk-removal-east-brainerd-tn"),
            ("Red Bank, TN",        "junk-removal-red-bank-tn"),
            ("Ooltewah, TN",        "junk-removal-ooltewah-tn"),
            ("Signal Mountain, TN", "junk-removal-signal-mountain-tn"),
            ("Harrison, TN",        "junk-removal-harrison-tn"),
            ("Cleveland, TN",       "junk-removal-cleveland-tn"),
            ("Chickamauga, GA",     "junk-removal-chickamauga-ga"),
            ("LaFayette, GA",       "junk-removal-lafayette-ga"),
            ("Ringgold, GA",        "junk-removal-ringgold-ga"),
            ("Fort Oglethorpe, GA", "junk-removal-fort-oglethorpe-ga"),
            ("Trenton, GA",         "junk-removal-trenton-ga"),
        ],
    },
    "same-day-junk-removal-chattanooga-tn": {
        "label": "Same-Day Service",
        "desc": "same-day junk removal",
        "cities": [
            ("Hixson, TN",          "junk-removal-hixson-tn"),
            ("East Brainerd, TN",   "junk-removal-east-brainerd-tn"),
            ("Red Bank, TN",        "junk-removal-red-bank-tn"),
            ("Ooltewah, TN",        "junk-removal-ooltewah-tn"),
            ("Soddy-Daisy, TN",     "junk-removal-soddy-daisy-tn"),
            ("Signal Mountain, TN", "junk-removal-signal-mountain-tn"),
            ("East Ridge, TN",      "junk-removal-east-ridge-tn"),
            ("Rossville, GA",       "junk-removal-rossville-ga"),
            ("Ringgold, GA",        "junk-removal-ringgold-ga"),
            ("Harrison, TN",        "junk-removal-harrison-tn"),
            ("Collegedale, TN",     "junk-removal-collegedale-tn"),
            ("Lookout Mountain, TN","junk-removal-lookout-mountain-tn"),
        ],
    },
}

# Nearby links for original 6 city pages → newer cities to add
ORIG_CITY_NEARBY = {
    "junk-removal-hixson-tn": [
        ("Soddy-Daisy, TN",    "junk-removal-soddy-daisy-tn"),
        ("Middle Valley, TN",  "junk-removal-middle-valley-tn"),
        ("Red Bank, TN",       "junk-removal-red-bank-tn"),
        ("Lakesite, TN",       "junk-removal-lakesite-tn"),
        ("Sale Creek, TN",     "junk-removal-sale-creek-tn"),
        ("Harrison, TN",       "junk-removal-harrison-tn"),
    ],
    "junk-removal-east-brainerd-tn": [
        ("Ooltewah, TN",       "junk-removal-ooltewah-tn"),
        ("Collegedale, TN",    "junk-removal-collegedale-tn"),
        ("Apison, TN",         "junk-removal-apison-tn"),
        ("East Ridge, TN",     "junk-removal-east-ridge-tn"),
        ("Ringgold, GA",       "junk-removal-ringgold-ga"),
        ("Fort Oglethorpe, GA","junk-removal-fort-oglethorpe-ga"),
    ],
    "junk-removal-red-bank-tn": [
        ("Hixson, TN",         "junk-removal-hixson-tn"),
        ("Signal Mountain, TN","junk-removal-signal-mountain-tn"),
        ("Lookout Mountain, TN","junk-removal-lookout-mountain-tn"),
        ("East Ridge, TN",     "junk-removal-east-ridge-tn"),
        ("Rossville, GA",      "junk-removal-rossville-ga"),
        ("Middle Valley, TN",  "junk-removal-middle-valley-tn"),
    ],
    "junk-removal-ooltewah-tn": [
        ("East Brainerd, TN",  "junk-removal-east-brainerd-tn"),
        ("Collegedale, TN",    "junk-removal-collegedale-tn"),
        ("Apison, TN",         "junk-removal-apison-tn"),
        ("Cleveland, TN",      "junk-removal-cleveland-tn"),
        ("Harrison, TN",       "junk-removal-harrison-tn"),
        ("Ringgold, GA",       "junk-removal-ringgold-ga"),
    ],
    "junk-removal-soddy-daisy-tn": [
        ("Sale Creek, TN",     "junk-removal-sale-creek-tn"),
        ("Birchwood, TN",      "junk-removal-birchwood-tn"),
        ("Harrison, TN",       "junk-removal-harrison-tn"),
        ("Lakesite, TN",       "junk-removal-lakesite-tn"),
        ("Dayton, TN",         "junk-removal-dayton-tn"),
        ("Middle Valley, TN",  "junk-removal-middle-valley-tn"),
    ],
    "junk-removal-signal-mountain-tn": [
        ("Lookout Mountain, TN","junk-removal-lookout-mountain-tn"),
        ("Red Bank, TN",       "junk-removal-red-bank-tn"),
        ("Dunlap, TN",         "junk-removal-dunlap-tn"),
        ("Jasper, TN",         "junk-removal-jasper-tn"),
        ("Middle Valley, TN",  "junk-removal-middle-valley-tn"),
        ("Hixson, TN",         "junk-removal-hixson-tn"),
    ],
}

# ─── PRIORITY 1: Add Cities section to service pages ──────────────────────────

def make_cities_section(label, desc, cities):
    cards = "\n".join(
        f'        <a href="/{slug}.html" class="related-link">{name} &#8594;</a>'
        for name, slug in cities
    )
    return f"""
  <section id="service-cities" style="background:#f0f6ff;">
    <div class="container">
      <h2>{label} in Chattanooga &amp; Surrounding Areas</h2>
      <p>We provide {desc} throughout the greater Chattanooga metro — Hamilton County, Bradley County, Sequatchie County, and North Georgia. Select your city for local service details and availability:</p>
      <div class="related-grid" style="margin-top:16px;">
{cards}
      </div>
    </div>
  </section>

"""

def add_cities_to_service_pages():
    print("\n── Priority 1: Service pages → city sections ──")
    for slug, data in SERVICE_PAGES.items():
        path = os.path.join(PUBLIC, f"{slug}.html")
        if not os.path.exists(path):
            print(f"  SKIP (not found): {path}")
            continue
        html = read(path)
        # Skip if already done
        if 'id="service-cities"' in html:
            print(f"  already done: {slug}")
            continue
        block = make_cities_section(data["label"], data["desc"], data["cities"])
        html = insert_before(html, '  <section id="contact">', block)
        write(path, html)

# ─── PRIORITY 2: Add pricing + cost-guide links to city pages ─────────────────

PRICING_SNIPPET = ' See our <a href="/junk-removal-pricing-chattanooga-tn.html" style="color:#1a2e4a;font-weight:600;">Chattanooga pricing guide</a> or the <a href="/how-much-does-junk-removal-cost-chattanooga.html" style="color:#1a2e4a;font-weight:600;">junk removal cost guide</a> for estimates before you call.'

def ensure_pricing_links_in_city_pages():
    print("\n── Priority 2: City pages → pricing + cost-guide links ──")
    city_slugs = [slug for _, slug in ALL_CITIES]
    for slug in city_slugs:
        path = os.path.join(PUBLIC, f"{slug}.html")
        if not os.path.exists(path):
            print(f"  SKIP (not found): {path}")
            continue
        html = read(path)
        # Already has both links?
        has_pricing = "junk-removal-pricing-chattanooga-tn.html" in html
        has_cost    = "how-much-does-junk-removal-cost-chattanooga.html" in html
        if has_pricing and has_cost:
            print(f"  already complete: {slug}")
            continue
        modified = False
        # If has pricing but not cost guide, append to the pricing link paragraph
        if has_pricing and not has_cost:
            # Find the pricing link context and append cost guide
            old = '<a href="/junk-removal-pricing-chattanooga-tn.html" style="color:#1a2e4a;font-weight:600;">Pricing Guide &#8594;</a>'
            if old in html:
                new = old + '\n        <a href="/how-much-does-junk-removal-cost-chattanooga.html" class="related-link">Junk Removal Cost Guide &#8594;</a>'
                html = replace_once(html, old, new)
                modified = True
        # If missing pricing entirely, inject into the related-grid before </div>
        if not has_pricing:
            # Find the related-grid closing and insert before it
            pattern = r'(</div>\s*</section>\s*<section id="contact")'
            inject = (
                '\n        <a href="/junk-removal-pricing-chattanooga-tn.html" class="related-link">Pricing Guide &#8594;</a>'
                '\n        <a href="/how-much-does-junk-removal-cost-chattanooga.html" class="related-link">Cost Guide &#8594;</a>'
            )
            # Try to find related-grid and append cards before closing </div>
            m = re.search(r'(class="related-grid"[^>]*>)(.*?)(</div>)', html, re.DOTALL)
            if m:
                replacement = m.group(1) + m.group(2) + inject + '\n      ' + m.group(3)
                html = html[:m.start()] + replacement + html[m.end():]
                modified = True
        if modified:
            write(path, html)
        else:
            print(f"  no change pattern found: {slug}")

# ─── PRIORITY 3: Add city area block to info/blog pages ──────────────────────

INFO_CITIES_BLOCK = """
  <section id="service-areas" style="background:#f0f6ff;">
    <div class="container">
      <h2>Serving Chattanooga &amp; Surrounding Communities</h2>
      <p>We haul junk across Chattanooga, Hamilton County, and into North Georgia. Find local service details for your area:</p>
      <div class="related-grid" style="margin-top:16px;">
        <a href="/junk-removal-hixson-tn.html" class="related-link">Hixson, TN &#8594;</a>
        <a href="/junk-removal-east-brainerd-tn.html" class="related-link">East Brainerd, TN &#8594;</a>
        <a href="/junk-removal-red-bank-tn.html" class="related-link">Red Bank, TN &#8594;</a>
        <a href="/junk-removal-ooltewah-tn.html" class="related-link">Ooltewah, TN &#8594;</a>
        <a href="/junk-removal-soddy-daisy-tn.html" class="related-link">Soddy-Daisy, TN &#8594;</a>
        <a href="/junk-removal-signal-mountain-tn.html" class="related-link">Signal Mountain, TN &#8594;</a>
        <a href="/junk-removal-harrison-tn.html" class="related-link">Harrison, TN &#8594;</a>
        <a href="/junk-removal-ringgold-ga.html" class="related-link">Ringgold, GA &#8594;</a>
        <a href="/junk-removal-east-ridge-tn.html" class="related-link">East Ridge, TN &#8594;</a>
        <a href="/junk-removal-cleveland-tn.html" class="related-link">Cleveland, TN &#8594;</a>
        <a href="/junk-removal-fort-oglethorpe-ga.html" class="related-link">Fort Oglethorpe, GA &#8594;</a>
        <a href="/junk-removal-collegedale-tn.html" class="related-link">Collegedale, TN &#8594;</a>
      </div>
    </div>
  </section>

"""

INFO_PAGES = [
    "how-much-does-junk-removal-cost-chattanooga",
    "how-to-get-rid-of-old-furniture-chattanooga",
    "junk-removal-near-me",
    "junk-removal-pricing-chattanooga-tn",
]

def add_cities_to_info_pages():
    print("\n── Priority 3: Info pages → city area blocks ──")
    for slug in INFO_PAGES:
        path = os.path.join(PUBLIC, f"{slug}.html")
        if not os.path.exists(path):
            print(f"  SKIP (not found): {path}")
            continue
        html = read(path)
        if 'id="service-areas"' in html:
            print(f"  already done: {slug}")
            continue
        html = insert_before(html, '  <section id="contact">', INFO_CITIES_BLOCK)
        write(path, html)

# ─── PRIORITY 4: Original 6 city pages → link to newer nearby cities ─────────

def add_nearby_to_original_cities():
    print("\n── Priority 4: Original 6 city pages → link to newer cities ──")
    for slug, nearby in ORIG_CITY_NEARBY.items():
        path = os.path.join(PUBLIC, f"{slug}.html")
        if not os.path.exists(path):
            print(f"  SKIP (not found): {path}")
            continue
        html = read(path)
        # Check if already has links to the new cities
        already_linked = sum(1 for _, s in nearby if f"/{s}.html" in html)
        if already_linked >= 3:
            print(f"  already has {already_linked} new-city links: {slug}")
            continue
        # Build a "More Nearby Areas" section and insert before contact
        cards = "\n".join(
            f'        <a href="/{s}.html" class="related-link">{n} &#8594;</a>'
            for n, s in nearby
        )
        block = f"""
  <section id="nearby-extended" style="background:#f0f6ff;">
    <div class="container">
      <h2>More Areas We Serve Nearby</h2>
      <p>We cover all of Hamilton County and beyond. Here are more communities near you that we serve regularly:</p>
      <div class="related-grid" style="margin-top:16px;">
{cards}
      </div>
    </div>
  </section>

"""
        if 'id="nearby-extended"' in html:
            print(f"  already done: {slug}")
            continue
        html = insert_before(html, '  <section id="contact">', block)
        write(path, html)

# ─── run all ──────────────────────────────────────────────────────────────────

if __name__ == "__main__":
    add_cities_to_service_pages()
    ensure_pricing_links_in_city_pages()
    add_cities_to_info_pages()
    add_nearby_to_original_cities()
    print("\nDone.")

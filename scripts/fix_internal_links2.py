#!/usr/bin/env python3
"""
Fix remaining internal linking issues:
1. Service pages (same-day) – contact marker had style attr, re-do with regex
2. Original 6 city pages – add nearby-extended section using regex contact finder
3. ALL city pages – add cost-guide card to related-grid (body only, not nav)
"""

import re, os

PUBLIC = "public"

# ── helpers ───────────────────────────────────────────────────────────────────

def read(path):
    with open(path, encoding="utf-8") as f:
        return f.read()

def write(path, content):
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"  ✓ {path}")

def insert_before_contact(html, block):
    """Insert block immediately before <section id=\"contact\"> using regex."""
    m = re.search(r'<section id="contact"', html)
    if not m:
        print("    WARNING: contact section not found")
        return html, False
    idx = m.start()
    return html[:idx] + block + html[idx:], True

# ── Fix 1: same-day service page cities section ───────────────────────────────

SAME_DAY_CITIES = [
    ("Hixson, TN",           "junk-removal-hixson-tn"),
    ("East Brainerd, TN",    "junk-removal-east-brainerd-tn"),
    ("Red Bank, TN",         "junk-removal-red-bank-tn"),
    ("Ooltewah, TN",         "junk-removal-ooltewah-tn"),
    ("Soddy-Daisy, TN",      "junk-removal-soddy-daisy-tn"),
    ("Signal Mountain, TN",  "junk-removal-signal-mountain-tn"),
    ("East Ridge, TN",       "junk-removal-east-ridge-tn"),
    ("Rossville, GA",        "junk-removal-rossville-ga"),
    ("Ringgold, GA",         "junk-removal-ringgold-ga"),
    ("Harrison, TN",         "junk-removal-harrison-tn"),
    ("Collegedale, TN",      "junk-removal-collegedale-tn"),
    ("Lookout Mountain, TN", "junk-removal-lookout-mountain-tn"),
]

def fix_same_day():
    print("\n── Fix 1: same-day service page ──")
    path = os.path.join(PUBLIC, "same-day-junk-removal-chattanooga-tn.html")
    html = read(path)
    if 'id="service-cities"' in html:
        print("  already done"); return
    cards = "\n".join(
        f'        <a href="/{slug}.html" class="related-link">{name} &#8594;</a>'
        for name, slug in SAME_DAY_CITIES
    )
    block = f"""  <section id="service-cities" style="background:#f0f6ff;">
    <div class="container">
      <h2>Same-Day Junk Removal in Chattanooga &amp; Surrounding Areas</h2>
      <p>We offer same-day junk removal throughout the greater Chattanooga metro — Hamilton County, North Georgia, and beyond. Select your city for local service details:</p>
      <div class="related-grid" style="margin-top:16px;">
{cards}
      </div>
    </div>
  </section>

  """
    html, ok = insert_before_contact(html, block)
    if ok:
        write(path, html)

# ── Fix 2: Original 6 city pages → nearby-extended section ───────────────────

ORIG_CITY_NEARBY = {
    "junk-removal-hixson-tn": [
        ("Middle Valley, TN",  "junk-removal-middle-valley-tn"),
        ("Lakesite, TN",       "junk-removal-lakesite-tn"),
        ("Sale Creek, TN",     "junk-removal-sale-creek-tn"),
        ("Harrison, TN",       "junk-removal-harrison-tn"),
        ("Birchwood, TN",      "junk-removal-birchwood-tn"),
        ("Dayton, TN",         "junk-removal-dayton-tn"),
    ],
    "junk-removal-east-brainerd-tn": [
        ("Collegedale, TN",    "junk-removal-collegedale-tn"),
        ("Apison, TN",         "junk-removal-apison-tn"),
        ("East Ridge, TN",     "junk-removal-east-ridge-tn"),
        ("Ringgold, GA",       "junk-removal-ringgold-ga"),
        ("Fort Oglethorpe, GA","junk-removal-fort-oglethorpe-ga"),
        ("Rossville, GA",      "junk-removal-rossville-ga"),
    ],
    "junk-removal-red-bank-tn": [
        ("Lookout Mountain, TN","junk-removal-lookout-mountain-tn"),
        ("East Ridge, TN",     "junk-removal-east-ridge-tn"),
        ("Rossville, GA",      "junk-removal-rossville-ga"),
        ("Middle Valley, TN",  "junk-removal-middle-valley-tn"),
        ("Hixson, TN",         "junk-removal-hixson-tn"),
        ("Signal Mountain, TN","junk-removal-signal-mountain-tn"),
    ],
    "junk-removal-ooltewah-tn": [
        ("Collegedale, TN",    "junk-removal-collegedale-tn"),
        ("Apison, TN",         "junk-removal-apison-tn"),
        ("Cleveland, TN",      "junk-removal-cleveland-tn"),
        ("Harrison, TN",       "junk-removal-harrison-tn"),
        ("Ringgold, GA",       "junk-removal-ringgold-ga"),
        ("East Brainerd, TN",  "junk-removal-east-brainerd-tn"),
    ],
    "junk-removal-soddy-daisy-tn": [
        ("Sale Creek, TN",     "junk-removal-sale-creek-tn"),
        ("Birchwood, TN",      "junk-removal-birchwood-tn"),
        ("Lakesite, TN",       "junk-removal-lakesite-tn"),
        ("Dayton, TN",         "junk-removal-dayton-tn"),
        ("Middle Valley, TN",  "junk-removal-middle-valley-tn"),
        ("Charleston, TN",     "junk-removal-charleston-tn"),
    ],
    "junk-removal-signal-mountain-tn": [
        ("Lookout Mountain, TN","junk-removal-lookout-mountain-tn"),
        ("Dunlap, TN",         "junk-removal-dunlap-tn"),
        ("Jasper, TN",         "junk-removal-jasper-tn"),
        ("Middle Valley, TN",  "junk-removal-middle-valley-tn"),
        ("Red Bank, TN",       "junk-removal-red-bank-tn"),
        ("Hixson, TN",         "junk-removal-hixson-tn"),
    ],
}

def fix_original_city_pages():
    print("\n── Fix 2: Original 6 city pages → nearby-extended ──")
    for slug, nearby in ORIG_CITY_NEARBY.items():
        path = os.path.join(PUBLIC, f"{slug}.html")
        html = read(path)
        if 'id="nearby-extended"' in html:
            print(f"  already done: {slug}"); continue
        cards = "\n".join(
            f'        <a href="/{s}.html" class="related-link">{n} &#8594;</a>'
            for n, s in nearby
        )
        block = f"""  <section id="nearby-extended" style="background:#f0f6ff;">
    <div class="container">
      <h2>More Areas We Serve Nearby</h2>
      <p>We cover all of Hamilton County and beyond. Here are more communities near you that we serve regularly:</p>
      <div class="related-grid" style="margin-top:16px;">
{cards}
      </div>
    </div>
  </section>

  """
        html, ok = insert_before_contact(html, block)
        if ok:
            write(path, html)

# ── Fix 3: All city pages → cost-guide card in body related-grid ──────────────

ALL_CITY_SLUGS = [
    "junk-removal-hixson-tn",
    "junk-removal-east-brainerd-tn",
    "junk-removal-red-bank-tn",
    "junk-removal-ooltewah-tn",
    "junk-removal-soddy-daisy-tn",
    "junk-removal-signal-mountain-tn",
    "junk-removal-harrison-tn",
    "junk-removal-collegedale-tn",
    "junk-removal-east-ridge-tn",
    "junk-removal-middle-valley-tn",
    "junk-removal-lakesite-tn",
    "junk-removal-birchwood-tn",
    "junk-removal-apison-tn",
    "junk-removal-cleveland-tn",
    "junk-removal-dunlap-tn",
    "junk-removal-dayton-tn",
    "junk-removal-sale-creek-tn",
    "junk-removal-jasper-tn",
    "junk-removal-charleston-tn",
    "junk-removal-lookout-mountain-tn",
    "junk-removal-ringgold-ga",
    "junk-removal-fort-oglethorpe-ga",
    "junk-removal-rossville-ga",
    "junk-removal-chickamauga-ga",
    "junk-removal-lafayette-ga",
    "junk-removal-trenton-ga",
]

COST_CARD   = '\n        <a href="/how-much-does-junk-removal-cost-chattanooga.html" class="related-link">Cost Guide &#8594;</a>'
PRICE_CARD  = '\n        <a href="/junk-removal-pricing-chattanooga-tn.html" class="related-link">Pricing Guide &#8594;</a>'

def add_cost_guide_to_city_pages():
    """
    For each city page, find the related-grid in the BODY (after </style>) and
    append missing Pricing Guide / Cost Guide cards before its closing </div>.
    """
    print("\n── Fix 3: City pages → cost-guide card in related-grid ──")
    for slug in ALL_CITY_SLUGS:
        path = os.path.join(PUBLIC, f"{slug}.html")
        if not os.path.exists(path):
            print(f"  SKIP: {path}"); continue
        html = read(path)

        # Work only on the body (after </style>)
        style_end = html.find("</style>")
        if style_end == -1:
            print(f"  no </style>: {slug}"); continue
        head = html[:style_end + 8]
        body = html[style_end + 8:]

        has_cost  = "how-much-does-junk-removal-cost-chattanooga.html" in body
        # Distinguish body pricing links (class="related-link") from nav links
        has_price_body = bool(re.search(
            r'href="/junk-removal-pricing-chattanooga-tn\.html"[^>]*class="related-link"', body
        ))

        if has_cost and has_price_body:
            print(f"  complete: {slug}"); continue

        # Find the last related-grid closing </div> in body
        # The grid div ends with: \n      </div> or \n        </div>
        m = None
        for match in re.finditer(r'class="related-grid"[^>]*>(.*?)</div>', body, re.DOTALL):
            m = match  # keep the last match
        if not m:
            print(f"  no related-grid found: {slug}"); continue

        grid_inner = m.group(1)
        inject = ""
        if not has_price_body:
            inject += PRICE_CARD
        if not has_cost:
            inject += COST_CARD

        new_body = body[:m.start(1)] + grid_inner + inject + "\n      " + body[m.start(1) + len(grid_inner):]
        write(path, head + new_body)

# ── run ───────────────────────────────────────────────────────────────────────

if __name__ == "__main__":
    fix_same_day()
    fix_original_city_pages()
    add_cost_guide_to_city_pages()
    print("\nDone.")

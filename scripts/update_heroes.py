#!/usr/bin/env python3
"""
Replace hero sections on all 5 service pages + 6 location pages
with unique, SEO-optimised, conversion-focused heroes.
Each hero has: unique H1 + unique sub-paragraph, direct CTA, visible phone link.
"""
import re, os

PHONE_DISPLAY = "(423) 556-3473"
PHONE_TEL     = "tel:+14235563473"

# ── new hero CSS to inject (once per file if not already present) ───────────
HERO_PHONE_CSS = """
    .hero-phone-link {
      display: inline-block;
      margin-top: 14px;
      font-size: 1.25rem;
      font-weight: 800;
      color: #1a2e4a;
      text-decoration: none;
      letter-spacing: 0.01em;
    }
    .hero-phone-link:hover { color: #f97316; }
    .hero-phone-label {
      display: block;
      font-size: 0.82rem;
      font-weight: 600;
      color: #6b7280;
      margin-top: 4px;
      letter-spacing: 0;
    }
"""

# ── hero data: (h1, subparagraph, cta_text, btn_sub) ───────────────────────
HEROES = {
    "public/furniture-removal-chattanooga-tn.html": {
        "h1":  "Furniture Removal in Chattanooga, TN",
        "sub": (
            "Got a couch that won't fit through the door, a mattress on its last legs, "
            "or a bedroom set you're finally replacing? We pick up all types of furniture "
            "from Chattanooga homes and rentals — same-day pickup often available, and "
            "we handle every bit of the heavy lifting."
        ),
        "cta": "Call Now for Same-Day Furniture Pickup",
        "note": "No obligation &bull; We haul it — you don't lift a thing",
    },
    "public/appliance-removal-chattanooga-tn.html": {
        "h1":  "Appliance Removal in Chattanooga, TN",
        "sub": (
            "Old fridge blocking your kitchen, washer sitting in the driveway, "
            "or a broken dryer you've been stepping around for months? "
            "We disconnect and haul away bulky appliances across Chattanooga — "
            "fast turnaround and same-day appointments often available."
        ),
        "cta": "Call for Same-Day Appliance Pickup",
        "note": "Available 7 days a week &bull; Free estimates over the phone",
    },
    "public/garage-cleanout-chattanooga-tn.html": {
        "h1":  "Garage Cleanout in Chattanooga, TN",
        "sub": (
            "Ready to actually park in your garage again? "
            "We clear out years of accumulated junk — boxes, tools, old equipment, "
            "broken furniture, and anything else taking up space — from Chattanooga homes "
            "and rentals. Same-day garage cleanouts are often available."
        ),
        "cta": "Call Now — Get Your Garage Cleared Today",
        "note": "Same-day available &bull; One call, one trip, done",
    },
    "public/yard-debris-removal-chattanooga-tn.html": {
        "h1":  "Yard Debris Removal in Chattanooga, TN",
        "sub": (
            "Storm brought down branches? Brush pile getting out of hand? "
            "Need a full outdoor cleanup before your yard is usable again? "
            "We haul away yard waste and debris from Chattanooga properties fast — "
            "same-day and next-day pickups available."
        ),
        "cta": "Call for Fast Yard Debris Pickup",
        "note": "Free estimate &bull; We load and haul &bull; 7 days a week",
    },
    "public/estate-cleanout-chattanooga-tn.html": {
        "h1":  "Estate Cleanout in Chattanooga, TN",
        "sub": (
            "Clearing out a family home, inherited property, or rental between tenants? "
            "We handle full estate cleanouts across the Chattanooga area — "
            "furniture, appliances, personal items, and everything in between. "
            "We work efficiently and respectfully, with same-day service often available."
        ),
        "cta": "Call to Schedule Your Estate Cleanout",
        "note": "Upfront pricing &bull; Full-service removal &bull; 7 days a week",
    },
    "public/junk-removal-hixson-tn.html": {
        "h1":  "Junk Removal in Hixson, TN",
        "sub": (
            "Whether you're clearing out a garage off Hixson Pike, hauling furniture "
            "from a home near Chester Frost Park, or dealing with leftover renovation "
            "debris, our crew can be there fast. We serve Hixson and the broader "
            "Chattanooga area 7 days a week — same-day pickups often available."
        ),
        "cta": "Call Now for Same-Day Pickup in Hixson",
        "note": "No obligation &bull; Free estimate over the phone",
    },
    "public/junk-removal-east-brainerd-tn.html": {
        "h1":  "Junk Removal in East Brainerd, TN",
        "sub": (
            "Need junk hauled away in East Brainerd? From a single piece of furniture "
            "to a full property cleanout, we serve East Brainerd and the surrounding "
            "Chattanooga area quickly and affordably. Same-day service is often "
            "available — just give us a call."
        ),
        "cta": "Call for Fast Junk Removal in East Brainerd",
        "note": "Available 7 days a week &bull; Upfront pricing before we start",
    },
    "public/junk-removal-red-bank-tn.html": {
        "h1":  "Junk Removal in Red Bank, TN",
        "sub": (
            "Red Bank residents trust us for straightforward, affordable junk removal — "
            "old furniture, appliances, yard waste, and more. "
            "We serve Red Bank and all of the Chattanooga area seven days a week, "
            "with same-day appointments often available for calls before noon."
        ),
        "cta": "Call Now — Same-Day Pickup Available in Red Bank",
        "note": "Free estimate &bull; No hidden fees &bull; We do the lifting",
    },
    "public/junk-removal-ooltewah-tn.html": {
        "h1":  "Junk Removal in Ooltewah, TN",
        "sub": (
            "From growing neighborhoods to established homes, we haul away furniture, "
            "appliances, debris, and more across Ooltewah and the greater Chattanooga "
            "region. Call for a free quote — same-day and next-day appointments "
            "are regularly available."
        ),
        "cta": "Call for Junk Removal in Ooltewah Today",
        "note": "7 days a week &bull; Same-day often available &bull; Free estimates",
    },
    "public/junk-removal-soddy-daisy-tn.html": {
        "h1":  "Junk Removal in Soddy-Daisy, TN",
        "sub": (
            "We haul away furniture, appliances, yard debris, and general junk "
            "from Soddy-Daisy homes and businesses. Fast, reliable service in the "
            "northern Chattanooga area — same-day pickups are often available "
            "when you call before noon."
        ),
        "cta": "Call Now for Same-Day Pickup in Soddy-Daisy",
        "note": "No obligation &bull; Upfront pricing &bull; 7 days a week",
    },
    "public/junk-removal-signal-mountain-tn.html": {
        "h1":  "Junk Removal in Signal Mountain, TN",
        "sub": (
            "Need a reliable crew to haul junk off Signal Mountain? "
            "We serve Signal Mountain and the wider Chattanooga area with "
            "fast, affordable removal — furniture, appliances, cleanouts, and more. "
            "Same-day and next-day appointments available."
        ),
        "cta": "Call for Junk Removal on Signal Mountain",
        "note": "Free estimate &bull; Same-day often available &bull; We haul it away",
    },
}


def build_hero(data):
    """Return the full replacement <section class=\"hero\">...</section> block."""
    return (
        '  <section class="hero">\n'
        '    <div class="container">\n'
        f'      <h1>{data["h1"]}</h1>\n'
        f'      <p>{data["sub"]}</p>\n'
        f'      <a class="btn" href="{PHONE_TEL}">&#128222;&nbsp; {data["cta"]}</a>\n'
        f'      <a class="hero-phone-link" href="{PHONE_TEL}">{PHONE_DISPLAY}</a>\n'
        f'      <span class="hero-phone-label">Call or text — free estimate, no obligation</span>\n'
        f'      <span class="btn-sub">{data["note"]}</span>\n'
        '    </div>\n'
        '  </section>'
    )


def inject_css(html):
    """Add hero-phone CSS before </style> if not already there."""
    if 'hero-phone-link' in html:
        return html
    return html.replace('  </style>', HERO_PHONE_CSS + '  </style>', 1)


def replace_hero(html, hero_html):
    """Replace existing <section class="hero">...</section> with new hero."""
    return re.sub(
        r'  <section class="hero">.*?</section>',
        hero_html,
        html,
        count=1,
        flags=re.DOTALL,
    )


updated, errors = [], []

for path, data in HEROES.items():
    try:
        with open(path) as f:
            html = f.read()

        html = inject_css(html)
        html = replace_hero(html, build_hero(data))

        with open(path, "w") as f:
            f.write(html)

        updated.append(path)
        print(f"OK  {path}")
    except Exception as e:
        errors.append((path, str(e)))
        print(f"ERR {path}: {e}")

print(f"\n{len(updated)} updated, {len(errors)} errors")
if errors:
    for p, e in errors:
        print(f"  ! {p}: {e}")

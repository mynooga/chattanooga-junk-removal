#!/usr/bin/env python3
"""
Full-site humanization: adds photo blocks distributed throughout every service,
location, about, contact, and pricing page. Also upgrades header on all pages.
"""
import re, os

PHONE = "(423) 556-3473"
TEL   = "tel:+14235563473"

# ── shared photo CSS to inject into every page ─────────────────────────────
PHOTO_CSS = """
    /* ── PHOTO BLOCKS ── */
    .photo-row { display:grid; grid-template-columns:repeat(3,1fr); gap:14px; margin:28px 0; }
    .photo-row-2 { display:grid; grid-template-columns:1fr 1fr; gap:14px; margin:28px 0; }
    .photo-item { position:relative; border-radius:8px; overflow:hidden; height:220px; }
    .photo-item img { width:100%; height:100%; object-fit:cover; display:block; transition:transform .3s; }
    .photo-item:hover img { transform:scale(1.04); }
    .photo-caption { position:absolute; bottom:0; left:0; right:0;
      background:linear-gradient(transparent,rgba(15,28,46,.88));
      color:#fff; font-size:.85rem; font-weight:700; padding:24px 12px 10px; }
    .photo-placeholder {
      background:#122338; border-radius:8px; display:flex; flex-direction:column;
      align-items:center; justify-content:center; gap:10px; color:#64748b;
      font-size:.85rem; font-weight:600; text-align:center; padding:16px;
      border:2px dashed #1e3a57; height:220px;
    }
    .photo-placeholder svg { opacity:.7; }
    .photo-split { display:grid; grid-template-columns:1fr 1fr; gap:32px; align-items:center; margin:28px 0; }
    .photo-split .photo-item { height:280px; }
    .photo-split .photo-placeholder { height:280px; }
    .photo-split-text h3 { font-size:1.15rem; font-weight:700; color:#1a2e4a; margin-bottom:8px; }
    .photo-split-text p { font-size:.97rem; color:#4b5563; line-height:1.6; }
    .photo-full { position:relative; border-radius:8px; overflow:hidden; height:260px; margin:28px 0; }
    .photo-full img { width:100%; height:100%; object-fit:cover; display:block; }
    .photo-full .photo-caption { font-size:.95rem; }
    .proof-strip-sm { background:#f97316; padding:12px 0; margin:0; }
    .proof-strip-sm .container { display:flex; flex-wrap:wrap; gap:0; justify-content:center; }
    .proof-item-sm { display:flex; align-items:center; gap:7px; color:#fff;
      font-size:.88rem; font-weight:700; padding:5px 16px;
      border-right:1px solid rgba(255,255,255,.3); }
    .proof-item-sm:last-child { border-right:none; }
    .proof-item-sm::before { content:"✓"; font-weight:900; }
    @media(max-width:640px) {
      .photo-row { grid-template-columns:1fr; }
      .photo-row-2 { grid-template-columns:1fr; }
      .photo-split { grid-template-columns:1fr; }
    }
    @media(max-width:480px){
      .proof-strip-sm .container { flex-direction:column; align-items:center; }
      .proof-item-sm { border-right:none; border-bottom:1px solid rgba(255,255,255,.2); width:100%; justify-content:center; }
      .proof-item-sm:last-child { border-bottom:none; }
    }
"""

# ── new sticky header HTML ──────────────────────────────────────────────────
def new_header(active_home=False, active_area=None):
    home_cls = ' class="active"' if active_home else ''
    areas = [
        ("Hixson, TN",        "/junk-removal-hixson-tn.html"),
        ("East Brainerd, TN", "/junk-removal-east-brainerd-tn.html"),
        ("Red Bank, TN",      "/junk-removal-red-bank-tn.html"),
        ("Ooltewah, TN",      "/junk-removal-ooltewah-tn.html"),
        ("Soddy-Daisy, TN",   "/junk-removal-soddy-daisy-tn.html"),
        ("Signal Mountain, TN","/junk-removal-signal-mountain-tn.html"),
    ]
    area_links = ""
    for label, href in areas:
        cls = ' class="active"' if active_area and active_area in label else ''
        area_links += f'      <a href="{href}"{cls}>{label}</a>\n'
    return f"""  <header>
    <div class="container">
      <a class="brand" href="/"><span style="color:#fff">Chattanooga</span> <span style="color:#f97316">Junk Removal</span></a>
      <div class="header-right">
        <a class="header-phone" href="{TEL}">{PHONE}</a>
        <a class="header-cta" href="{TEL}" style="display:inline-block;background:#f97316;color:#fff;font-weight:700;font-size:.88rem;padding:8px 14px;border-radius:5px;text-decoration:none;white-space:nowrap;">Call for a Free Quote</a>
        <button class="menu-btn" id="menuBtn" aria-label="Open menu">&#9776;</button>
      </div>
    </div>
  </header>
  <nav class="dropdown-menu" id="dropdownMenu">
    <div class="container">
      <a href="/"{"" if not active_home else ' class="active"'}>Home</a>
      <span class="menu-label">Services</span>
      <a href="/furniture-removal-chattanooga-tn.html">Furniture Removal</a>
      <a href="/appliance-removal-chattanooga-tn.html">Appliance Removal</a>
      <a href="/garage-cleanout-chattanooga-tn.html">Garage Cleanout</a>
      <a href="/yard-debris-removal-chattanooga-tn.html">Yard Debris Removal</a>
      <a href="/estate-cleanout-chattanooga-tn.html">Estate Cleanout</a>
      <span class="menu-label">Service Areas</span>
{area_links}      <span class="menu-label">Info</span>
      <a href="/junk-removal-pricing-chattanooga-tn.html">Pricing</a>
      <a href="/contact.html">Contact</a>
    </div>
  </nav>"""

# ── photo building helpers ──────────────────────────────────────────────────
CAM_SVG = '<svg width="38" height="38" viewBox="0 0 24 24" fill="none" stroke="#f97316" stroke-width="1.5"><path d="M23 19a2 2 0 0 1-2 2H3a2 2 0 0 1-2-2V8a2 2 0 0 1 2-2h4l2-3h6l2 3h4a2 2 0 0 1 2 2z"/><circle cx="12" cy="13" r="4"/></svg>'

def placeholder(label, height="220px"):
    return (
        f'<div class="photo-placeholder" style="height:{height}">'
        f'{CAM_SVG}<span>{label}</span></div>'
    )

def real_img(src, alt, caption, height="220px"):
    return (
        f'<div class="photo-item" style="height:{height}">'
        f'<img src="{src}" alt="{alt}" loading="lazy" />'
        f'<div class="photo-caption">{caption}</div></div>'
    )

# ── proof strip (small) ─────────────────────────────────────────────────────
def proof_strip(items):
    inner = "".join(f'<div class="proof-item-sm">{i}</div>' for i in items)
    return (
        '\n  <div class="proof-strip-sm">'
        '<div class="container">'
        f'{inner}'
        '</div></div>\n'
    )

# ── after-hero photo strip ──────────────────────────────────────────────────
def photo_row_3(items):
    cells = "".join(f'      {item}\n' for item in items)
    return f'\n    <div class="photo-row">\n{cells}    </div>\n'

def photo_row_2(items):
    cells = "".join(f'      {item}\n' for item in items)
    return f'\n    <div class="photo-row-2">\n{cells}    </div>\n'

def photo_split(img_html, text_html):
    return (
        f'\n    <div class="photo-split">'
        f'{img_html}'
        f'<div class="photo-split-text">{text_html}</div>'
        f'</div>\n'
    )

def photo_full(src, alt, caption):
    return (
        f'\n    <div class="photo-full">'
        f'<img src="{src}" alt="{alt}" loading="lazy" />'
        f'<div class="photo-caption">{caption}</div>'
        f'</div>\n'
    )

# ── CSS / header helpers ────────────────────────────────────────────────────
def inject_css(html):
    """Append photo CSS just before closing </style>"""
    return html.replace('  </style>', PHOTO_CSS + '  </style>', 1)

def replace_header(html, active_area=None):
    """Replace everything from <header> through </nav> (dropdown)."""
    header_block = new_header(active_area=active_area)
    html = re.sub(
        r'<header>.*?</nav>\s*',
        header_block + '\n  ',
        html, flags=re.DOTALL, count=1
    )
    return html

def make_section(content, bg=""):
    style = f' style="background:{bg};"' if bg else ''
    return f'\n  <section{style}>\n    <div class="container">\n{content}\n    </div>\n  </section>\n'

# ── insert after a section with given id ───────────────────────────────────
def insert_after_section(html, section_id, new_html):
    pattern = rf'(</section>)(\s*)(<!-- .*? -->\s*)?\s*(<section[^>]*id="{section_id}")'
    # Try inserting after closing tag of that section
    close_pat = rf'(</section>)(\s*)(?=\s*<section[^>]*id="{section_id}|<nav|<footer)'
    # Instead: find the section, find its closing tag, insert after
    idx = html.find(f'id="{section_id}"')
    if idx == -1:
        return html
    # Find the </section> after this section
    close_idx = html.find('</section>', idx)
    if close_idx == -1:
        return html
    close_end = close_idx + len('</section>')
    return html[:close_end] + '\n' + new_html + html[close_end:]

def insert_after_tag(html, tag, new_html, nth=1):
    """Insert new_html after nth occurrence of tag."""
    idx = -1
    for _ in range(nth):
        idx = html.find(tag, idx + 1)
        if idx == -1:
            return html
    pos = idx + len(tag)
    return html[:pos] + new_html + html[pos:]

# ═══════════════════════════════════════════════════════════════════════════
# PAGE BUILDERS
# ═══════════════════════════════════════════════════════════════════════════

def build_service_page(path, active_area=None, photos_spec=None):
    with open(path) as f:
        html = f.read()

    html = inject_css(html)
    html = replace_header(html, active_area=active_area)

    # 1. After hero — proof strip + photo row
    strip = proof_strip(["Same-day available", "Free estimates", "We haul it away", "7 days a week"])

    p = photos_spec or {}
    row_after_hero = '\n  <section style="padding:40px 0 8px;">\n    <div class="container">\n'
    row_after_hero += '      ' + real_img("/images/workers-loading.jpg",
        "Junk removal crew at work in Chattanooga, TN",
        "Our crew handles all the heavy lifting") + '\n'
    row_after_hero += '    </div>\n  </section>\n'

    three_row = photo_row_3([
        real_img("/images/junk-removal-truck.jpg",
                 "Junk removal truck in Chattanooga, TN", "Ready for pickup"),
        real_img("/images/workers-loading.jpg",
                 "Workers loading junk in Chattanooga", "We do all the lifting"),
        real_img("/images/junk-pile.jpg",
                 "Junk pile ready for hauling", "From small loads to full truckloads"),
    ])
    photo_section_mid = f'\n  <section style="padding:8px 0 40px;">\n    <div class="container">\n{three_row}    </div>\n  </section>\n'

    # Insert proof strip after hero section
    html = html.replace('<section id="description">', strip + '<section id="description">', 1)

    # Insert 3-photo row after description section
    html = insert_after_section(html, "description",
        f'  <section style="padding:16px 0 48px;background:#f3f7fb;">\n'
        f'    <div class="container">\n'
        f'      <p style="font-size:1rem;color:#4b5563;margin-bottom:18px;font-style:italic;">'
        f'"From single items to full cleanouts — we haul it away so you don\'t have to."</p>\n'
        + three_row +
        f'    </div>\n  </section>')

    # Insert inline photo+text split before "why choose us"
    split_html = (
        f'\n  <section style="padding:8px 0 40px;">\n    <div class="container">\n'
        f'    <div class="photo-split">\n'
        f'      {real_img("/images/junk-removal-truck.jpg", "Junk removal truck ready in Chattanooga", "Same-day and next-day availability", height="280px")}\n'
        f'      <div class="photo-split-text">'
        f'<h3>Ready When You Are</h3>'
        f'<p>Our truck is loaded and our crew is ready. Call before noon for the best shot at same-day service. We work 7 days a week across Chattanooga and Hamilton County.</p>'
        f'<p style="margin-top:12px;"><a href="{TEL}" style="color:#f97316;font-weight:700;">Call {PHONE} &rarr;</a></p>'
        f'</div>\n'
        f'    </div>\n    </div>\n  </section>\n'
    )
    html = html.replace('<section id="why-choose-us">', split_html + '<section id="why-choose-us">', 1)
    html = html.replace('<section id="why-choose-us" style="background:#f9fafb;">', split_html + '<section id="why-choose-us" style="background:#f9fafb;">', 1)

    # Insert a 2-photo row after same-day section
    two_row = photo_row_2([
        real_img("/images/junk-pile.jpg",
                 "Large junk pile before removal in Chattanooga", "Before: full load ready to go"),
        real_img("/images/workers-loading.jpg",
                 "Junk removal workers clearing debris", "After: cleared and hauled away"),
    ])
    before_after = (
        f'\n  <section style="padding:8px 0 40px;background:#f3f7fb;">\n    <div class="container">\n'
        f'      <h3 style="font-size:1rem;font-weight:700;color:#1a2e4a;margin-bottom:14px;">Real Jobs. Real Results.</h3>\n'
        + two_row +
        f'    </div>\n  </section>\n'
    )
    html = html.replace('<section id="related-services">', before_after + '<section id="related-services">', 1)
    html = html.replace('<section id="related-services" style="background:#f9fafb;">', before_after + '<section id="related-services" style="background:#f9fafb;">', 1)

    return html


def build_location_page(path, city_name, area_key=None):
    with open(path) as f:
        html = f.read()

    html = inject_css(html)
    html = replace_header(html, active_area=city_name)

    strip = proof_strip(["Same-day available", "Free estimates", f"Serving {city_name}", "7 days a week"])

    three_row = photo_row_3([
        real_img("/images/junk-removal-truck.jpg",
                 f"Junk removal truck serving {city_name}, TN",
                 f"Serving {city_name} and nearby communities"),
        real_img("/images/workers-loading.jpg",
                 f"Junk removal crew loading items near {city_name}",
                 "We do all the lifting"),
        real_img("/images/junk-pile.jpg",
                 f"Junk pile removal near {city_name}, TN",
                 "From single items to full property cleanouts"),
    ])

    # After hero → proof strip
    html = html.replace('<section id="same-day">', strip + '<section id="same-day">', 1)

    # After same-day → 3-photo row
    photo_sec = (
        f'\n  <section style="padding:8px 0 48px;background:#f3f7fb;">\n'
        f'    <div class="container">\n'
        f'      <h3 style="font-size:1rem;font-weight:700;color:#1a2e4a;margin-bottom:16px;">'
        f'See Us in Action in the {city_name} Area</h3>\n'
        + three_row +
        f'    </div>\n  </section>\n'
    )
    html = insert_after_section(html, "same-day", photo_sec)

    # Before CTA → split photo
    split = (
        f'\n  <section style="padding:8px 0 40px;">\n    <div class="container">\n'
        f'    <div class="photo-split">\n'
        f'      {real_img("/images/workers-loading.jpg", f"Junk removal workers in {city_name}, TN", "Your local junk removal crew", height="280px")}\n'
        f'      <div class="photo-split-text">'
        f'<h3>Local Crew. Fast Service.</h3>'
        f'<p>We serve {city_name} and the surrounding Chattanooga area 7 days a week. Same-day and next-day appointments available. One call gets it done.</p>'
        f'<p style="margin-top:14px;"><a href="{TEL}" style="color:#f97316;font-weight:700;font-size:1.05rem;">{PHONE}</a></p>'
        f'</div>\n'
        f'    </div>\n    </div>\n  </section>\n'
    )
    html = html.replace('<section id="contact">', split + '<section id="contact">', 1)
    html = html.replace('<section id="contact" style="background:#f9fafb;">', split + '<section id="contact" style="background:#f9fafb;">', 1)

    return html


def build_about_page(path):
    with open(path) as f:
        html = f.read()

    html = inject_css(html)
    html = replace_header(html)

    strip = proof_strip(["Locally owned", "7 days a week", "Upfront pricing", "Chattanooga area"])

    three_row = photo_row_3([
        real_img("/images/junk-removal-truck.jpg",
                 "Chattanooga Junk Removal truck ready for service",
                 "Our truck — ready for your call"),
        real_img("/images/workers-loading.jpg",
                 "Junk removal crew loading items in Chattanooga",
                 "Our crew doing the heavy lifting"),
        real_img("/images/junk-pile.jpg",
                 "Large junk haul in Chattanooga, TN",
                 "From small loads to full cleanouts"),
    ])
    photo_sec = (
        f'\n  <section style="padding:8px 0 48px;">\n'
        f'    <div class="container">\n'
        + three_row +
        f'    </div>\n  </section>\n'
    )

    html = html.replace('<section id="who-we-are">', strip + '<section id="who-we-are">', 1)
    html = insert_after_section(html, "who-we-are", photo_sec.strip())

    split = (
        f'\n  <section style="padding:8px 0 48px;background:#f3f7fb;">\n    <div class="container">\n'
        f'    <div class="photo-split">\n'
        f'      {real_img("/images/workers-loading.jpg", "Junk removal workers in Chattanooga", "Your local crew at work", height="280px")}\n'
        f'      <div class="photo-split-text">'
        f'<h3>A Real Local Crew</h3>'
        f'<p>We\'re not a call center or a franchise — we\'re a local Chattanooga operation that knows this city, works hard, and treats every job seriously. '
        f'When you call us, you reach a real person. When we show up, we do the work.</p>'
        f'<p style="margin-top:12px;"><a href="{TEL}" style="color:#f97316;font-weight:700;">{PHONE}</a></p>'
        f'</div>\n'
        f'    </div>\n    </div>\n  </section>\n'
    )
    html = html.replace('<section id="our-approach">', split + '<section id="our-approach">', 1)
    html = html.replace('<section id="our-approach" style="background:#f9fafb;">', split + '<section id="our-approach" style="background:#f9fafb;">', 1)

    return html


def build_contact_page(path):
    with open(path) as f:
        html = f.read()

    html = inject_css(html)
    html = replace_header(html)

    strip = proof_strip(["Call a real person", "Free estimate by phone", "Same-day available", "7 days a week"])

    full_photo = photo_full(
        "/images/junk-removal-truck.jpg",
        "Chattanooga Junk Removal truck ready for same day service",
        "Call us today — same-day and next-day service available across Chattanooga"
    )
    photo_cta = (
        f'\n  <section style="padding:8px 0 40px;">\n'
        f'    <div class="container">\n'
        f'{full_photo}'
        f'    </div>\n  </section>\n'
    )

    two_row = photo_row_2([
        real_img("/images/workers-loading.jpg",
                 "Junk removal workers loading a truck in Chattanooga",
                 "Your crew — ready to haul"),
        real_img("/images/junk-pile.jpg",
                 "Junk pile before removal in Chattanooga, TN",
                 "We handle all sizes of jobs"),
    ])

    html = html.replace('<section id="call-us">', strip + '<section id="call-us">', 1)
    html = insert_after_section(html, "call-us",
        f'  <section style="padding:8px 0 40px;background:#f3f7fb;">\n'
        f'    <div class="container">\n'
        + two_row +
        f'    </div>\n  </section>')

    html = html.replace('<section id="what-to-expect">', photo_cta + '<section id="what-to-expect">', 1)
    html = html.replace('<section id="what-to-expect" style="background:#f9fafb;">', photo_cta + '<section id="what-to-expect" style="background:#f9fafb;">', 1)

    return html


def build_pricing_page(path):
    with open(path) as f:
        html = f.read()

    html = inject_css(html)
    html = replace_header(html)

    strip = proof_strip(["Volume-based pricing", "No hidden fees", "Free estimates", "Upfront quotes"])

    full_photo = photo_full(
        "/images/junk-removal-truck.jpg",
        "Junk removal truck loaded for a Chattanooga job",
        "Pricing is based on truck space — the more you need removed, the larger the load"
    )
    photo_sec = (
        f'\n  <section style="padding:8px 0 40px;">\n'
        f'    <div class="container">\n'
        f'{full_photo}'
        f'    </div>\n  </section>\n'
    )

    two_row = photo_row_2([
        real_img("/images/junk-pile.jpg",
                 "Large junk pile representing a full truck load",
                 "Full truckload: largest volume, best value per item"),
        real_img("/images/workers-loading.jpg",
                 "Crew loading items — pricing by truck space in Chattanooga",
                 "You only pay for the space your load takes up"),
    ])
    two_sec = (
        f'\n  <section style="padding:8px 0 40px;background:#f3f7fb;">\n'
        f'    <div class="container">\n'
        f'      <p style="font-size:.97rem;color:#4b5563;margin-bottom:16px;">'
        f'These photos show what different load sizes look like — from a partial load to a full truck.</p>\n'
        + two_row +
        f'    </div>\n  </section>\n'
    )

    html = html.replace('<section id="how-we-price">', strip + '<section id="how-we-price">', 1)
    html = insert_after_section(html, "how-we-price", photo_sec.strip())
    html = html.replace('<section id="price-ranges">', two_sec + '<section id="price-ranges">', 1)
    html = html.replace('<section id="price-ranges" style="background:#f9fafb;">', two_sec + '<section id="price-ranges" style="background:#f9fafb;">', 1)

    return html


# ── MAIN ────────────────────────────────────────────────────────────────────
PAGES = {
    "public/furniture-removal-chattanooga-tn.html":  ("service", None),
    "public/appliance-removal-chattanooga-tn.html":  ("service", None),
    "public/garage-cleanout-chattanooga-tn.html":    ("service", None),
    "public/yard-debris-removal-chattanooga-tn.html":("service", None),
    "public/estate-cleanout-chattanooga-tn.html":    ("service", None),
    "public/junk-removal-hixson-tn.html":            ("location", "Hixson"),
    "public/junk-removal-east-brainerd-tn.html":     ("location", "East Brainerd"),
    "public/junk-removal-red-bank-tn.html":          ("location", "Red Bank"),
    "public/junk-removal-ooltewah-tn.html":          ("location", "Ooltewah"),
    "public/junk-removal-soddy-daisy-tn.html":       ("location", "Soddy-Daisy"),
    "public/junk-removal-signal-mountain-tn.html":   ("location", "Signal Mountain"),
    "public/about.html":    ("about",   None),
    "public/contact.html":  ("contact", None),
    "public/junk-removal-pricing-chattanooga-tn.html": ("pricing", None),
}

updated = []
errors  = []
for path, (kind, city) in PAGES.items():
    try:
        if kind == "service":
            html = build_service_page(path)
        elif kind == "location":
            html = build_location_page(path, city)
        elif kind == "about":
            html = build_about_page(path)
        elif kind == "contact":
            html = build_contact_page(path)
        elif kind == "pricing":
            html = build_pricing_page(path)
        with open(path, "w") as f:
            f.write(html)
        updated.append(path)
        print(f"OK  {path}")
    except Exception as e:
        errors.append((path, str(e)))
        print(f"ERR {path}: {e}")

print(f"\n{len(updated)} updated, {len(errors)} errors")

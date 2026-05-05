#!/usr/bin/env python3
"""
Replace all photo-section images on every subpage with unique,
page-specific images and SEO-optimized alt text.
Targets <img> tags inside photo-item, photo-split, photo-full, photo-placeholder,
hp-photo-box, and action-card divs — leaves hero images untouched.
"""
import re, glob, os

# ── Per-page image specs ────────────────────────────────────────────────────
# Each entry: list of (src, alt, caption) in order images appear in photo sections
# (hero image NOT included here — it stays as-is)

PAGES = {

  # ── SERVICE PAGES ──────────────────────────────────────────────────────────

  "public/furniture-removal-chattanooga-tn.html": {
    "photo_imgs": [
      # workers-split (after proof strip)
      ("/images/workers-loading.jpg",
       "Junk removal crew carrying furniture out of a Chattanooga home",
       "Our crew handles all the heavy lifting"),
      # 3-photo row
      ("/images/old-sofa-removal.jpg",
       "Old sofa ready for pickup in Chattanooga, TN",
       "Sofas, sectionals &amp; loveseats"),
      ("/images/furniture-cleanout.jpg",
       "Full furniture cleanout from a Chattanooga property",
       "We haul it all in one trip"),
      ("/images/mattress-removal.jpg",
       "Mattress removal service in Chattanooga, TN",
       "Mattresses, bed frames &amp; more"),
      # photo-split (mid-page)
      ("/images/hauling-crew.jpg",
       "Junk removal crew ready for furniture pickup in Chattanooga",
       "Ready When You Are"),
      # before/after pair
      ("/images/old-sofa-removal.jpg",
       "Old furniture piled up before removal in Chattanooga, TN",
       "Before: furniture cleared and ready"),
      ("/images/workers-loading.jpg",
       "Workers loading old furniture onto junk removal truck",
       "After: cleared and hauled away"),
    ],
  },

  "public/appliance-removal-chattanooga-tn.html": {
    "photo_imgs": [
      ("/images/hauling-crew.jpg",
       "Junk removal crew ready to haul appliances in Chattanooga, TN",
       "Our crew handles all the heavy lifting"),
      ("/images/refrigerator-removal.jpg",
       "Old refrigerator being removed from a Chattanooga home",
       "Fridges &amp; freezers"),
      ("/images/washer-dryer-removal.jpg",
       "Washer and dryer removal service in Chattanooga, TN",
       "Washers, dryers &amp; more"),
      ("/images/old-appliance-removal.jpg",
       "Old appliances ready for removal in Chattanooga",
       "All appliance types accepted"),
      ("/images/truck-loading-job.jpg",
       "Junk removal truck loaded with appliances in Chattanooga, TN",
       "Ready When You Are"),
      ("/images/old-appliance-removal.jpg",
       "Old appliances piled up before removal in Chattanooga",
       "Before: appliances cleared out"),
      ("/images/junk-removal-load.jpg",
       "Truck fully loaded after appliance removal in Chattanooga, TN",
       "After: hauled away completely"),
    ],
  },

  "public/garage-cleanout-chattanooga-tn.html": {
    "photo_imgs": [
      ("/images/hauling-crew.jpg",
       "Junk removal crew arriving for a garage cleanout in Chattanooga",
       "Our crew handles all the heavy lifting"),
      ("/images/cluttered-garage.jpg",
       "Cluttered garage before a cleanout service in Chattanooga, TN",
       "Before: packed garage"),
      ("/images/garage-cleanout-tools.jpg",
       "Garage cleanout in progress — tools and boxes being cleared",
       "We haul everything out"),
      ("/images/garage-cleanout-boxes.jpg",
       "Boxes and junk being loaded from garage cleanout in Chattanooga",
       "Boxes, tools &amp; clutter"),
      ("/images/workers-loading.jpg",
       "Workers loading garage junk onto truck in Chattanooga, TN",
       "Ready When You Are"),
      ("/images/garage-before.jpg",
       "Overfull garage before professional cleanout in Chattanooga",
       "Before: cramped and unusable"),
      ("/images/junk-removal-load.jpg",
       "Truck loaded after garage cleanout in Chattanooga, TN",
       "After: cleared out completely"),
    ],
  },

  "public/yard-debris-removal-chattanooga-tn.html": {
    "photo_imgs": [
      ("/images/hauling-crew.jpg",
       "Junk removal crew ready for yard debris pickup in Chattanooga",
       "Our crew handles all the heavy lifting"),
      ("/images/yard-debris-cleanup.jpg",
       "Yard debris cleanup service in Chattanooga, TN",
       "Yard waste &amp; storm cleanup"),
      ("/images/yard-branches-pile.jpg",
       "Tree branches and yard debris pile ready for removal in Chattanooga",
       "We load and haul it away"),
      ("/images/junk-pile.jpg",
       "Large outdoor debris pile before junk removal in Chattanooga",
       "All sizes of cleanups"),
      ("/images/junk-removal-truck.jpg",
       "Junk removal truck ready for yard debris pickup in Chattanooga, TN",
       "Ready When You Are"),
      ("/images/yard-branches-pile.jpg",
       "Tree branches and debris piled up before yard cleanup in Chattanooga",
       "Before: debris cleared"),
      ("/images/truck-loading-job.jpg",
       "Truck being loaded with yard debris in Chattanooga, TN",
       "After: yard cleared and hauled"),
    ],
  },

  "public/estate-cleanout-chattanooga-tn.html": {
    "photo_imgs": [
      ("/images/hauling-crew.jpg",
       "Junk removal crew ready for estate cleanout in Chattanooga, TN",
       "Our crew handles all the heavy lifting"),
      ("/images/house-cleanout-boxes.jpg",
       "Estate cleanout boxes and belongings being cleared in Chattanooga",
       "Full estate &amp; property cleanouts"),
      ("/images/estate-cleanout-room.jpg",
       "Estate cleanout in progress — room being cleared in Chattanooga",
       "We clear it room by room"),
      ("/images/cleanout-before.jpg",
       "Cluttered estate property before cleanout in Chattanooga, TN",
       "Residential &amp; rental properties"),
      ("/images/workers-loading.jpg",
       "Workers loading estate cleanout items onto truck in Chattanooga",
       "Ready When You Are"),
      ("/images/house-cleanout-boxes.jpg",
       "Boxes and furniture piled up before estate cleanout",
       "Before: full property cleared"),
      ("/images/truck-loading-job.jpg",
       "Truck loaded after estate cleanout service in Chattanooga, TN",
       "After: ready for next chapter"),
    ],
  },

  # ── LOCATION PAGES ─────────────────────────────────────────────────────────

  "public/junk-removal-hixson-tn.html": {
    "photo_imgs": [
      # 3-photo row
      ("/images/residential-neighborhood.jpg",
       "Residential neighborhood in Hixson, TN served by junk removal",
       "Serving Hixson and nearby communities"),
      ("/images/workers-loading.jpg",
       "Junk removal workers loading items near Hixson, TN",
       "We do all the lifting"),
      ("/images/junk-removal-truck.jpg",
       "Junk removal truck serving Hixson, TN residents",
       "From single items to full cleanouts"),
      # photo-split
      ("/images/hauling-crew.jpg",
       "Local junk removal crew serving Hixson, TN homeowners",
       "Your local Hixson crew"),
    ],
  },

  "public/junk-removal-east-brainerd-tn.html": {
    "photo_imgs": [
      ("/images/local-home.jpg",
       "East Brainerd, TN home served by local junk removal company",
       "Serving East Brainerd residents"),
      ("/images/hauling-crew.jpg",
       "Junk removal crew loading a truck in East Brainerd, TN",
       "We do all the lifting"),
      ("/images/junk-removal-load.jpg",
       "Junk removal truck fully loaded in East Brainerd, TN",
       "Same-day pickups available"),
      ("/images/workers-loading.jpg",
       "Workers loading junk removal truck near East Brainerd, TN",
       "Your local East Brainerd crew"),
    ],
  },

  "public/junk-removal-red-bank-tn.html": {
    "photo_imgs": [
      ("/images/chattanooga-residential.jpg",
       "Residential street in Red Bank, TN near Chattanooga",
       "Serving Red Bank homeowners"),
      ("/images/workers-loading.jpg",
       "Junk removal crew working in Red Bank, TN",
       "We do all the lifting"),
      ("/images/truck-loading-job.jpg",
       "Junk removal truck loaded up in Red Bank, TN",
       "From single items to full cleanouts"),
      ("/images/hauling-crew.jpg",
       "Local junk removal crew serving Red Bank, TN",
       "Your local Red Bank crew"),
    ],
  },

  "public/junk-removal-ooltewah-tn.html": {
    "photo_imgs": [
      ("/images/local-home.jpg",
       "Ooltewah, TN home serviced by local junk removal",
       "Serving Ooltewah residents"),
      ("/images/junk-removal-truck.jpg",
       "Junk removal truck serving Ooltewah, TN community",
       "We do all the lifting"),
      ("/images/cleanout-before.jpg",
       "Property cleanout in progress near Ooltewah, TN",
       "From small loads to full cleanouts"),
      ("/images/workers-loading.jpg",
       "Junk removal workers in Ooltewah, TN area",
       "Your local Ooltewah crew"),
    ],
  },

  "public/junk-removal-soddy-daisy-tn.html": {
    "photo_imgs": [
      ("/images/residential-neighborhood.jpg",
       "Soddy-Daisy, TN neighborhood served by local junk removal",
       "Serving Soddy-Daisy residents"),
      ("/images/junk-removal-load.jpg",
       "Junk removal truck loaded in Soddy-Daisy, TN",
       "We do all the lifting"),
      ("/images/workers-loading.jpg",
       "Junk removal crew at work in Soddy-Daisy, TN",
       "Same-day pickups available"),
      ("/images/hauling-crew.jpg",
       "Local crew serving Soddy-Daisy, TN and surrounding area",
       "Your local Soddy-Daisy crew"),
    ],
  },

  "public/junk-removal-signal-mountain-tn.html": {
    "photo_imgs": [
      ("/images/chattanooga-residential.jpg",
       "Signal Mountain, TN area home served by junk removal",
       "Serving Signal Mountain residents"),
      ("/images/truck-loading-job.jpg",
       "Junk removal truck making a Signal Mountain, TN pickup",
       "We do all the lifting"),
      ("/images/junk-pile.jpg",
       "Junk removal job completed on Signal Mountain, TN",
       "From single items to full cleanouts"),
      ("/images/workers-loading.jpg",
       "Junk removal workers serving Signal Mountain, TN area",
       "Your local Signal Mountain crew"),
    ],
  },

  # ── INFO PAGES ─────────────────────────────────────────────────────────────

  "public/about.html": {
    "photo_imgs": [
      ("/images/junk-removal-truck.jpg",
       "Chattanooga Junk Removal truck ready for service in Hamilton County",
       "Our truck — ready for your call"),
      ("/images/workers-loading.jpg",
       "Local junk removal crew doing the heavy lifting in Chattanooga",
       "Our crew doing the heavy lifting"),
      ("/images/junk-pile.jpg",
       "Large junk haul completed by Chattanooga Junk Removal",
       "From small loads to full cleanouts"),
      ("/images/hauling-crew.jpg",
       "Chattanooga Junk Removal crew loading a truck for local customers",
       "A Real Local Crew"),
    ],
  },

  "public/contact.html": {
    "photo_imgs": [
      ("/images/workers-loading.jpg",
       "Chattanooga junk removal crew ready for your call",
       "Your crew — ready to haul"),
      ("/images/junk-pile.jpg",
       "Junk pile at a Chattanooga property ready for pickup",
       "We handle all sizes of jobs"),
      ("/images/truck-loading-job.jpg",
       "Junk removal truck loaded and ready for service in Chattanooga, TN",
       "Call today — same-day and next-day service available across Chattanooga"),
    ],
  },

  "public/junk-removal-pricing-chattanooga-tn.html": {
    "photo_imgs": [
      ("/images/junk-removal-truck.jpg",
       "Junk removal truck representing pricing by volume in Chattanooga, TN",
       "Pricing is based on truck space — the more you need removed, the larger the load"),
      ("/images/junk-pile.jpg",
       "Large junk pile representing a full truck load in Chattanooga",
       "Full truckload: largest volume, best value per item"),
      ("/images/hauling-crew.jpg",
       "Crew loading junk — pricing by truck space in Chattanooga, TN",
       "You only pay for the space your load takes up"),
    ],
  },
}


def replace_photo_imgs(html, img_specs):
    """
    Find all <img> tags that are inside photo-item, photo-full,
    photo-split, hp-photo-box, action-card or photo-placeholder divs,
    and replace them in order with the provided specs.
    Skips hero images (keeps first <img> in .hero section untouched).
    """
    # Split off everything before </section> after the hero to avoid touching hero img
    hero_end = html.find('</section>', html.find('class="hero"'))
    if hero_end == -1:
        hero_end = 0
    prefix = html[:hero_end + len('</section>')]
    body   = html[hero_end + len('</section>'):]

    # Find all <img> tags in body that are within our photo containers
    img_pattern = re.compile(
        r'(<img\s[^>]*?src=")(/images/[^"]+)("[^>]*?alt=")([^"]*?)("[^>]*?/>)',
        re.DOTALL
    )

    idx = [0]
    def replacer(m):
        if idx[0] >= len(img_specs):
            return m.group(0)
        src, alt, _ = img_specs[idx[0]]
        idx[0] += 1
        return m.group(1) + src + m.group(3) + alt + m.group(5)

    new_body = img_pattern.sub(replacer, body)
    return prefix + new_body


def update_captions(html, img_specs):
    """Update photo-caption and hp-photo-cap divs to match the image specs."""
    # Find all caption divs in the photo sections (after hero)
    hero_end = html.find('</section>', html.find('class="hero"'))
    if hero_end == -1:
        hero_end = 0
    prefix = html[:hero_end + len('</section>')]
    body   = html[hero_end + len('</section>'):]

    cap_pattern = re.compile(
        r'(<div class="(?:photo-caption|hp-photo-cap)"[^>]*>)([^<]*)(</div>)',
        re.DOTALL
    )

    idx = [0]
    def cap_replacer(m):
        if idx[0] >= len(img_specs):
            return m.group(0)
        _, _, cap = img_specs[idx[0]]
        idx[0] += 1
        return m.group(1) + cap + m.group(3)

    new_body = cap_pattern.sub(cap_replacer, body)
    return prefix + new_body


updated, errors = [], []

for path, spec in PAGES.items():
    try:
        with open(path) as f:
            html = f.read()

        img_specs = spec["photo_imgs"]
        html = replace_photo_imgs(html, img_specs)
        html = update_captions(html, img_specs)

        with open(path, "w") as f:
            f.write(html)

        updated.append(path)
        print(f"OK  {path} — {len(img_specs)} images")
    except Exception as e:
        errors.append((path, str(e)))
        print(f"ERR {path}: {e}")

print(f"\n{len(updated)} updated, {len(errors)} errors")

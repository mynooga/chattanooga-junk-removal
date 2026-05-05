#!/usr/bin/env python3
"""
Generate 20 new city/location SEO pages for Fast Chattanooga Junk Removal.
Each page is fully unique with local references, 600-900 words of body copy,
proper internal linking, and consistent design matching existing pages.
"""
import os

BASE_URL = "https://fastchattanoogajunkremoval.com"
PHONE_DISPLAY = "(423) 556-3473"
PHONE_TEL = "tel:+14235563473"

# ── Page definitions ─────────────────────────────────────────────────────────
# Each dict: slug, city, state, title, meta_desc, hero_p, proof_items (4),
#   main_h2, main_body (list of <p> strings),
#   remove_items (list of strings),
#   why_items (list of {head, body}),
#   service_area_body (list of <p>),
#   related_p (str), related_links (list of {href, label}),
#   split_img, split_img_alt, split_img_cap, split_text_h3, split_text_p,
#   contact_h2, contact_p,
#   nearby_pages (list of {href, label}),  -- for nav bar + footer
#   service_links (list of {href, label}),  -- 2-3 service links
#   nearby_city_links (list of {href, label}),  -- 2-3 nearby city links
#   footer_area_label (str),
#   photo_imgs: [(src, alt, cap), ...] — 3 photo row images

PAGES = [

  # ─── 1. Harrison, TN ───────────────────────────────────────────────────────
  dict(
    slug="junk-removal-harrison-tn",
    city="Harrison", state="TN",
    title="Junk Removal Harrison TN | Same-Day Haul-Away Service",
    meta="Junk removal in Harrison, TN — near Lake Chickamauga and Highway 58. We haul furniture, garage clutter, yard debris & more. Same-day often available. Call for a free quote!",
    hero_p="Harrison sits right along Lake Chickamauga, and between the lake-area homes, seasonal properties, and the busy Highway 58 corridor, junk has a way of piling up fast. Whether you're clearing out a garage, dealing with outdoor debris after a storm, or just doing a long-overdue cleanout, we can be there quickly — same-day pickups often available for calls before noon.",
    hero_btn="Call Now for Same-Day Pickup in Harrison",
    proof_items=["Same-day available", "Free estimates", "Serving Harrison TN", "7 days a week"],
    main_h2="Local Junk Removal Serving Harrison, TN",
    main_body=[
      "Harrison is a relaxed lake-side community, but lake homes come with their own brand of clutter — watercraft accessories, old dock furniture, outdoor equipment, and garages stuffed with gear from a dozen different seasons. We haul it all.",
      "The Highway 58 corridor has grown significantly in recent years, and with more households comes more junk. Whether you've just moved into a Harrison home and inherited the previous owner's leftovers, or you're finally clearing out the garage you've been avoiding, our crew handles the heavy lifting from start to finish.",
      "We serve Harrison as part of our regular Hamilton County routes. Give us a call, describe what you need gone, and we'll give you a straight price before we start. No surprise charges, no pressure.",
      "Same-day and next-day availability means you don't have to plan weeks ahead. Just call when you're ready and we'll work around your schedule.",
    ],
    remove_items=["Old furniture & sofas","Appliances","Mattresses","Yard waste & debris","Garage clutter","Electronics & TVs","Outdoor equipment","Construction debris","Moving leftovers","Estate cleanouts","Hot tubs","And much more"],
    why_items=[
      {"head":"Fast Scheduling for Harrison Jobs","body":"We route through the Harrison area regularly and can often get there the same day you call, especially for morning calls."},
      {"head":"No-Surprise Pricing","body":"You'll get a firm price before we touch a thing. What we quote is what you pay."},
      {"head":"We Handle It All","body":"From hauling individual pieces out of a lake house to clearing an entire garage, our crew does the lifting, loading, and cleanup."},
      {"head":"Responsible Disposal","body":"We separate out items that can be donated or recycled rather than sending everything straight to the landfill."},
    ],
    service_area_body=[
      "We serve all of Harrison, TN including neighborhoods near Lake Chickamauga, Harrison Bay State Park, the Highway 58 corridor, and surrounding Harrison Pike areas.",
      "We also cover nearby communities including Ooltewah, East Brainerd, and Birchwood. If you're unsure whether we reach your address, just call — we'll let you know right away.",
      'Harrison residents most often call us for <a href="/garage-cleanout-chattanooga-tn.html" style="color:#1a2e4a;font-weight:600;">garage cleanouts</a>, <a href="/yard-debris-removal-chattanooga-tn.html" style="color:#1a2e4a;font-weight:600;">yard debris removal</a>, and <a href="/furniture-removal-chattanooga-tn.html" style="color:#1a2e4a;font-weight:600;">furniture haul-away</a>. We can combine services in a single trip to save you time.',
    ],
    related_p='Need a specific service? We handle <a href="/furniture-removal-chattanooga-tn.html" style="color:#1a2e4a;font-weight:600;">furniture removal</a> and <a href="/garage-cleanout-chattanooga-tn.html" style="color:#1a2e4a;font-weight:600;">garage cleanouts</a> throughout the Harrison area. We also serve nearby <a href="/junk-removal-ooltewah-tn.html" style="color:#1a2e4a;font-weight:600;">Ooltewah</a> and <a href="/junk-removal-east-brainerd-tn.html" style="color:#1a2e4a;font-weight:600;">East Brainerd</a>.',
    related_links=[
      ("/furniture-removal-chattanooga-tn.html","Furniture Removal"),
      ("/garage-cleanout-chattanooga-tn.html","Garage Cleanout"),
      ("/yard-debris-removal-chattanooga-tn.html","Yard Debris Removal"),
      ("/junk-removal-ooltewah-tn.html","Ooltewah, TN"),
      ("/junk-removal-pricing-chattanooga-tn.html","Pricing Guide"),
    ],
    split_img="/images/hauling-crew.jpg",
    split_img_alt="Junk removal crew serving Harrison, TN lake-area homes",
    split_img_cap="Serving Harrison and the Lake Chickamauga area",
    split_text_h3="Lake-Area Homes, Handled",
    split_text_p="From seasonal property cleanouts to year-round garage haul-aways, we serve Harrison homeowners 7 days a week. Same-day and next-day slots available.",
    contact_h2="Ready to Clear Out Your Harrison Property?",
    contact_p="Give us a call for fast, friendly junk removal in Harrison, TN. Free quote, no obligation.",
    nearby_pages=[
      ("/junk-removal-ooltewah-tn.html","Ooltewah, TN"),
      ("/junk-removal-east-brainerd-tn.html","East Brainerd, TN"),
      ("/junk-removal-soddy-daisy-tn.html","Soddy-Daisy, TN"),
    ],
    footer_area_label="Harrison, TN",
    photo_imgs=[
      ("/images/residential-neighborhood.jpg","Lake-area residential neighborhood in Harrison, TN","Serving Harrison lakeside homes"),
      ("/images/garage-cleanout-boxes.jpg","Garage cleanout in progress near Harrison, TN","We clear out garages completely"),
      ("/images/yard-debris-cleanup.jpg","Yard debris cleanup service in Harrison, TN","Outdoor and seasonal debris removal"),
    ],
  ),

  # ─── 2. Cleveland, TN ──────────────────────────────────────────────────────
  dict(
    slug="junk-removal-cleveland-tn",
    city="Cleveland", state="TN",
    title="Junk Removal Cleveland TN | Fast Haul-Away Service",
    meta="Junk removal in Cleveland, TN — fast, affordable pickup for homes, apartments, and rentals in Bradley County. Same-day often available. Call for a free quote!",
    hero_p="Cleveland is one of the larger communities in our service area, and with that comes plenty of variety — suburban homes off Keith Street, apartments near Lee University, older neighborhoods downtown, and everything in between. Whatever you need hauled, we can come to you fast. Same-day appointments are often available.",
    hero_btn="Call Now for Same-Day Junk Removal in Cleveland",
    proof_items=["Same-day available","Free estimates","Serving Cleveland TN","7 days a week"],
    main_h2="Junk Removal for Cleveland, TN Homes & Rentals",
    main_body=[
      "Cleveland sits at the crossroads of Bradley and McMinn counties and has grown steadily over the past decade. With that growth comes more residential turnover — and more junk removal calls. Whether you're a homeowner doing a long-overdue cleanout, a landlord prepping a rental unit, or a resident just trying to reclaim some space, we're the crew to call.",
      "We handle single-item pickups all the way up to full property cleanouts. Got an old refrigerator sitting on the porch? We'll grab it. Clearing out an apartment between tenants? We can haul out all the leftover furniture, appliances, and miscellaneous debris in one trip.",
      "Our pricing is based on how much space your load takes up in the truck. You'll get a quote before we start — no hidden fees, no add-ons at the end. Just load it and go.",
      "We serve Cleveland and the surrounding Bradley County area regularly, so getting on the schedule is usually quick. Call us in the morning and we can often be there the same day.",
    ],
    remove_items=["Old furniture & sofas","Appliances","Mattresses","Rental move-out debris","Electronics & TVs","Yard waste","Garage clutter","Construction debris","Estate cleanouts","Office furniture","Clothing & boxes","And much more"],
    why_items=[
      {"head":"Familiar with the Cleveland Market","body":"We serve Cleveland and Bradley County regularly. Apartments, houses, rentals — we've seen it all and can handle any volume."},
      {"head":"Straight Pricing Before We Start","body":"No confusing quotes. We look at the load, name a price, and you decide. Simple as that."},
      {"head":"Fast Turnaround","body":"Same-day and next-day availability means you're not waiting around for weeks. Call and we'll find a time that works."},
      {"head":"We Do All the Heavy Work","body":"You don't lift a thing. Our crew carries everything out, loads the truck, and sweeps up when we're done."},
    ],
    service_area_body=[
      "We cover all of Cleveland, TN including areas near Keith Street, 25th Street NW, Westside Drive, Lee University, the Ocoee Street corridor, and surrounding Bradley County neighborhoods.",
      "We also regularly serve nearby Charleston, Dayton, and Harrison. If you're on the edge of our coverage area, just call and we'll confirm.",
      'Cleveland customers commonly book us for <a href="/appliance-removal-chattanooga-tn.html" style="color:#1a2e4a;font-weight:600;">appliance removal</a>, <a href="/furniture-removal-chattanooga-tn.html" style="color:#1a2e4a;font-weight:600;">furniture haul-away</a>, and full <a href="/estate-cleanout-chattanooga-tn.html" style="color:#1a2e4a;font-weight:600;">estate cleanouts</a>.',
    ],
    related_p='We provide <a href="/appliance-removal-chattanooga-tn.html" style="color:#1a2e4a;font-weight:600;">appliance removal</a> and <a href="/furniture-removal-chattanooga-tn.html" style="color:#1a2e4a;font-weight:600;">furniture pickup</a> throughout Cleveland. We also serve nearby <a href="/junk-removal-charleston-tn.html" style="color:#1a2e4a;font-weight:600;">Charleston</a> and <a href="/junk-removal-dayton-tn.html" style="color:#1a2e4a;font-weight:600;">Dayton</a>.',
    related_links=[
      ("/furniture-removal-chattanooga-tn.html","Furniture Removal"),
      ("/appliance-removal-chattanooga-tn.html","Appliance Removal"),
      ("/estate-cleanout-chattanooga-tn.html","Estate Cleanout"),
      ("/junk-removal-charleston-tn.html","Charleston, TN"),
      ("/junk-removal-pricing-chattanooga-tn.html","Pricing Guide"),
    ],
    split_img="/images/workers-loading.jpg",
    split_img_alt="Junk removal crew loading a truck in Cleveland, TN",
    split_img_cap="Your Cleveland crew — ready to haul",
    split_text_h3="Cleveland's Go-To Junk Haulers",
    split_text_p="Homes, apartments, rentals, garages — we handle cleanouts of all types across Cleveland and Bradley County. Call for fast, no-pressure service any day of the week.",
    contact_h2="Ready to Schedule Your Cleveland Junk Removal?",
    contact_p="Call us for fast, affordable junk removal anywhere in Cleveland, TN. We'll give you a free quote and can often get there the same day.",
    nearby_pages=[
      ("/junk-removal-charleston-tn.html","Charleston, TN"),
      ("/junk-removal-dayton-tn.html","Dayton, TN"),
      ("/junk-removal-harrison-tn.html","Harrison, TN"),
    ],
    footer_area_label="Cleveland, TN",
    photo_imgs=[
      ("/images/local-home.jpg","Residential home in Cleveland, TN ready for junk removal","Serving homes across Bradley County"),
      ("/images/old-appliance-removal.jpg","Appliance removal service in Cleveland, TN","Appliances, furniture & more"),
      ("/images/house-cleanout-boxes.jpg","Move-out cleanout boxes being cleared in Cleveland, TN","Full rental and estate cleanouts"),
    ],
  ),

  # ─── 3. Collegedale, TN ────────────────────────────────────────────────────
  dict(
    slug="junk-removal-collegedale-tn",
    city="Collegedale", state="TN",
    title="Junk Removal Collegedale TN | Same-Day Pickup Service",
    meta="Junk removal in Collegedale, TN — serving homes, student housing, and garages near Southern Adventist University. Same-day often available. Free quote, call now!",
    hero_p="Collegedale is a tight-knit suburban community southeast of Chattanooga, and between the growing neighborhoods off Apison Pike, student housing near Southern Adventist University, and the steady influx of new families, junk removal is a frequent need. We serve the Collegedale area fast — same-day pickups often available.",
    hero_btn="Call Now for Same-Day Junk Removal in Collegedale",
    proof_items=["Same-day available","Free estimates","Serving Collegedale TN","7 days a week"],
    main_h2="Junk Removal for Collegedale Homes & Neighborhoods",
    main_body=[
      "Collegedale has developed quickly over the past several years. New subdivisions, updated homes, and a growing rental market all mean that stuff accumulates — and eventually needs to go somewhere. That's where we come in.",
      "Whether you're clearing out a garage in one of the Cambridge Square-area neighborhoods, doing a move-out cleanout near campus, or hauling away old furniture from a home you're renovating, we take it all. Our crew arrives, assesses the load, quotes you a price, and gets to work.",
      "We're used to working in residential neighborhoods where space is tight. We'll protect your driveway, yard, and walls on the way out. Everything goes straight onto the truck.",
      "Calling before noon usually means we can fit you in the same day. Weekends and early morning slots are available too.",
    ],
    remove_items=["Old furniture","Appliances","Mattresses","Student move-out items","Garage clutter","Electronics","Yard debris","Construction leftovers","Estate items","Boxes & clothing","Hot tubs","And much more"],
    why_items=[
      {"head":"Familiar with Collegedale Neighborhoods","body":"We work in these neighborhoods regularly. Tight driveways and busy streets aren't a problem for our crew."},
      {"head":"Clear Pricing Upfront","body":"We quote before we lift. You know the price before we take a single item off your hands."},
      {"head":"We Handle the Lifting","body":"You point to what needs to go. We carry it out, load the truck, and do a final sweep. Done."},
      {"head":"We Try to Divert from Landfills","body":"Usable items get donated when possible. We'd rather see a good piece of furniture find a new home than go to waste."},
    ],
    service_area_body=[
      "We serve all of Collegedale including areas near Apison Pike, Collegedale Road, the Southern Adventist University campus neighborhood, and surrounding Hamilton County communities.",
      "We also cover nearby Ooltewah, Apison, and East Brainerd. Not sure if we cover your address? Give us a call.",
      'Common requests from Collegedale include <a href="/furniture-removal-chattanooga-tn.html" style="color:#1a2e4a;font-weight:600;">furniture removal</a>, <a href="/garage-cleanout-chattanooga-tn.html" style="color:#1a2e4a;font-weight:600;">garage cleanouts</a>, and <a href="/appliance-removal-chattanooga-tn.html" style="color:#1a2e4a;font-weight:600;">appliance haul-away</a> — often in combination.',
    ],
    related_p='We offer <a href="/furniture-removal-chattanooga-tn.html" style="color:#1a2e4a;font-weight:600;">furniture removal</a> and <a href="/garage-cleanout-chattanooga-tn.html" style="color:#1a2e4a;font-weight:600;">garage cleanouts</a> across Collegedale. We also serve <a href="/junk-removal-ooltewah-tn.html" style="color:#1a2e4a;font-weight:600;">Ooltewah</a> and <a href="/junk-removal-apison-tn.html" style="color:#1a2e4a;font-weight:600;">Apison</a>.',
    related_links=[
      ("/furniture-removal-chattanooga-tn.html","Furniture Removal"),
      ("/garage-cleanout-chattanooga-tn.html","Garage Cleanout"),
      ("/appliance-removal-chattanooga-tn.html","Appliance Removal"),
      ("/junk-removal-ooltewah-tn.html","Ooltewah, TN"),
      ("/junk-removal-apison-tn.html","Apison, TN"),
    ],
    split_img="/images/residential-neighborhood.jpg",
    split_img_alt="Residential neighborhood in Collegedale, TN served by junk removal",
    split_img_cap="Serving Collegedale's growing neighborhoods",
    split_text_h3="Suburban Cleanouts Made Easy",
    split_text_p="From garage clutter to student move-outs, we keep Collegedale neighborhoods clean and clutter-free. Same-day and next-day appointments available 7 days a week.",
    contact_h2="Ready to Clear Out in Collegedale?",
    contact_p="Call for fast junk removal anywhere in Collegedale, TN. Free quote, no pressure.",
    nearby_pages=[
      ("/junk-removal-ooltewah-tn.html","Ooltewah, TN"),
      ("/junk-removal-apison-tn.html","Apison, TN"),
      ("/junk-removal-east-brainerd-tn.html","East Brainerd, TN"),
    ],
    footer_area_label="Collegedale, TN",
    photo_imgs=[
      ("/images/chattanooga-residential.jpg","Suburban home in Collegedale, TN served by junk removal","Serving Collegedale residential neighborhoods"),
      ("/images/furniture-cleanout.jpg","Furniture being cleared from a Collegedale home","Furniture and move-out cleanouts"),
      ("/images/garage-cleanout-boxes.jpg","Garage cleanout underway in Collegedale, TN","Garage clutter taken care of"),
    ],
  ),

  # ─── 4. Ringgold, GA ───────────────────────────────────────────────────────
  dict(
    slug="junk-removal-ringgold-ga",
    city="Ringgold", state="GA",
    title="Junk Removal Ringgold GA | Same-Day North Georgia Haul-Away",
    meta="Junk removal in Ringgold, GA — fast haul-away for Catoosa County homes, rentals, and businesses. Same-day often available. Free quote from Fast Chattanooga Junk Removal!",
    hero_p="Ringgold sits just across the Georgia state line in Catoosa County, and we make the trip regularly. Whether you're clearing out a home on Tiger Drive, handling a move-out on the US-41 corridor, or tackling accumulated clutter from a small business, our crew can be there quickly — same-day pickups often available for morning calls.",
    hero_btn="Call Now for Same-Day Junk Removal in Ringgold",
    proof_items=["Same-day available","Free estimates","Serving Ringgold GA","7 days a week"],
    main_h2="Junk Removal for Ringgold & Catoosa County",
    main_body=[
      "Ringgold is a practical, working community with a mix of established neighborhoods and newer developments. A lot of homeowners here deal with the same thing: furniture that's been sitting in a spare room for years, garages that gradually became storage units, and appliances that finally gave out but are too heavy to move alone.",
      "We serve Ringgold as part of our regular routes into North Georgia. The process is simple — call us, tell us what needs to go, and we'll give you a price. If the price works for you, we schedule a time and our crew takes care of everything else.",
      "Move-out cleanouts are common in Ringgold, especially for rental properties along US-41 and the surrounding neighborhoods. Landlords call us to clear out everything left behind so they can turn units around fast. We handle it efficiently and leave the space clean.",
      "We're also available for small business cleanouts — storage areas, back-office clutter, old equipment. If it fits on a truck, we'll take it.",
    ],
    remove_items=["Old furniture","Appliances","Mattresses","Move-out debris","Electronics","Yard waste","Garage clutter","Business equipment","Estate items","Construction debris","Storage cleanouts","And much more"],
    why_items=[
      {"head":"We Cross the State Line","body":"Ringgold and Catoosa County are part of our regular service area. No extra fees for the Georgia trip."},
      {"head":"Pricing You'll Understand","body":"We quote based on truck space. You see the load, we name the price. Simple and transparent."},
      {"head":"Fast Scheduling","body":"Same-day and next-day availability means you're not stuck waiting. Morning calls usually get same-day slots."},
      {"head":"We Clear It and Go","body":"Our crew loads everything, sweeps up, and leaves. You don't have to do a thing except show us what to take."},
    ],
    service_area_body=[
      "We serve all of Ringgold and Catoosa County including areas along US-41, Tiger Drive, Battlefield Parkway, and the surrounding residential communities.",
      "We also serve nearby Rossville, Fort Oglethorpe, and East Ridge. Call us if you're not sure whether we cover your specific address.",
      'Common requests from Ringgold include <a href="/furniture-removal-chattanooga-tn.html" style="color:#1a2e4a;font-weight:600;">furniture haul-away</a>, <a href="/estate-cleanout-chattanooga-tn.html" style="color:#1a2e4a;font-weight:600;">estate cleanouts</a>, and <a href="/appliance-removal-chattanooga-tn.html" style="color:#1a2e4a;font-weight:600;">appliance disposal</a>.',
    ],
    related_p='We handle <a href="/estate-cleanout-chattanooga-tn.html" style="color:#1a2e4a;font-weight:600;">estate cleanouts</a> and <a href="/furniture-removal-chattanooga-tn.html" style="color:#1a2e4a;font-weight:600;">furniture removal</a> in Ringgold. We also serve <a href="/junk-removal-rossville-ga.html" style="color:#1a2e4a;font-weight:600;">Rossville</a> and <a href="/junk-removal-fort-oglethorpe-ga.html" style="color:#1a2e4a;font-weight:600;">Fort Oglethorpe</a>.',
    related_links=[
      ("/furniture-removal-chattanooga-tn.html","Furniture Removal"),
      ("/estate-cleanout-chattanooga-tn.html","Estate Cleanout"),
      ("/appliance-removal-chattanooga-tn.html","Appliance Removal"),
      ("/junk-removal-rossville-ga.html","Rossville, GA"),
      ("/junk-removal-fort-oglethorpe-ga.html","Fort Oglethorpe, GA"),
    ],
    split_img="/images/truck-loading-job.jpg",
    split_img_alt="Junk removal truck loaded for pickup in Ringgold, GA",
    split_img_cap="Serving Ringgold and Catoosa County",
    split_text_h3="North Georgia. No Problem.",
    split_text_p="We cross the state line regularly to serve Ringgold and surrounding Catoosa County communities. Same-day and next-day slots available, 7 days a week.",
    contact_h2="Ready to Clear Out in Ringgold, GA?",
    contact_p="Call for fast, no-hassle junk removal in Ringgold and Catoosa County. Free quote, no obligation.",
    nearby_pages=[
      ("/junk-removal-rossville-ga.html","Rossville, GA"),
      ("/junk-removal-fort-oglethorpe-ga.html","Fort Oglethorpe, GA"),
      ("/junk-removal-east-ridge-tn.html","East Ridge, TN"),
    ],
    footer_area_label="Ringgold, GA",
    photo_imgs=[
      ("/images/local-home.jpg","Home in Ringgold, GA ready for junk removal","Serving Ringgold and Catoosa County"),
      ("/images/workers-loading.jpg","Junk removal workers hauling items in Ringgold, GA","We do all the heavy lifting"),
      ("/images/estate-cleanout-room.jpg","Estate cleanout in progress near Ringgold, GA","Move-out and estate cleanouts"),
    ],
  ),

  # ─── 5. Fort Oglethorpe, GA ────────────────────────────────────────────────
  dict(
    slug="junk-removal-fort-oglethorpe-ga",
    city="Fort Oglethorpe", state="GA",
    title="Junk Removal Fort Oglethorpe GA | Fast Haul-Away Service",
    meta="Junk removal in Fort Oglethorpe, GA — homes, businesses & rental cleanouts near Battlefield Parkway. Same-day often available. Free quote, call now!",
    hero_p="Fort Oglethorpe is a busy corridor community along Battlefield Parkway, with a mix of homes, retail properties, and rental units that all eventually need a cleanout. Our crew serves Fort Oglethorpe and the surrounding Catoosa County area regularly — same-day pickups often available.",
    hero_btn="Call Now for Same-Day Junk Removal in Fort Oglethorpe",
    proof_items=["Same-day available","Free estimates","Serving Fort Oglethorpe GA","7 days a week"],
    main_h2="Serving Fort Oglethorpe Homes & Businesses",
    main_body=[
      "Fort Oglethorpe is a community that's always moving. The Battlefield Parkway corridor sees a steady flow of residential and commercial activity, and with that comes regular calls for junk removal — from homeowners clearing out extra rooms, landlords turning over rental units, and small businesses hauling out old inventory and equipment.",
      "We handle all of it. Whether it's a single couch or a full property cleanout, our crew shows up, loads the truck, and clears out. You don't need to sort, bag, or haul anything to the curb. Just show us what needs to go.",
      "Properties along LaFayette Road and the surrounding neighborhoods often deal with older furniture and appliances. We pick up everything from refrigerators and washers to bedroom sets and garage junk — all in one trip when possible.",
      "Call before noon and we can usually get a crew out the same day. Weekend availability is common as well.",
    ],
    remove_items=["Old furniture","Appliances","Mattresses","Business equipment","Rental cleanout debris","Electronics","Yard waste","Garage clutter","Construction debris","Estate items","Storage unit cleanouts","And much more"],
    why_items=[
      {"head":"Regular Route Through Fort Oglethorpe","body":"We're in the area regularly, which means faster scheduling and no extra fees for the North Georgia trip."},
      {"head":"Works for Homes and Businesses","body":"Whether it's a residential cleanout or a commercial space, we handle both without fuss."},
      {"head":"Upfront Price, No Surprises","body":"We assess the load and give you a firm quote before we start. What we say is what you pay."},
      {"head":"We Do the Work","body":"Your job is to show us what's going. Our job is to get it off your property."},
    ],
    service_area_body=[
      "We serve all of Fort Oglethorpe including areas near Battlefield Parkway, LaFayette Road, Chickamauga Avenue, and the surrounding residential and commercial neighborhoods.",
      "We also regularly serve Ringgold, Rossville, and Chickamauga, GA. Call to confirm coverage for your address.",
      'Fort Oglethorpe customers commonly book us for <a href="/appliance-removal-chattanooga-tn.html" style="color:#1a2e4a;font-weight:600;">appliance removal</a>, <a href="/furniture-removal-chattanooga-tn.html" style="color:#1a2e4a;font-weight:600;">furniture haul-away</a>, and full <a href="/estate-cleanout-chattanooga-tn.html" style="color:#1a2e4a;font-weight:600;">property cleanouts</a>.',
    ],
    related_p='We offer <a href="/appliance-removal-chattanooga-tn.html" style="color:#1a2e4a;font-weight:600;">appliance removal</a> and <a href="/estate-cleanout-chattanooga-tn.html" style="color:#1a2e4a;font-weight:600;">estate cleanouts</a> in Fort Oglethorpe. We also serve <a href="/junk-removal-ringgold-ga.html" style="color:#1a2e4a;font-weight:600;">Ringgold</a> and <a href="/junk-removal-rossville-ga.html" style="color:#1a2e4a;font-weight:600;">Rossville</a>.',
    related_links=[
      ("/appliance-removal-chattanooga-tn.html","Appliance Removal"),
      ("/furniture-removal-chattanooga-tn.html","Furniture Removal"),
      ("/estate-cleanout-chattanooga-tn.html","Estate Cleanout"),
      ("/junk-removal-ringgold-ga.html","Ringgold, GA"),
      ("/junk-removal-rossville-ga.html","Rossville, GA"),
    ],
    split_img="/images/junk-removal-load.jpg",
    split_img_alt="Junk removal truck loaded and ready in Fort Oglethorpe, GA",
    split_img_cap="Fast service in Fort Oglethorpe and Catoosa County",
    split_text_h3="Fast Pickups Along the Battlefield Corridor",
    split_text_p="From Battlefield Parkway homes to LaFayette Road businesses, we serve Fort Oglethorpe quickly and without hassle. 7 days a week, same-day often available.",
    contact_h2="Ready to Book Junk Removal in Fort Oglethorpe?",
    contact_p="Call for a free quote and fast scheduling anywhere in Fort Oglethorpe, GA. No pressure, no hidden fees.",
    nearby_pages=[
      ("/junk-removal-ringgold-ga.html","Ringgold, GA"),
      ("/junk-removal-rossville-ga.html","Rossville, GA"),
      ("/junk-removal-chickamauga-ga.html","Chickamauga, GA"),
    ],
    footer_area_label="Fort Oglethorpe, GA",
    photo_imgs=[
      ("/images/hauling-crew.jpg","Junk removal crew serving Fort Oglethorpe, GA","Serving Catoosa County communities"),
      ("/images/old-appliance-removal.jpg","Appliance removal service in Fort Oglethorpe, GA","Appliances picked up same day"),
      ("/images/cleanout-before.jpg","Property cleanout before and after in Fort Oglethorpe area","Rental and estate cleanouts"),
    ],
  ),

  # ─── 6. Rossville, GA ──────────────────────────────────────────────────────
  dict(
    slug="junk-removal-rossville-ga",
    city="Rossville", state="GA",
    title="Junk Removal Rossville GA | Same-Day Pickup Near Chattanooga",
    meta="Junk removal in Rossville, GA — fast haul-away for older homes and rentals near the TN state line. Same-day often available. Free quote from Fast Chattanooga Junk Removal!",
    hero_p="Rossville is right on the Tennessee-Georgia line, and we serve it as naturally as we serve Chattanooga itself. Whether you're in one of the older McFarland Avenue neighborhoods, clearing out a rental near the state line, or just need a truck to come pick up a few bulky items, we can usually be there the same day.",
    hero_btn="Call Now for Same-Day Pickup in Rossville",
    proof_items=["Same-day available","Free estimates","Serving Rossville GA","7 days a week"],
    main_h2="Fast Junk Removal for Rossville, GA",
    main_body=[
      "Rossville has a large stock of older homes, and older homes mean older stuff — furniture from multiple generations, appliances that finally gave out, and garages that have become more storage than parking. We hear it constantly: 'I've been meaning to clear this out for years.' We make that finally happen.",
      "Rental properties are common in Rossville, and we work with landlords regularly to clear out units between tenants. A quick, efficient cleanout means you can get the unit back on the market faster. We can often come within a day or two — sometimes same-day if you call early.",
      "We charge by the amount of truck space your load takes up. We quote you a price before we touch anything, and that price is what you pay. No itemized fees or end-of-job add-ons.",
      "McFarland Avenue, Chickamauga Avenue, and the streets running off them are familiar territory for us. We've done cleanouts in this part of town regularly and know what to expect.",
    ],
    remove_items=["Old furniture","Appliances","Mattresses","Rental debris","Electronics","Yard waste","Garage clutter","Construction leftovers","Estate cleanouts","Clothing & boxes","Moving leftovers","And much more"],
    why_items=[
      {"head":"Close to Chattanooga — Fast Response","body":"Rossville is practically next door. We can often get a crew there the same morning you call."},
      {"head":"Great for Older Homes","body":"We've cleared out homes with decades of accumulated stuff. We work efficiently without judgment."},
      {"head":"Transparent Pricing","body":"Price is based on how much of the truck you fill. We quote it upfront. Simple."},
      {"head":"We Do It All","body":"From carrying furniture down stairs to sweeping out a garage, our crew handles every step."},
    ],
    service_area_body=[
      "We serve all of Rossville, GA including neighborhoods near McFarland Avenue, Chickamauga Avenue, Cloud Springs Road, and the surrounding areas near the Tennessee line.",
      "We also cover nearby East Ridge, Fort Oglethorpe, and Ringgold. Just call us if you're not sure.",
      'Rossville residents most often call us for <a href="/furniture-removal-chattanooga-tn.html" style="color:#1a2e4a;font-weight:600;">furniture removal</a>, <a href="/appliance-removal-chattanooga-tn.html" style="color:#1a2e4a;font-weight:600;">appliance pickup</a>, and full <a href="/estate-cleanout-chattanooga-tn.html" style="color:#1a2e4a;font-weight:600;">home cleanouts</a>.',
    ],
    related_p='We handle <a href="/furniture-removal-chattanooga-tn.html" style="color:#1a2e4a;font-weight:600;">furniture removal</a> and <a href="/appliance-removal-chattanooga-tn.html" style="color:#1a2e4a;font-weight:600;">appliance disposal</a> in Rossville. We also serve <a href="/junk-removal-east-ridge-tn.html" style="color:#1a2e4a;font-weight:600;">East Ridge</a> and <a href="/junk-removal-fort-oglethorpe-ga.html" style="color:#1a2e4a;font-weight:600;">Fort Oglethorpe</a>.',
    related_links=[
      ("/furniture-removal-chattanooga-tn.html","Furniture Removal"),
      ("/appliance-removal-chattanooga-tn.html","Appliance Removal"),
      ("/estate-cleanout-chattanooga-tn.html","Estate Cleanout"),
      ("/junk-removal-east-ridge-tn.html","East Ridge, TN"),
      ("/junk-removal-fort-oglethorpe-ga.html","Fort Oglethorpe, GA"),
    ],
    split_img="/images/junk-removal-truck.jpg",
    split_img_alt="Junk removal truck serving Rossville, GA near Chattanooga",
    split_img_cap="Quick pickups in Rossville and surrounding areas",
    split_text_h3="Right Across the State Line",
    split_text_p="Rossville is part of our everyday service area. Same-day and next-day service available. One call and we handle the rest.",
    contact_h2="Need Junk Removed in Rossville, GA?",
    contact_p="Call for a free, no-pressure quote. We serve Rossville and surrounding communities 7 days a week.",
    nearby_pages=[
      ("/junk-removal-east-ridge-tn.html","East Ridge, TN"),
      ("/junk-removal-fort-oglethorpe-ga.html","Fort Oglethorpe, GA"),
      ("/junk-removal-ringgold-ga.html","Ringgold, GA"),
    ],
    footer_area_label="Rossville, GA",
    photo_imgs=[
      ("/images/chattanooga-residential.jpg","Older residential neighborhood in Rossville, GA near Chattanooga","Serving Rossville homes and rentals"),
      ("/images/workers-loading.jpg","Junk removal workers clearing a Rossville, GA property","Fast, professional service"),
      ("/images/furniture-cleanout.jpg","Furniture cleanout in progress near Rossville, GA","Old furniture hauled away"),
    ],
  ),

  # ─── 7. Lookout Mountain, TN ───────────────────────────────────────────────
  dict(
    slug="junk-removal-lookout-mountain-tn",
    city="Lookout Mountain", state="TN",
    title="Junk Removal Lookout Mountain TN | Hauling Mountain Homes",
    meta="Junk removal in Lookout Mountain, TN — we handle steep driveways, mountain homes, and large property cleanouts. Same-day often available. Free quote, call now!",
    hero_p="Lookout Mountain presents its own set of challenges for junk removal — steep driveways, narrow roads, and homes perched on terrain that can make hauling tricky. We've done it before. Our crew is used to mountain property work, and we bring the right equipment and muscle for the job.",
    hero_btn="Call Now for Same-Day Junk Removal on Lookout Mountain",
    proof_items=["Same-day available","Free estimates","Serving Lookout Mountain TN","7 days a week"],
    main_h2="Junk Removal Built for Lookout Mountain Properties",
    main_body=[
      "Homes on Lookout Mountain tend to be older and larger, with more accumulated belongings and less convenient truck access than flat-ground properties. We've cleared out carports at the top of steep driveways, hauled furniture up and down narrow stairways, and navigated roads that can be tricky even for passenger vehicles.",
      "If you're clearing out a house along Scenic Highway or up off Lookout Mountain Parkway, give us a call. We'll talk through the logistics, come out to see the scope if needed, and give you a fair price before we start anything.",
      "Mountain homes are also common for estate cleanouts — properties that have been in a family for decades and need a thorough, careful clearance. We work efficiently and respectfully, keeping reusable and valuable items separate as we go.",
      "Availability is typically good — same-day and next-day slots open up frequently, and we serve Lookout Mountain regularly as part of our Chattanooga-area routes.",
    ],
    remove_items=["Old furniture","Appliances","Mattresses","Estate items","Garage & carport clutter","Electronics","Yard waste & debris","Construction materials","Hot tubs","Moving leftovers","Large bulk items","And much more"],
    why_items=[
      {"head":"Experienced with Difficult Access","body":"Steep driveways, tight turns, heavy items — we've handled it. Mountain properties don't intimidate us."},
      {"head":"Careful Crew","body":"We take care not to damage floors, walls, and landscaping on the way out. Your property matters to us."},
      {"head":"Honest, Upfront Pricing","body":"We assess the job and give you a real price before we start. No surprises when the truck is full."},
      {"head":"We Handle Every Step","body":"Carrying, loading, and cleanup — all of it. You don't lift a thing."},
    ],
    service_area_body=[
      "We serve properties across Lookout Mountain, TN including areas along Scenic Highway, Lookout Mountain Parkway, and the surrounding mountain residential communities.",
      "We also serve nearby Signal Mountain, Chattanooga, and East Ridge. Mountain properties may require a site assessment before quoting — just call and we'll discuss.",
      'Common requests from Lookout Mountain include <a href="/furniture-removal-chattanooga-tn.html" style="color:#1a2e4a;font-weight:600;">furniture removal</a>, <a href="/estate-cleanout-chattanooga-tn.html" style="color:#1a2e4a;font-weight:600;">estate cleanouts</a>, and <a href="/garage-cleanout-chattanooga-tn.html" style="color:#1a2e4a;font-weight:600;">garage and carport cleanouts</a>.',
    ],
    related_p='We handle <a href="/estate-cleanout-chattanooga-tn.html" style="color:#1a2e4a;font-weight:600;">estate cleanouts</a> and <a href="/furniture-removal-chattanooga-tn.html" style="color:#1a2e4a;font-weight:600;">furniture removal</a> on Lookout Mountain. We also serve <a href="/junk-removal-signal-mountain-tn.html" style="color:#1a2e4a;font-weight:600;">Signal Mountain</a> and <a href="/junk-removal-east-ridge-tn.html" style="color:#1a2e4a;font-weight:600;">East Ridge</a>.',
    related_links=[
      ("/estate-cleanout-chattanooga-tn.html","Estate Cleanout"),
      ("/furniture-removal-chattanooga-tn.html","Furniture Removal"),
      ("/garage-cleanout-chattanooga-tn.html","Garage Cleanout"),
      ("/junk-removal-signal-mountain-tn.html","Signal Mountain, TN"),
      ("/junk-removal-east-ridge-tn.html","East Ridge, TN"),
    ],
    split_img="/images/hauling-crew.jpg",
    split_img_alt="Junk removal crew ready for a Lookout Mountain, TN property cleanout",
    split_img_cap="Built for mountain property work",
    split_text_h3="We Come Up the Mountain",
    split_text_p="Steep driveways and difficult access don't stop us. We've hauled from mountain properties all over the Chattanooga area. Call and let's talk through your job.",
    contact_h2="Ready to Clear Out Your Lookout Mountain Property?",
    contact_p="Call for a no-pressure quote. We handle mountain homes, estates, and large cleanouts with care.",
    nearby_pages=[
      ("/junk-removal-signal-mountain-tn.html","Signal Mountain, TN"),
      ("/junk-removal-east-ridge-tn.html","East Ridge, TN"),
      ("/junk-removal-rossville-ga.html","Rossville, GA"),
    ],
    footer_area_label="Lookout Mountain, TN",
    photo_imgs=[
      ("/images/estate-cleanout-room.jpg","Estate cleanout in a large Lookout Mountain, TN home","Full estate and mountain home cleanouts"),
      ("/images/house-cleanout-boxes.jpg","Large property cleanout near Lookout Mountain, TN","Big hauls handled with care"),
      ("/images/workers-loading.jpg","Crew loading a junk removal truck on Lookout Mountain, TN","We handle the heavy lifting"),
    ],
  ),

  # ─── 8. East Ridge, TN ─────────────────────────────────────────────────────
  dict(
    slug="junk-removal-east-ridge-tn",
    city="East Ridge", state="TN",
    title="Junk Removal East Ridge TN | Same-Day Haul-Away Service",
    meta="Junk removal in East Ridge, TN — fast pickup for apartments, rental properties, and older homes near Ringgold Road. Same-day often available. Free quote!",
    hero_p="East Ridge sits right on the edge of Chattanooga and has a dense mix of older homes, apartment complexes, and rental properties along Ringgold Road and Battlefield Parkway. Whether you're a tenant clearing out, a landlord flipping a unit, or a homeowner reclaiming space, our crew can be there fast.",
    hero_btn="Call Now for Same-Day Junk Removal in East Ridge",
    proof_items=["Same-day available","Free estimates","Serving East Ridge TN","7 days a week"],
    main_h2="Junk Removal for East Ridge Homes & Rentals",
    main_body=[
      "East Ridge is one of the busiest residential communities in Hamilton County, with a high density of rental units and older homes that see frequent turnover. That turnover drives a lot of junk removal calls — furniture and appliances left behind, garages packed with years of clutter, and move-out cleanouts that need to happen quickly.",
      "We serve East Ridge regularly and can often get there the same day you call. Morning calls before noon are the best bet for same-day slots, but we do our best to work around your schedule even on shorter notice.",
      "Our pricing is based on how much truck space you need. You'll see the estimate before we start — no surprises at the end. We can handle single large items like sofas or refrigerators or we can clear out an entire rental unit in one pass.",
      "The Ringgold Road corridor and areas off Battlefield Parkway are familiar to us. Tight parking, shared driveways, older structures — we deal with all of it without making it your problem.",
    ],
    remove_items=["Old furniture","Appliances","Mattresses","Rental move-out debris","Electronics","Yard waste","Garage clutter","Construction materials","Estate items","Clothing & boxes","Moving leftovers","And much more"],
    why_items=[
      {"head":"Built for High-Turnover Rentals","body":"East Ridge has a lot of rental activity. We help landlords turn units quickly with efficient, professional cleanouts."},
      {"head":"Pricing Before We Touch Anything","body":"You know the price before the first item moves. That's just how we work."},
      {"head":"Fast Response Times","body":"East Ridge is on our regular route. Same-day and next-day availability is common."},
      {"head":"We Handle the Full Job","body":"Carrying out, loading up, and sweeping up — all included. Your only job is to let us in."},
    ],
    service_area_body=[
      "We serve all of East Ridge, TN including areas along Ringgold Road, Battlefield Parkway, Spring Creek Road, and the surrounding residential communities.",
      "We also cover nearby Rossville, Ringgold, and Chattanooga. If you're unsure whether we cover your address, just call.",
      'East Ridge customers commonly book us for <a href="/furniture-removal-chattanooga-tn.html" style="color:#1a2e4a;font-weight:600;">furniture removal</a>, <a href="/appliance-removal-chattanooga-tn.html" style="color:#1a2e4a;font-weight:600;">appliance pickup</a>, and full <a href="/estate-cleanout-chattanooga-tn.html" style="color:#1a2e4a;font-weight:600;">property cleanouts</a>.',
    ],
    related_p='We handle <a href="/furniture-removal-chattanooga-tn.html" style="color:#1a2e4a;font-weight:600;">furniture removal</a> and <a href="/appliance-removal-chattanooga-tn.html" style="color:#1a2e4a;font-weight:600;">appliance disposal</a> in East Ridge. We also serve <a href="/junk-removal-rossville-ga.html" style="color:#1a2e4a;font-weight:600;">Rossville</a> and <a href="/junk-removal-ringgold-ga.html" style="color:#1a2e4a;font-weight:600;">Ringgold</a>.',
    related_links=[
      ("/furniture-removal-chattanooga-tn.html","Furniture Removal"),
      ("/appliance-removal-chattanooga-tn.html","Appliance Removal"),
      ("/estate-cleanout-chattanooga-tn.html","Estate Cleanout"),
      ("/junk-removal-rossville-ga.html","Rossville, GA"),
      ("/junk-removal-ringgold-ga.html","Ringgold, GA"),
    ],
    split_img="/images/workers-loading.jpg",
    split_img_alt="Junk removal workers clearing a rental property in East Ridge, TN",
    split_img_cap="Fast rental cleanouts in East Ridge",
    split_text_h3="Quick Cleanouts for East Ridge Rentals",
    split_text_p="High-turnover rentals need fast, reliable removal. We serve East Ridge with same-day and next-day appointments, 7 days a week.",
    contact_h2="Ready to Clear Out in East Ridge, TN?",
    contact_p="Call for a free quote. We specialize in fast rental and residential cleanouts across East Ridge.",
    nearby_pages=[
      ("/junk-removal-rossville-ga.html","Rossville, GA"),
      ("/junk-removal-ringgold-ga.html","Ringgold, GA"),
      ("/junk-removal-lookout-mountain-tn.html","Lookout Mountain, TN"),
    ],
    footer_area_label="East Ridge, TN",
    photo_imgs=[
      ("/images/residential-neighborhood.jpg","Older residential neighborhood in East Ridge, TN","Serving East Ridge homes and rentals"),
      ("/images/old-sofa-removal.jpg","Old sofa removed from East Ridge, TN rental property","Furniture picked up fast"),
      ("/images/refrigerator-removal.jpg","Refrigerator removed from East Ridge, TN apartment","Appliances and bulk items removed"),
    ],
  ),

  # ─── 9. Middle Valley, TN ──────────────────────────────────────────────────
  dict(
    slug="junk-removal-middle-valley-tn",
    city="Middle Valley", state="TN",
    title="Junk Removal Middle Valley TN | Same-Day Haul-Away Service",
    meta="Junk removal in Middle Valley, TN — serving suburban homes and garages off Middle Valley Road and Harrison Pike. Same-day often available. Free quote!",
    hero_p="Middle Valley is a growing suburban area in unincorporated Hamilton County, with neighborhoods stretching along Middle Valley Road and Harrison Pike. It's a quiet, residential community — and a regular stop on our junk removal routes. Whether it's garage clutter, old furniture, or yard debris, we can usually be there the same day.",
    hero_btn="Call Now for Same-Day Junk Removal in Middle Valley",
    proof_items=["Same-day available","Free estimates","Serving Middle Valley TN","7 days a week"],
    main_h2="Serving Middle Valley Neighborhoods",
    main_body=[
      "Middle Valley sits between Hixson and Red Bank, surrounded by established residential neighborhoods and newer subdivisions. A lot of homeowners here have been in their homes long enough that the garage has quietly become unusable — filled with furniture, tools, old appliances, and boxes from moves that never got fully unpacked.",
      "We handle garage cleanouts, single-item pickups, and everything in between. Call us, tell us what you've got, and we'll give you a price. If it works for you, we schedule a time and take care of the rest.",
      "Middle Valley Road, Harrison Pike, and the surrounding streets are familiar to our crew. We work efficiently in established neighborhoods and take care not to block traffic or disturb neighbors.",
      "Same-day slots are often available, especially for morning calls. We also work weekends, so if that's when you have time, that's when we'll come.",
    ],
    remove_items=["Old furniture","Appliances","Mattresses","Garage clutter","Electronics","Yard waste & debris","Construction materials","Hot tubs","Moving leftovers","Estate items","Office furniture","And much more"],
    why_items=[
      {"head":"Local Route Through Middle Valley","body":"We pass through the area regularly, which means fast scheduling and no travel fees."},
      {"head":"Upfront Pricing Always","body":"We quote before we start. No end-of-job surprises."},
      {"head":"Efficient in Residential Areas","body":"We work carefully in neighborhoods — protecting your driveway, yard, and home on the way out."},
      {"head":"Full-Service Hauling","body":"We carry everything out and load the truck ourselves. You don't have to move a thing to the curb."},
    ],
    service_area_body=[
      "We serve all of Middle Valley, TN including neighborhoods along Middle Valley Road, Harrison Pike, Thrasher Pike, and the surrounding Hamilton County communities.",
      "We also regularly serve nearby Hixson, Red Bank, and Soddy-Daisy. Call to confirm coverage for your street.",
      'Middle Valley residents commonly book us for <a href="/garage-cleanout-chattanooga-tn.html" style="color:#1a2e4a;font-weight:600;">garage cleanouts</a>, <a href="/furniture-removal-chattanooga-tn.html" style="color:#1a2e4a;font-weight:600;">furniture removal</a>, and <a href="/yard-debris-removal-chattanooga-tn.html" style="color:#1a2e4a;font-weight:600;">yard debris pickup</a>.',
    ],
    related_p='We offer <a href="/garage-cleanout-chattanooga-tn.html" style="color:#1a2e4a;font-weight:600;">garage cleanouts</a> and <a href="/furniture-removal-chattanooga-tn.html" style="color:#1a2e4a;font-weight:600;">furniture removal</a> in Middle Valley. We also serve <a href="/junk-removal-hixson-tn.html" style="color:#1a2e4a;font-weight:600;">Hixson</a> and <a href="/junk-removal-red-bank-tn.html" style="color:#1a2e4a;font-weight:600;">Red Bank</a>.',
    related_links=[
      ("/garage-cleanout-chattanooga-tn.html","Garage Cleanout"),
      ("/furniture-removal-chattanooga-tn.html","Furniture Removal"),
      ("/yard-debris-removal-chattanooga-tn.html","Yard Debris Removal"),
      ("/junk-removal-hixson-tn.html","Hixson, TN"),
      ("/junk-removal-red-bank-tn.html","Red Bank, TN"),
    ],
    split_img="/images/garage-before.jpg",
    split_img_alt="Cluttered garage in Middle Valley, TN before cleanout",
    split_img_cap="Garages cleared out completely",
    split_text_h3="Reclaim Your Garage in Middle Valley",
    split_text_p="Garage cleanouts are one of our specialties. We carry everything out, load the truck, and leave the space clean. Same-day availability most days.",
    contact_h2="Ready to Clear Out in Middle Valley, TN?",
    contact_p="Call for a free, no-obligation quote. We serve Middle Valley and surrounding Hamilton County 7 days a week.",
    nearby_pages=[
      ("/junk-removal-hixson-tn.html","Hixson, TN"),
      ("/junk-removal-red-bank-tn.html","Red Bank, TN"),
      ("/junk-removal-soddy-daisy-tn.html","Soddy-Daisy, TN"),
    ],
    footer_area_label="Middle Valley, TN",
    photo_imgs=[
      ("/images/cluttered-garage.jpg","Cluttered garage in Middle Valley, TN ready for cleanout","Garage cleanouts are our specialty"),
      ("/images/garage-cleanout-tools.jpg","Tools and clutter being removed from Middle Valley garage","We clear everything out"),
      ("/images/residential-neighborhood.jpg","Suburban neighborhood in Middle Valley, TN","Serving Middle Valley homeowners"),
    ],
  ),

  # ─── 10. Lakesite, TN ──────────────────────────────────────────────────────
  dict(
    slug="junk-removal-lakesite-tn",
    city="Lakesite", state="TN",
    title="Junk Removal Lakesite TN | Lake Home & Seasonal Cleanup",
    meta="Junk removal in Lakesite, TN — lake home cleanouts, outdoor debris, and seasonal property cleanup on Lake Chickamauga. Same-day often available. Call for a free quote!",
    hero_p="Lakesite is a small community right on the shores of Lake Chickamauga, and lake homes tend to accumulate a specific kind of clutter — outdoor furniture, watercraft gear, old dock equipment, and seasonal items that stack up over years. We serve Lakesite and surrounding lake-area communities, with same-day pickups often available.",
    hero_btn="Call Now for Same-Day Junk Removal in Lakesite",
    proof_items=["Same-day available","Free estimates","Serving Lakesite TN","7 days a week"],
    main_h2="Lake Home Junk Removal in Lakesite, TN",
    main_body=[
      "Lake properties are wonderful until it's time to clear one out. Decades of seasonal use means weathered outdoor furniture, rusted equipment, broken watercraft accessories, and garages packed with everything that 'might come in handy someday.' We've done this kind of work many times and know what to expect.",
      "Seasonal cleanouts are a common call from Lakesite — either at the start of the season to clear out winter clutter, or at the end to haul away things that finally need to go. We handle outdoor items, garage contents, and indoor furniture in a single trip whenever possible.",
      "Lakesite is a small community, but we're in the area regularly because of our Soddy-Daisy and Birchwood routes. That means fast scheduling and no long waits.",
      "We charge based on truck space — the more you have, the larger the load, the more it costs, but you get a specific price before we do anything. Call with a description of what you've got and we'll give you a range right over the phone.",
    ],
    remove_items=["Outdoor furniture","Old dock equipment","Boat accessories","Garage contents","Appliances","Furniture","Yard debris & branches","Electronics","Construction materials","Hot tubs","Moving leftovers","And much more"],
    why_items=[
      {"head":"Familiar with Lake Property Work","body":"We've cleared out lake homes many times. We know how to handle outdoor items and difficult access points near the waterfront."},
      {"head":"In the Area Regularly","body":"We route through Lakesite and the surrounding area often, which means faster scheduling."},
      {"head":"Price Before We Start","body":"Know your cost before we lift a single item. No end-of-job surprises."},
      {"head":"We Handle the Heavy Stuff","body":"Dock furniture, old watercraft equipment, heavy appliances — our crew handles it all."},
    ],
    service_area_body=[
      "We serve Lakesite, TN and surrounding lake-area communities along Lake Chickamauga, including areas near Lakesite Drive and the surrounding waterfront neighborhoods.",
      "We also serve nearby Soddy-Daisy, Birchwood, and Harrison. If you're a seasonal property owner, we can work around your visit schedule.",
      'Lakesite customers often book us for <a href="/yard-debris-removal-chattanooga-tn.html" style="color:#1a2e4a;font-weight:600;">outdoor debris removal</a>, <a href="/garage-cleanout-chattanooga-tn.html" style="color:#1a2e4a;font-weight:600;">garage and storage cleanouts</a>, and <a href="/furniture-removal-chattanooga-tn.html" style="color:#1a2e4a;font-weight:600;">furniture haul-away</a>.',
    ],
    related_p='We handle <a href="/yard-debris-removal-chattanooga-tn.html" style="color:#1a2e4a;font-weight:600;">outdoor debris removal</a> and <a href="/garage-cleanout-chattanooga-tn.html" style="color:#1a2e4a;font-weight:600;">garage cleanouts</a> in Lakesite. We also serve <a href="/junk-removal-soddy-daisy-tn.html" style="color:#1a2e4a;font-weight:600;">Soddy-Daisy</a> and <a href="/junk-removal-birchwood-tn.html" style="color:#1a2e4a;font-weight:600;">Birchwood</a>.',
    related_links=[
      ("/yard-debris-removal-chattanooga-tn.html","Yard & Outdoor Debris Removal"),
      ("/garage-cleanout-chattanooga-tn.html","Garage Cleanout"),
      ("/furniture-removal-chattanooga-tn.html","Furniture Removal"),
      ("/junk-removal-soddy-daisy-tn.html","Soddy-Daisy, TN"),
      ("/junk-removal-birchwood-tn.html","Birchwood, TN"),
    ],
    split_img="/images/yard-debris-cleanup.jpg",
    split_img_alt="Outdoor debris cleanup at a Lakesite, TN lake property",
    split_img_cap="Lake property cleanouts — indoor and outdoor",
    split_text_h3="Lake Property Cleanouts Done Right",
    split_text_p="Seasonal or year-round, we serve Lakesite properties with fast, thorough haul-away service. Same-day and next-day slots available.",
    contact_h2="Ready to Clear Out Your Lakesite Property?",
    contact_p="Call for a free quote on lake home and seasonal property cleanouts in Lakesite, TN.",
    nearby_pages=[
      ("/junk-removal-soddy-daisy-tn.html","Soddy-Daisy, TN"),
      ("/junk-removal-birchwood-tn.html","Birchwood, TN"),
      ("/junk-removal-harrison-tn.html","Harrison, TN"),
    ],
    footer_area_label="Lakesite, TN",
    photo_imgs=[
      ("/images/yard-branches-pile.jpg","Outdoor debris pile at a Lakesite, TN lake property","Outdoor and seasonal debris removal"),
      ("/images/garage-cleanout-boxes.jpg","Lake home garage cleanout near Lakesite, TN","Garages and storage cleared out"),
      ("/images/junk-removal-load.jpg","Junk removal truck loaded after Lakesite, TN cleanout","Full loads hauled in one trip"),
    ],
  ),

  # ─── 11. Birchwood, TN ─────────────────────────────────────────────────────
  dict(
    slug="junk-removal-birchwood-tn",
    city="Birchwood", state="TN",
    title="Junk Removal Birchwood TN | Rural Property & Barn Cleanouts",
    meta="Junk removal in Birchwood, TN — rural properties, barns, sheds, and outdoor debris removal. Same-day often available. Free quote from Fast Chattanooga Junk Removal!",
    hero_p="Birchwood is a rural community in Hamilton County where properties tend to be bigger — and the amount of accumulated junk tends to match. Old barns, sheds stuffed with tools and equipment, overgrown outdoor areas, and farmhouses full of years of belongings are common calls for us in the Birchwood area.",
    hero_btn="Call Now for Same-Day Junk Removal in Birchwood",
    proof_items=["Same-day available","Free estimates","Serving Birchwood TN","7 days a week"],
    main_h2="Rural Property Cleanouts in Birchwood, TN",
    main_body=[
      "Rural properties are different from suburban cleanouts. The loads are bigger, the access is sometimes tricky, and the items can range from household furniture to large outdoor equipment. We're built for this kind of work. We bring the right trucks, the right crew, and the right attitude to get it done.",
      "Barns and sheds are a particularly common call from Birchwood. Decades of farm equipment, tools, old machinery, and odds and ends can fill a large structure quickly. We load everything that needs to go and haul it in one or more trips depending on the volume.",
      "We also handle outdoor debris — fallen trees, brush piles, construction waste, and yard cleanup from large rural lots. If it needs to go and you need help moving it, we're the crew for the job.",
      "Birchwood sits near the Rhea-Hamilton county line and we serve the area as part of our northern Hamilton County routes. Same-day availability is common for morning calls.",
    ],
    remove_items=["Barn & shed contents","Old farm equipment","Outdoor furniture","Appliances","Furniture","Mattresses","Yard debris & brush","Construction materials","Electronics","Estate cleanout items","Hot tubs","And much more"],
    why_items=[
      {"head":"Built for Rural Properties","body":"We bring the equipment and crew size needed for large rural lots, barns, sheds, and outbuildings."},
      {"head":"Multiple Trip Capacity","body":"For very large cleanouts, we make multiple runs. We'll give you a per-load price so you know exactly what it costs."},
      {"head":"Transparent Pricing","body":"Quote before we start. Always."},
      {"head":"We Handle the Heavy Stuff","body":"Old equipment, heavy appliances, large furniture — our crew carries it out so you don't have to."},
    ],
    service_area_body=[
      "We serve Birchwood, TN and surrounding rural Hamilton County, including areas near Birchwood Road and the Rhea County line.",
      "We also regularly serve nearby Soddy-Daisy, Sale Creek, and Lakesite. Rural addresses are fine — just give us a general description of access when you call.",
      'Birchwood customers frequently book us for <a href="/yard-debris-removal-chattanooga-tn.html" style="color:#1a2e4a;font-weight:600;">outdoor debris removal</a>, <a href="/garage-cleanout-chattanooga-tn.html" style="color:#1a2e4a;font-weight:600;">barn and shed cleanouts</a>, and <a href="/estate-cleanout-chattanooga-tn.html" style="color:#1a2e4a;font-weight:600;">rural estate cleanouts</a>.',
    ],
    related_p='We handle <a href="/yard-debris-removal-chattanooga-tn.html" style="color:#1a2e4a;font-weight:600;">outdoor debris removal</a> and <a href="/estate-cleanout-chattanooga-tn.html" style="color:#1a2e4a;font-weight:600;">estate cleanouts</a> in Birchwood. We also serve <a href="/junk-removal-soddy-daisy-tn.html" style="color:#1a2e4a;font-weight:600;">Soddy-Daisy</a> and <a href="/junk-removal-sale-creek-tn.html" style="color:#1a2e4a;font-weight:600;">Sale Creek</a>.',
    related_links=[
      ("/yard-debris-removal-chattanooga-tn.html","Yard & Outdoor Debris Removal"),
      ("/garage-cleanout-chattanooga-tn.html","Barn & Shed Cleanout"),
      ("/estate-cleanout-chattanooga-tn.html","Estate Cleanout"),
      ("/junk-removal-soddy-daisy-tn.html","Soddy-Daisy, TN"),
      ("/junk-removal-sale-creek-tn.html","Sale Creek, TN"),
    ],
    split_img="/images/junk-pile.jpg",
    split_img_alt="Large outdoor debris pile at a Birchwood, TN rural property",
    split_img_cap="Rural cleanouts — any size load",
    split_text_h3="Built for Big Rural Cleanouts",
    split_text_p="Birchwood properties often have years of accumulated items. We bring the crew and trucks to handle it all. Same-day and next-day availability.",
    contact_h2="Ready to Clear Out Your Birchwood Property?",
    contact_p="Call for a free quote on rural property, barn, and outdoor cleanouts in Birchwood, TN.",
    nearby_pages=[
      ("/junk-removal-soddy-daisy-tn.html","Soddy-Daisy, TN"),
      ("/junk-removal-sale-creek-tn.html","Sale Creek, TN"),
      ("/junk-removal-lakesite-tn.html","Lakesite, TN"),
    ],
    footer_area_label="Birchwood, TN",
    photo_imgs=[
      ("/images/yard-branches-pile.jpg","Outdoor debris pile at a Birchwood, TN rural property","Rural outdoor debris cleared fast"),
      ("/images/cleanout-before.jpg","Cluttered rural property before cleanout near Birchwood, TN","Before: accumulated junk removed"),
      ("/images/junk-removal-truck.jpg","Junk removal truck serving rural Birchwood, TN","We haul it all away"),
    ],
  ),

  # ─── 12. Apison, TN ────────────────────────────────────────────────────────
  dict(
    slug="junk-removal-apison-tn",
    city="Apison", state="TN",
    title="Junk Removal Apison TN | Serving Growing Southeast Chattanooga",
    meta="Junk removal in Apison, TN — fast haul-away for new and established homes in one of Chattanooga's fastest-growing communities. Same-day often available. Free quote!",
    hero_p="Apison is one of the fastest-growing communities in the Chattanooga metro area. New neighborhoods are popping up off Apison Pike regularly, and with that growth comes the full range of junk removal needs — from garage overflows in new homes to cleanouts in older properties being renovated for resale.",
    hero_btn="Call Now for Same-Day Junk Removal in Apison",
    proof_items=["Same-day available","Free estimates","Serving Apison TN","7 days a week"],
    main_h2="Junk Removal for Apison's Growing Community",
    main_body=[
      "Apison has changed a lot in recent years. Where there used to be farmland, there are now subdivisions, and with new homes come renovations, upgrades, and the eventual need to move out the old stuff. Whether it's furniture from a previous owner, appliances being replaced, or a garage that filled up during a busy move, we're here to help.",
      "New construction and home improvement projects generate a lot of debris — old cabinets, flooring, drywall scraps, and mixed household items. We haul construction debris along with standard household junk, often in a single visit.",
      "We also serve longer-established Apison homes that are doing overdue cleanouts. Every home eventually accumulates more than it can hold, and clearing it out is a big relief. We make the process simple: call, get a quote, pick a time, and we handle the rest.",
      "Same-day pickups are often available for morning calls. We serve Apison as part of our southeast Hamilton County routes, which means fast response times for most addresses.",
    ],
    remove_items=["Old furniture","Appliances","Mattresses","Construction debris","Garage clutter","Electronics","Yard waste","Moving leftovers","Estate cleanouts","Hot tubs","Office furniture","And much more"],
    why_items=[
      {"head":"Familiar with New and Old Apison","body":"We've worked in both the newer subdivisions and established properties in the area. We adapt to whatever the job requires."},
      {"head":"Construction Debris Welcome","body":"Renovation leftovers, old materials, demo debris — we haul it alongside standard household junk."},
      {"head":"Upfront, Clear Pricing","body":"You get a firm price before we start loading. No changes after the fact."},
      {"head":"We Do the Lifting","body":"You don't carry, bag, or haul anything. Our crew handles start to finish."},
    ],
    service_area_body=[
      "We serve all of Apison, TN including neighborhoods along Apison Pike, Standifer Gap Road, and the surrounding growing Hamilton County communities.",
      "We also cover nearby Collegedale, Ooltewah, and East Brainerd. Call to confirm coverage for your specific address.",
      'Common Apison requests include <a href="/garage-cleanout-chattanooga-tn.html" style="color:#1a2e4a;font-weight:600;">garage cleanouts</a>, <a href="/furniture-removal-chattanooga-tn.html" style="color:#1a2e4a;font-weight:600;">furniture removal</a>, and <a href="/appliance-removal-chattanooga-tn.html" style="color:#1a2e4a;font-weight:600;">appliance haul-away</a>.',
    ],
    related_p='We handle <a href="/garage-cleanout-chattanooga-tn.html" style="color:#1a2e4a;font-weight:600;">garage cleanouts</a> and <a href="/furniture-removal-chattanooga-tn.html" style="color:#1a2e4a;font-weight:600;">furniture removal</a> in Apison. We also serve <a href="/junk-removal-collegedale-tn.html" style="color:#1a2e4a;font-weight:600;">Collegedale</a> and <a href="/junk-removal-ooltewah-tn.html" style="color:#1a2e4a;font-weight:600;">Ooltewah</a>.',
    related_links=[
      ("/garage-cleanout-chattanooga-tn.html","Garage Cleanout"),
      ("/furniture-removal-chattanooga-tn.html","Furniture Removal"),
      ("/appliance-removal-chattanooga-tn.html","Appliance Removal"),
      ("/junk-removal-collegedale-tn.html","Collegedale, TN"),
      ("/junk-removal-ooltewah-tn.html","Ooltewah, TN"),
    ],
    split_img="/images/garage-cleanout-boxes.jpg",
    split_img_alt="Garage cleanout in progress in Apison, TN growing community",
    split_img_cap="Serving Apison's new and established neighborhoods",
    split_text_h3="Growing Neighborhood, Growing Needs",
    split_text_p="New homes, renovations, garage overflows — Apison's growth means junk removal is in demand. We're here to meet it. Same-day and next-day service available.",
    contact_h2="Ready for Junk Removal in Apison, TN?",
    contact_p="Call for a fast, no-pressure quote. We serve Apison and southeast Hamilton County 7 days a week.",
    nearby_pages=[
      ("/junk-removal-collegedale-tn.html","Collegedale, TN"),
      ("/junk-removal-ooltewah-tn.html","Ooltewah, TN"),
      ("/junk-removal-east-brainerd-tn.html","East Brainerd, TN"),
    ],
    footer_area_label="Apison, TN",
    photo_imgs=[
      ("/images/local-home.jpg","New home in Apison, TN community served by junk removal","Serving Apison's growing neighborhoods"),
      ("/images/garage-before.jpg","Garage clutter in an Apison, TN home ready for cleanout","Garage cleanouts done efficiently"),
      ("/images/furniture-cleanout.jpg","Furniture being cleared from an Apison, TN property","Old furniture hauled away fast"),
    ],
  ),

  # ─── 13. Chickamauga, GA ───────────────────────────────────────────────────
  dict(
    slug="junk-removal-chickamauga-ga",
    city="Chickamauga", state="GA",
    title="Junk Removal Chickamauga GA | Walker County Haul-Away Service",
    meta="Junk removal in Chickamauga, GA — serving older homes, rural properties, and estate cleanouts in Walker County. Same-day often available. Free quote!",
    hero_p="Chickamauga is a historic Walker County community with a mix of older homes near the downtown area and rural properties on the outskirts. Whether you're clearing out a family homestead, dealing with estate belongings, or just hauling off furniture and appliances that have been sitting too long, we make the trip into North Georgia regularly.",
    hero_btn="Call Now for Same-Day Junk Removal in Chickamauga",
    proof_items=["Same-day available","Free estimates","Serving Chickamauga GA","7 days a week"],
    main_h2="Junk Removal for Chickamauga & Walker County",
    main_body=[
      "Chickamauga's older housing stock means many homes have accumulated items over multiple generations. We often work with families doing estate cleanouts — clearing out a parent's or grandparent's home, dealing with belongings from decades past, and trying to handle it all in a reasonable timeframe.",
      "We approach these jobs with care. We work at your pace, keep a clear communication throughout, and make sure you know the price before we remove a single item.",
      "Rural properties outside the Chickamauga downtown area often have outbuildings, barns, or sheds full of accumulated equipment and debris. We handle those cleanouts too — larger loads may require multiple trips, but we'll quote you per load so there are no surprises.",
      "We serve Chickamauga as part of our North Georgia routes, which also include Fort Oglethorpe and LaFayette. Same-day appointments are often available.",
    ],
    remove_items=["Old furniture","Appliances","Mattresses","Estate items","Farm & rural equipment","Barn & shed contents","Electronics","Yard debris","Construction materials","Moving leftovers","Clothing & boxes","And much more"],
    why_items=[
      {"head":"Experienced with Estate Cleanouts","body":"We handle estate jobs with care and efficiency — no rushing, no judgment, and always a clear price upfront."},
      {"head":"We Serve North Georgia","body":"Chickamauga and Walker County are part of our regular service area. No extra fees for the trip."},
      {"head":"Transparent Pricing","body":"You know the cost before we start. For large rural loads, we quote per trip."},
      {"head":"Full-Service Haul","body":"We carry, load, and clean up. You don't have to do a thing."},
    ],
    service_area_body=[
      "We serve Chickamauga, GA and Walker County including areas near Lee and Gordon Moore Park, Crawfish Springs Road, and surrounding rural Walker County communities.",
      "We also regularly serve Fort Oglethorpe, LaFayette, and Ringgold. Call to confirm we cover your specific address.",
      'Common Chickamauga requests include <a href="/estate-cleanout-chattanooga-tn.html" style="color:#1a2e4a;font-weight:600;">estate cleanouts</a>, <a href="/furniture-removal-chattanooga-tn.html" style="color:#1a2e4a;font-weight:600;">furniture removal</a>, and <a href="/yard-debris-removal-chattanooga-tn.html" style="color:#1a2e4a;font-weight:600;">outdoor debris removal</a>.',
    ],
    related_p='We handle <a href="/estate-cleanout-chattanooga-tn.html" style="color:#1a2e4a;font-weight:600;">estate cleanouts</a> and <a href="/furniture-removal-chattanooga-tn.html" style="color:#1a2e4a;font-weight:600;">furniture haul-away</a> in Chickamauga. We also serve <a href="/junk-removal-fort-oglethorpe-ga.html" style="color:#1a2e4a;font-weight:600;">Fort Oglethorpe</a> and <a href="/junk-removal-lafayette-ga.html" style="color:#1a2e4a;font-weight:600;">LaFayette</a>.',
    related_links=[
      ("/estate-cleanout-chattanooga-tn.html","Estate Cleanout"),
      ("/furniture-removal-chattanooga-tn.html","Furniture Removal"),
      ("/yard-debris-removal-chattanooga-tn.html","Outdoor Debris Removal"),
      ("/junk-removal-fort-oglethorpe-ga.html","Fort Oglethorpe, GA"),
      ("/junk-removal-lafayette-ga.html","LaFayette, GA"),
    ],
    split_img="/images/house-cleanout-boxes.jpg",
    split_img_alt="Estate cleanout in progress at a Chickamauga, GA home",
    split_img_cap="Estate and family property cleanouts done carefully",
    split_text_h3="Walker County Estate Cleanouts",
    split_text_p="Older homes, rural properties, and estate cleanouts are our specialty in the Chickamauga area. We work with care and always quote before we start.",
    contact_h2="Ready to Clear Out in Chickamauga, GA?",
    contact_p="Call for a free, no-pressure quote. We serve Chickamauga and Walker County with fast, professional service.",
    nearby_pages=[
      ("/junk-removal-fort-oglethorpe-ga.html","Fort Oglethorpe, GA"),
      ("/junk-removal-lafayette-ga.html","LaFayette, GA"),
      ("/junk-removal-ringgold-ga.html","Ringgold, GA"),
    ],
    footer_area_label="Chickamauga, GA",
    photo_imgs=[
      ("/images/estate-cleanout-room.jpg","Estate cleanout in an older Chickamauga, GA home","We handle estate and family cleanouts"),
      ("/images/house-cleanout-boxes.jpg","Boxes and belongings being cleared in Chickamauga, GA","Careful, thorough clearing"),
      ("/images/junk-removal-truck.jpg","Junk removal truck serving rural Chickamauga, GA","Walker County haul-away service"),
    ],
  ),

  # ─── 14. Dunlap, TN ────────────────────────────────────────────────────────
  dict(
    slug="junk-removal-dunlap-tn",
    city="Dunlap", state="TN",
    title="Junk Removal Dunlap TN | Sequatchie County Haul-Away Service",
    meta="Junk removal in Dunlap, TN — rural cleanouts, garage and shed haul-aways, and outdoor debris removal in Sequatchie County. Same-day often available. Free quote!",
    hero_p="Dunlap is the seat of Sequatchie County, tucked in the valley between Walden Ridge and the Cumberland Plateau. Properties here tend to be larger, with more land and more accumulated items — old outbuildings, tools and equipment, and the kind of deep-garage clutter that builds up over decades. We serve Dunlap and the surrounding valley regularly.",
    hero_btn="Call Now for Same-Day Junk Removal in Dunlap",
    proof_items=["Same-day available","Free estimates","Serving Dunlap TN","7 days a week"],
    main_h2="Sequatchie Valley Junk Removal in Dunlap, TN",
    main_body=[
      "Dunlap sits in one of the most scenic valleys in Tennessee, but the views don't make it any easier to haul a refrigerator down a long driveway or clear decades of tools and equipment out of an old barn. That's what we're here for.",
      "Properties in Sequatchie County often have more going on than a typical suburban lot — multiple outbuildings, large garages, sheds with decades of tools and equipment, and outdoor areas with accumulated debris. We handle all of it, including larger loads that may require multiple trips.",
      "Estate cleanouts are also a common call from Dunlap. Many families have owned property in the valley for generations, and when the time comes to clear it out, the volume can be significant. We work methodically, keep you informed, and always quote before we start.",
      "We make the trip to Dunlap from Chattanooga regularly. Same-day availability may be more limited given the distance, but next-day and scheduled appointments are readily available.",
    ],
    remove_items=["Old furniture","Appliances","Mattresses","Farm & garage equipment","Barn & shed contents","Yard debris & branches","Electronics","Construction materials","Estate items","Hot tubs","Moving leftovers","And much more"],
    why_items=[
      {"head":"We Make the Valley Trip","body":"Dunlap is part of our extended service area. We'll be upfront about travel logistics and pricing."},
      {"head":"Built for Larger Rural Loads","body":"Multiple outbuildings, large garages, heavy equipment — we bring the crew and truck space to handle it."},
      {"head":"Estate Cleanout Experience","body":"We've helped many families clear generational properties. We work carefully and communicate throughout."},
      {"head":"Upfront Pricing Per Load","body":"For large multi-trip jobs, we quote per load. You always know the cost before we take anything."},
    ],
    service_area_body=[
      "We serve Dunlap, TN and Sequatchie County including residential areas near Main Street, Rankin Avenue, and the surrounding Sequatchie Valley communities.",
      "We also cover nearby Jasper, Signal Mountain, and Sale Creek. Call to discuss your specific location and we'll figure out the fastest way to get there.",
      'Common Dunlap requests include <a href="/garage-cleanout-chattanooga-tn.html" style="color:#1a2e4a;font-weight:600;">garage and shed cleanouts</a>, <a href="/estate-cleanout-chattanooga-tn.html" style="color:#1a2e4a;font-weight:600;">estate haul-aways</a>, and <a href="/yard-debris-removal-chattanooga-tn.html" style="color:#1a2e4a;font-weight:600;">outdoor debris removal</a>.',
    ],
    related_p='We handle <a href="/garage-cleanout-chattanooga-tn.html" style="color:#1a2e4a;font-weight:600;">garage and shed cleanouts</a> and <a href="/estate-cleanout-chattanooga-tn.html" style="color:#1a2e4a;font-weight:600;">estate cleanouts</a> in Dunlap. We also serve <a href="/junk-removal-jasper-tn.html" style="color:#1a2e4a;font-weight:600;">Jasper</a> and <a href="/junk-removal-signal-mountain-tn.html" style="color:#1a2e4a;font-weight:600;">Signal Mountain</a>.',
    related_links=[
      ("/garage-cleanout-chattanooga-tn.html","Garage & Shed Cleanout"),
      ("/estate-cleanout-chattanooga-tn.html","Estate Cleanout"),
      ("/yard-debris-removal-chattanooga-tn.html","Outdoor Debris Removal"),
      ("/junk-removal-jasper-tn.html","Jasper, TN"),
      ("/junk-removal-signal-mountain-tn.html","Signal Mountain, TN"),
    ],
    split_img="/images/junk-pile.jpg",
    split_img_alt="Large junk pile at a rural Dunlap, TN property before cleanout",
    split_img_cap="Rural valley cleanouts — any size",
    split_text_h3="Big Rural Loads, Handled",
    split_text_p="Dunlap and Sequatchie Valley properties often have large volumes of accumulated junk. We bring the right crew and truck capacity to get it done.",
    contact_h2="Ready to Clear Out Your Dunlap Property?",
    contact_p="Call for a free quote on garage, estate, and rural cleanouts in Dunlap, TN. We'll talk through the logistics and find a time that works.",
    nearby_pages=[
      ("/junk-removal-jasper-tn.html","Jasper, TN"),
      ("/junk-removal-signal-mountain-tn.html","Signal Mountain, TN"),
      ("/junk-removal-sale-creek-tn.html","Sale Creek, TN"),
    ],
    footer_area_label="Dunlap, TN",
    photo_imgs=[
      ("/images/yard-branches-pile.jpg","Outdoor debris pile at a Dunlap, TN rural property","Rural and valley cleanouts"),
      ("/images/garage-before.jpg","Cluttered garage or outbuilding near Dunlap, TN","Garages and sheds fully cleared"),
      ("/images/truck-loading-job.jpg","Junk removal truck loaded in Sequatchie County, TN","We haul the whole load"),
    ],
  ),

  # ─── 15. Dayton, TN ────────────────────────────────────────────────────────
  dict(
    slug="junk-removal-dayton-tn",
    city="Dayton", state="TN",
    title="Junk Removal Dayton TN | Rhea County Haul-Away Service",
    meta="Junk removal in Dayton, TN — fast haul-away for homes, rentals, garages, and yard debris in Rhea County. Same-day often available. Free quote, call now!",
    hero_p="Dayton is the county seat of Rhea County and home to a mix of established residential neighborhoods, rental properties, and rural homes on the outskirts of town. Whether you're clearing out a garage, hauling off old furniture, or dealing with yard debris after a storm, we serve the Dayton area with prompt, professional service.",
    hero_btn="Call Now for Same-Day Junk Removal in Dayton",
    proof_items=["Same-day available","Free estimates","Serving Dayton TN","7 days a week"],
    main_h2="Junk Removal for Dayton & Rhea County",
    main_body=[
      "Dayton has a lot of character — older homes on tree-lined streets, newer subdivisions growing toward the edge of town, and rural properties that have been in families for years. All of them eventually need a good cleanout.",
      "Homeowners call us for the usual suspects: old furniture they can't get rid of, appliances that finally stopped working, garages that slowly turned into storage units, and yard waste that's piled up after pruning and storm cleanup.",
      "Landlords in Dayton also call us regularly to clear units between tenants. A quick, thorough move-out cleanout gets the property back on the market faster, and we can usually schedule within a day or two.",
      "We're farther from our main Chattanooga base than some stops, so same-day availability in Dayton can vary — but we make the trip regularly and next-day appointments are typically easy to arrange. Just call and tell us what you've got.",
    ],
    remove_items=["Old furniture","Appliances","Mattresses","Yard waste & debris","Garage clutter","Electronics","Rental move-out items","Construction materials","Estate cleanouts","Clothing & boxes","Hot tubs","And much more"],
    why_items=[
      {"head":"We Make the Rhea County Trip","body":"Dayton is part of our extended service area. We'll work with you on scheduling and be clear about any additional distance fees."},
      {"head":"Pricing Before We Start","body":"You get a firm quote before we load a single item. Simple and transparent."},
      {"head":"Handles All Property Types","body":"Homes, rentals, garages, yards — whatever kind of cleanout you need, we can do it."},
      {"head":"We Do the Work","body":"Point us to what needs to go and step back. Our crew handles everything else."},
    ],
    service_area_body=[
      "We serve Dayton, TN and Rhea County including residential areas near Market Street, Rhea County Highway, and surrounding communities in the area.",
      "We also regularly serve nearby Sale Creek, Birchwood, and Cleveland. Call to discuss your address and we'll confirm quickly.",
      'Dayton customers often book us for <a href="/furniture-removal-chattanooga-tn.html" style="color:#1a2e4a;font-weight:600;">furniture haul-away</a>, <a href="/appliance-removal-chattanooga-tn.html" style="color:#1a2e4a;font-weight:600;">appliance removal</a>, and <a href="/yard-debris-removal-chattanooga-tn.html" style="color:#1a2e4a;font-weight:600;">yard debris pickup</a>.',
    ],
    related_p='We handle <a href="/furniture-removal-chattanooga-tn.html" style="color:#1a2e4a;font-weight:600;">furniture removal</a> and <a href="/yard-debris-removal-chattanooga-tn.html" style="color:#1a2e4a;font-weight:600;">yard debris pickup</a> in Dayton. We also serve <a href="/junk-removal-sale-creek-tn.html" style="color:#1a2e4a;font-weight:600;">Sale Creek</a> and <a href="/junk-removal-cleveland-tn.html" style="color:#1a2e4a;font-weight:600;">Cleveland</a>.',
    related_links=[
      ("/furniture-removal-chattanooga-tn.html","Furniture Removal"),
      ("/appliance-removal-chattanooga-tn.html","Appliance Removal"),
      ("/yard-debris-removal-chattanooga-tn.html","Yard Debris Removal"),
      ("/junk-removal-sale-creek-tn.html","Sale Creek, TN"),
      ("/junk-removal-cleveland-tn.html","Cleveland, TN"),
    ],
    split_img="/images/workers-loading.jpg",
    split_img_alt="Junk removal crew hauling items from a Dayton, TN home",
    split_img_cap="Serving Dayton and Rhea County",
    split_text_h3="Dayton and Rhea County — We Come to You",
    split_text_p="Homes, rentals, garages, and yards across Rhea County — we haul it all. Same-day availability varies but next-day is almost always possible.",
    contact_h2="Ready to Book Junk Removal in Dayton, TN?",
    contact_p="Call for a free quote. We serve Dayton and Rhea County regularly. One call gets it done.",
    nearby_pages=[
      ("/junk-removal-sale-creek-tn.html","Sale Creek, TN"),
      ("/junk-removal-cleveland-tn.html","Cleveland, TN"),
      ("/junk-removal-birchwood-tn.html","Birchwood, TN"),
    ],
    footer_area_label="Dayton, TN",
    photo_imgs=[
      ("/images/residential-neighborhood.jpg","Established neighborhood in Dayton, TN served by junk removal","Serving Dayton and Rhea County"),
      ("/images/old-appliance-removal.jpg","Old appliance being removed from a Dayton, TN home","Appliances and bulk items hauled fast"),
      ("/images/yard-debris-cleanup.jpg","Yard debris cleanup in Dayton, TN","Yard waste cleared quickly"),
    ],
  ),

  # ─── 16. Sale Creek, TN ────────────────────────────────────────────────────
  dict(
    slug="junk-removal-sale-creek-tn",
    city="Sale Creek", state="TN",
    title="Junk Removal Sale Creek TN | Rural & River Area Cleanup",
    meta="Junk removal in Sale Creek, TN — rural properties, river-area homes, and outdoor debris removal in north Hamilton County. Same-day often available. Free quote!",
    hero_p="Sale Creek is a rural community in northern Hamilton County along the Tennessee River, and properties here tend to be spread out with larger lots and plenty of outdoor space. Whether you're clearing accumulated items from a river-area property, hauling off debris from a large lot, or dealing with a garage or outbuilding full of years of junk, we serve the Sale Creek area regularly.",
    hero_btn="Call Now for Same-Day Junk Removal in Sale Creek",
    proof_items=["Same-day available","Free estimates","Serving Sale Creek TN","7 days a week"],
    main_h2="Rural Property Cleanouts in Sale Creek, TN",
    main_body=[
      "Sale Creek sits between Soddy-Daisy to the south and Dayton to the north, and it has the feel of a rural community that's been there a long time. Properties along Harrison Bay Road, Sale Creek Road, and the river corridor tend to have large lots — which means more space for things to pile up.",
      "We've done cleanouts from properties here that have everything from porch furniture and old appliances to barn contents and construction debris left over from projects that were never quite finished. We haul it all.",
      "River-area properties can also accumulate unique outdoor items — old boat accessories, dock furniture, watercraft gear, and weathered outdoor pieces. We're used to loading heavy, awkward outdoor items and have the equipment to do it efficiently.",
      "Schedule is generally flexible for Sale Creek — we're in the area often enough that next-day availability is common, and same-day slots open up frequently in the morning.",
    ],
    remove_items=["Old furniture","Appliances","Mattresses","Outdoor equipment","Barn & shed contents","Yard debris","Construction materials","Electronics","River-area items","Estate cleanouts","Moving leftovers","And much more"],
    why_items=[
      {"head":"Regular Route Through Sale Creek","body":"We're in the area often enough to offer next-day and frequently same-day service."},
      {"head":"Built for Rural Lots","body":"Large lots, long driveways, and heavy outdoor items are no problem for our crew."},
      {"head":"Clear Pricing","body":"We quote based on truck space before we start. You'll know the cost before a single item is moved."},
      {"head":"Everything Included","body":"Carrying, loading, and cleanup — all of it is part of the job."},
    ],
    service_area_body=[
      "We serve Sale Creek, TN and surrounding north Hamilton County including areas near Sale Creek Road, Harrison Bay Road, and the Tennessee River corridor.",
      "We also regularly serve nearby Soddy-Daisy, Birchwood, and Dayton. Rural addresses are welcome — just describe your access when you call.",
      'Sale Creek customers most often book us for <a href="/yard-debris-removal-chattanooga-tn.html" style="color:#1a2e4a;font-weight:600;">outdoor debris removal</a>, <a href="/garage-cleanout-chattanooga-tn.html" style="color:#1a2e4a;font-weight:600;">garage and shed cleanouts</a>, and <a href="/estate-cleanout-chattanooga-tn.html" style="color:#1a2e4a;font-weight:600;">rural estate haul-aways</a>.',
    ],
    related_p='We handle <a href="/yard-debris-removal-chattanooga-tn.html" style="color:#1a2e4a;font-weight:600;">outdoor debris removal</a> and <a href="/garage-cleanout-chattanooga-tn.html" style="color:#1a2e4a;font-weight:600;">garage cleanouts</a> in Sale Creek. We also serve <a href="/junk-removal-soddy-daisy-tn.html" style="color:#1a2e4a;font-weight:600;">Soddy-Daisy</a> and <a href="/junk-removal-birchwood-tn.html" style="color:#1a2e4a;font-weight:600;">Birchwood</a>.',
    related_links=[
      ("/yard-debris-removal-chattanooga-tn.html","Outdoor Debris Removal"),
      ("/garage-cleanout-chattanooga-tn.html","Garage & Shed Cleanout"),
      ("/estate-cleanout-chattanooga-tn.html","Estate Cleanout"),
      ("/junk-removal-soddy-daisy-tn.html","Soddy-Daisy, TN"),
      ("/junk-removal-birchwood-tn.html","Birchwood, TN"),
    ],
    split_img="/images/yard-debris-cleanup.jpg",
    split_img_alt="Outdoor debris cleanup at a Sale Creek, TN rural property",
    split_img_cap="Rural and river-area cleanouts in Sale Creek",
    split_text_h3="River Area, Rural Lots — We Handle It",
    split_text_p="Large lots and rural properties in Sale Creek are our kind of job. We bring the crew and truck capacity to clear it out efficiently.",
    contact_h2="Ready to Clear Out Your Sale Creek Property?",
    contact_p="Call for a free quote. Rural and river-area properties welcome. Same-day and next-day service available.",
    nearby_pages=[
      ("/junk-removal-soddy-daisy-tn.html","Soddy-Daisy, TN"),
      ("/junk-removal-birchwood-tn.html","Birchwood, TN"),
      ("/junk-removal-dayton-tn.html","Dayton, TN"),
    ],
    footer_area_label="Sale Creek, TN",
    photo_imgs=[
      ("/images/yard-branches-pile.jpg","Outdoor debris pile at Sale Creek, TN rural property","Rural and river-area debris cleared"),
      ("/images/junk-pile.jpg","Large junk accumulation near Sale Creek, TN","Any size load handled"),
      ("/images/junk-removal-truck.jpg","Junk removal truck serving Sale Creek, TN","We haul it all away"),
    ],
  ),

  # ─── 17. Jasper, TN ────────────────────────────────────────────────────────
  dict(
    slug="junk-removal-jasper-tn",
    city="Jasper", state="TN",
    title="Junk Removal Jasper TN | Marion County Haul-Away Service",
    meta="Junk removal in Jasper, TN — garage cleanouts, shed haul-aways, and property cleanouts in Marion County. Same-day often available. Free quote!",
    hero_p="Jasper is the seat of Marion County, positioned along I-24 between Chattanooga and the Sequatchie Valley. It's a community with a mix of downtown residential properties and larger rural lots on the outskirts — both of which generate regular junk removal calls. We serve Jasper and the surrounding Marion County area.",
    hero_btn="Call Now for Same-Day Junk Removal in Jasper",
    proof_items=["Same-day available","Free estimates","Serving Jasper TN","7 days a week"],
    main_h2="Junk Removal for Jasper & Marion County",
    main_body=[
      "Jasper sits in a beautiful part of Tennessee, but the scenery doesn't help when you're trying to move a refrigerator down a steep driveway or figure out what to do with a garage full of decades of accumulated items. We've worked in Marion County many times and know how to handle both suburban and rural property cleanouts.",
      "Garages and sheds are among the most common calls we get from Jasper. Properties here often have more outbuilding space than the average Chattanooga suburb, and those outbuildings tend to fill up over the years with tools, furniture, equipment, and miscellaneous junk. We empty them completely.",
      "Estate cleanouts are also common — families settling the affairs of parents or grandparents who have lived in Marion County for decades. We handle these carefully and efficiently, keeping you informed throughout.",
      "Our scheduling for Jasper can vary by day, but next-day appointments are typically available and we do occasionally have same-day capacity for morning calls. Just call and we'll work out the logistics.",
    ],
    remove_items=["Old furniture","Appliances","Mattresses","Garage & shed contents","Farm equipment","Electronics","Yard debris","Construction materials","Estate items","Hot tubs","Moving leftovers","And much more"],
    why_items=[
      {"head":"We Serve Marion County","body":"Jasper is part of our extended service area. We'll be upfront about scheduling and any distance considerations."},
      {"head":"Large-Load Capable","body":"Bigger properties, multiple outbuildings — we bring enough crew and truck space to handle the job in full."},
      {"head":"Pricing You Can Count On","body":"We quote per truckload before we start. You always know the cost."},
      {"head":"We Handle Every Step","body":"Carrying, loading, sweeping up — all included. You just show us what to take."},
    ],
    service_area_body=[
      "We serve Jasper, TN and Marion County including areas near the downtown corridor, US-41, and surrounding rural Marion County properties.",
      "We also cover nearby Dunlap, Signal Mountain, and Sale Creek. Call to discuss your address — we'll confirm coverage and talk through the job.",
      'Jasper customers most often book us for <a href="/garage-cleanout-chattanooga-tn.html" style="color:#1a2e4a;font-weight:600;">garage and shed cleanouts</a>, <a href="/estate-cleanout-chattanooga-tn.html" style="color:#1a2e4a;font-weight:600;">estate haul-aways</a>, and <a href="/furniture-removal-chattanooga-tn.html" style="color:#1a2e4a;font-weight:600;">furniture removal</a>.',
    ],
    related_p='We handle <a href="/garage-cleanout-chattanooga-tn.html" style="color:#1a2e4a;font-weight:600;">garage cleanouts</a> and <a href="/estate-cleanout-chattanooga-tn.html" style="color:#1a2e4a;font-weight:600;">estate haul-aways</a> in Jasper. We also serve <a href="/junk-removal-dunlap-tn.html" style="color:#1a2e4a;font-weight:600;">Dunlap</a> and <a href="/junk-removal-signal-mountain-tn.html" style="color:#1a2e4a;font-weight:600;">Signal Mountain</a>.',
    related_links=[
      ("/garage-cleanout-chattanooga-tn.html","Garage & Shed Cleanout"),
      ("/estate-cleanout-chattanooga-tn.html","Estate Cleanout"),
      ("/furniture-removal-chattanooga-tn.html","Furniture Removal"),
      ("/junk-removal-dunlap-tn.html","Dunlap, TN"),
      ("/junk-removal-signal-mountain-tn.html","Signal Mountain, TN"),
    ],
    split_img="/images/hauling-crew.jpg",
    split_img_alt="Junk removal crew ready for a Marion County, TN property cleanout",
    split_img_cap="Serving Jasper and Marion County",
    split_text_h3="Marion County's Junk Removal Crew",
    split_text_p="Garages, sheds, estates, and more — we serve Jasper and surrounding Marion County with professional haul-away service. Call for fast scheduling.",
    contact_h2="Ready to Clear Out in Jasper, TN?",
    contact_p="Call for a free, no-obligation quote on junk removal in Jasper and Marion County.",
    nearby_pages=[
      ("/junk-removal-dunlap-tn.html","Dunlap, TN"),
      ("/junk-removal-signal-mountain-tn.html","Signal Mountain, TN"),
      ("/junk-removal-sale-creek-tn.html","Sale Creek, TN"),
    ],
    footer_area_label="Jasper, TN",
    photo_imgs=[
      ("/images/garage-cleanout-tools.jpg","Garage contents being cleared in Jasper, TN Marion County","Garages and sheds fully emptied"),
      ("/images/estate-cleanout-room.jpg","Estate cleanout in a Jasper, TN family property","Estate cleanouts handled with care"),
      ("/images/truck-loading-job.jpg","Junk removal truck loaded in Jasper, TN","Full loads hauled efficiently"),
    ],
  ),

  # ─── 18. Trenton, GA ───────────────────────────────────────────────────────
  dict(
    slug="junk-removal-trenton-ga",
    city="Trenton", state="GA",
    title="Junk Removal Trenton GA | Dade County Mountain Property Cleanouts",
    meta="Junk removal in Trenton, GA — mountain and rural property cleanouts in Dade County. Same-day often available. Free quote from Fast Chattanooga Junk Removal!",
    hero_p="Trenton is the seat of Dade County, set against the base of Lookout Mountain in the northwest corner of Georgia. Properties here range from in-town residential homes to larger rural lots and mountain properties up on the ridge. We serve Trenton and surrounding Dade County as part of our extended North Georgia routes.",
    hero_btn="Call Now for Same-Day Junk Removal in Trenton",
    proof_items=["Same-day available","Free estimates","Serving Trenton GA","7 days a week"],
    main_h2="Junk Removal for Trenton & Dade County, GA",
    main_body=[
      "Trenton's location at the foot of Lookout Mountain gives it a rural, unhurried quality. But rural doesn't mean unchecked clutter. Homes in Trenton and the surrounding communities accumulate items like anywhere else — old furniture, appliances, garage overflow, and yard debris that eventually becomes its own project to manage.",
      "Mountain properties in the Dade County area can come with their own challenges — steep access, large lots, outbuildings — and we've handled cleanouts at all kinds of properties. We discuss the logistics before scheduling so there are no surprises on either side.",
      "Estate cleanouts and property cleanouts for families dealing with inherited homes are a common request in this part of Georgia. We approach this work with care, communicating throughout and always quoting a firm price before we take anything.",
      "Scheduling for Trenton may require a day or two of lead time, but next-day appointments are typical and we occasionally have same-day capacity. Call and we'll sort it out.",
    ],
    remove_items=["Old furniture","Appliances","Mattresses","Mountain property debris","Estate items","Garage & shed contents","Electronics","Yard debris & brush","Construction materials","Moving leftovers","Outdoor equipment","And much more"],
    why_items=[
      {"head":"We Serve Dade County","body":"Trenton and surrounding Dade County are part of our regular Georgia service area."},
      {"head":"Mountain Property Experience","body":"We've worked on properties with steep access and large lots. We'll talk through logistics before we arrive."},
      {"head":"Clear Pricing Before We Start","body":"Every job gets a quote before we load. No surprises."},
      {"head":"We Handle Everything","body":"From carrying items down a hillside to sweeping out a garage — all included."},
    ],
    service_area_body=[
      "We serve Trenton, GA and Dade County including residential areas along main town streets and surrounding rural and mountain communities up toward Lookout Mountain.",
      "We also serve nearby LaFayette, Fort Oglethorpe, and Lookout Mountain, TN. Call to discuss your address and we'll confirm quickly.",
      'Trenton customers commonly book us for <a href="/estate-cleanout-chattanooga-tn.html" style="color:#1a2e4a;font-weight:600;">estate cleanouts</a>, <a href="/furniture-removal-chattanooga-tn.html" style="color:#1a2e4a;font-weight:600;">furniture haul-away</a>, and <a href="/yard-debris-removal-chattanooga-tn.html" style="color:#1a2e4a;font-weight:600;">outdoor debris removal</a>.',
    ],
    related_p='We handle <a href="/estate-cleanout-chattanooga-tn.html" style="color:#1a2e4a;font-weight:600;">estate cleanouts</a> and <a href="/furniture-removal-chattanooga-tn.html" style="color:#1a2e4a;font-weight:600;">furniture removal</a> in Trenton. We also serve <a href="/junk-removal-lafayette-ga.html" style="color:#1a2e4a;font-weight:600;">LaFayette</a> and <a href="/junk-removal-fort-oglethorpe-ga.html" style="color:#1a2e4a;font-weight:600;">Fort Oglethorpe</a>.',
    related_links=[
      ("/estate-cleanout-chattanooga-tn.html","Estate Cleanout"),
      ("/furniture-removal-chattanooga-tn.html","Furniture Removal"),
      ("/yard-debris-removal-chattanooga-tn.html","Outdoor Debris Removal"),
      ("/junk-removal-lafayette-ga.html","LaFayette, GA"),
      ("/junk-removal-fort-oglethorpe-ga.html","Fort Oglethorpe, GA"),
    ],
    split_img="/images/house-cleanout-boxes.jpg",
    split_img_alt="Estate cleanout at a Trenton, GA Dade County property",
    split_img_cap="Mountain and rural cleanouts in Dade County",
    split_text_h3="Dade County Cleanouts Done Right",
    split_text_p="From mountain properties to in-town homes, we serve Trenton and Dade County with professional junk removal. Call to discuss your project.",
    contact_h2="Ready to Clear Out in Trenton, GA?",
    contact_p="Call for a free quote. We serve Trenton and Dade County with professional junk removal service.",
    nearby_pages=[
      ("/junk-removal-lafayette-ga.html","LaFayette, GA"),
      ("/junk-removal-fort-oglethorpe-ga.html","Fort Oglethorpe, GA"),
      ("/junk-removal-lookout-mountain-tn.html","Lookout Mountain, TN"),
    ],
    footer_area_label="Trenton, GA",
    photo_imgs=[
      ("/images/local-home.jpg","Home in Trenton, GA Dade County served by junk removal","Serving Trenton and Dade County"),
      ("/images/house-cleanout-boxes.jpg","Property cleanout in progress in Trenton, GA","Estate and family cleanouts"),
      ("/images/junk-removal-truck.jpg","Junk removal truck serving rural Trenton, GA","We haul it all from Dade County"),
    ],
  ),

  # ─── 19. LaFayette, GA ─────────────────────────────────────────────────────
  dict(
    slug="junk-removal-lafayette-ga",
    city="LaFayette", state="GA",
    title="Junk Removal LaFayette GA | Walker County Haul-Away Service",
    meta="Junk removal in LaFayette, GA — serving older homes, rentals, and estate cleanouts in Walker County. Same-day often available. Free quote from Fast Chattanooga Junk Removal!",
    hero_p="LaFayette is the seat of Walker County and a community with deep roots — which often means older homes with decades of accumulated items, rental properties in various states of turnover, and estate cleanouts for families settling longtime Walker County properties. Our crew serves LaFayette as part of our North Georgia routes.",
    hero_btn="Call Now for Same-Day Junk Removal in LaFayette",
    proof_items=["Same-day available","Free estimates","Serving LaFayette GA","7 days a week"],
    main_h2="Serving LaFayette & Walker County Homes",
    main_body=[
      "LaFayette has the character of a genuine small Southern city — with a historic downtown, established neighborhoods, and plenty of older homes on the surrounding streets. College Street, the South Main Street corridor, and the neighborhoods branching off them are full of homes that have been in families for a long time, and that history often comes with a lot of accumulated stuff.",
      "Estate cleanouts are one of the most common requests we get from LaFayette. When a longtime resident passes and family is left to clear the home, the volume of items can be overwhelming. We approach these cleanouts with care, taking direction from the family, working at a manageable pace, and quoting firmly before we start.",
      "Rental properties in LaFayette also generate regular calls. Move-out cleanouts between tenants, clearing garages that filled up over a long tenancy, and hauling off appliances that were left behind — we handle all of it efficiently.",
      "Scheduling for LaFayette usually means next-day or same-day service depending on our route that week. Call early for the best chance at same-day availability.",
    ],
    remove_items=["Old furniture","Appliances","Mattresses","Estate items","Rental debris","Electronics","Yard waste","Garage clutter","Construction materials","Moving leftovers","Clothing & boxes","And much more"],
    why_items=[
      {"head":"Walker County is Our Territory","body":"We serve LaFayette and Walker County regularly as part of our North Georgia routes."},
      {"head":"Estate Cleanout Specialists","body":"We've helped many Walker County families through the estate clearance process. We work carefully and quote upfront."},
      {"head":"Pricing That Makes Sense","body":"Based on truck space. You see the load, we name the price. No end-of-job fees."},
      {"head":"We Do It All","body":"Carrying, hauling, cleanup — all included. You don't touch a thing if you don't want to."},
    ],
    service_area_body=[
      "We serve LaFayette, GA and Walker County including areas near the downtown corridor, Chattanooga Street, College Street, and the surrounding residential communities.",
      "We also regularly serve nearby Chickamauga, Fort Oglethorpe, and Trenton. Call and we'll confirm coverage for your address.",
      'LaFayette customers frequently book us for <a href="/estate-cleanout-chattanooga-tn.html" style="color:#1a2e4a;font-weight:600;">estate cleanouts</a>, <a href="/furniture-removal-chattanooga-tn.html" style="color:#1a2e4a;font-weight:600;">furniture removal</a>, and <a href="/appliance-removal-chattanooga-tn.html" style="color:#1a2e4a;font-weight:600;">appliance haul-away</a>.',
    ],
    related_p='We handle <a href="/estate-cleanout-chattanooga-tn.html" style="color:#1a2e4a;font-weight:600;">estate cleanouts</a> and <a href="/furniture-removal-chattanooga-tn.html" style="color:#1a2e4a;font-weight:600;">furniture removal</a> in LaFayette. We also serve <a href="/junk-removal-chickamauga-ga.html" style="color:#1a2e4a;font-weight:600;">Chickamauga</a> and <a href="/junk-removal-trenton-ga.html" style="color:#1a2e4a;font-weight:600;">Trenton</a>.',
    related_links=[
      ("/estate-cleanout-chattanooga-tn.html","Estate Cleanout"),
      ("/furniture-removal-chattanooga-tn.html","Furniture Removal"),
      ("/appliance-removal-chattanooga-tn.html","Appliance Removal"),
      ("/junk-removal-chickamauga-ga.html","Chickamauga, GA"),
      ("/junk-removal-trenton-ga.html","Trenton, GA"),
    ],
    split_img="/images/estate-cleanout-room.jpg",
    split_img_alt="Estate cleanout in progress in LaFayette, GA Walker County",
    split_img_cap="Estate and family property cleanouts in Walker County",
    split_text_h3="Walker County's Estate Cleanout Crew",
    split_text_p="From longtime family homes to rental properties, we serve LaFayette and Walker County with professional, caring junk removal service.",
    contact_h2="Ready to Book Junk Removal in LaFayette, GA?",
    contact_p="Call for a free, no-pressure quote. We serve LaFayette and Walker County 7 days a week.",
    nearby_pages=[
      ("/junk-removal-chickamauga-ga.html","Chickamauga, GA"),
      ("/junk-removal-trenton-ga.html","Trenton, GA"),
      ("/junk-removal-fort-oglethorpe-ga.html","Fort Oglethorpe, GA"),
    ],
    footer_area_label="LaFayette, GA",
    photo_imgs=[
      ("/images/chattanooga-residential.jpg","Established neighborhood in LaFayette, GA Walker County","Serving LaFayette and Walker County"),
      ("/images/estate-cleanout-room.jpg","Estate cleanout in a LaFayette, GA family home","Estate cleanouts done carefully"),
      ("/images/refrigerator-removal.jpg","Appliance removal service in LaFayette, GA","Appliances and bulk items removed"),
    ],
  ),

  # ─── 20. Charleston, TN ────────────────────────────────────────────────────
  dict(
    slug="junk-removal-charleston-tn",
    city="Charleston", state="TN",
    title="Junk Removal Charleston TN | Bradley & McMinn County Haul-Away",
    meta="Junk removal in Charleston, TN — homes, garages, and appliance removal near the Bradley-McMinn county line. Same-day often available. Free quote!",
    hero_p="Charleston sits near the border of Bradley and McMinn counties, south of Cleveland and east of the Tennessee River. It's a small community with a mix of residential homes and rural properties that call us when it's time for a cleanout. Whether you're hauling off old appliances, clearing a garage, or dealing with estate items, we serve Charleston as part of our extended area routes.",
    hero_btn="Call Now for Same-Day Junk Removal in Charleston",
    proof_items=["Same-day available","Free estimates","Serving Charleston TN","7 days a week"],
    main_h2="Junk Removal for Charleston & Surrounding Communities",
    main_body=[
      "Charleston is a small, quiet community — the kind of place where things don't always get thrown away immediately. Old appliances sit on the porch. Furniture migrates from the living room to the spare room to the garage. Yard debris from last season is still sitting in a pile. We handle all of it.",
      "Homeowners in Charleston often call us for appliance haul-aways — old refrigerators, washers, dryers, and stoves that finally need to go. We pick up appliances of all types and sizes and haul them away properly.",
      "Garages are another common call. Charleston properties often have extra outdoor storage, and those spaces fill up quickly with tools, furniture, seasonal items, and miscellaneous junk. We empty them completely in a single trip when the volume allows.",
      "Scheduling for Charleston is usually next-day or close to same-day depending on our Bradley County route that week. Call early and we'll give you the fastest available slot.",
    ],
    remove_items=["Old furniture","Appliances","Mattresses","Garage clutter","Electronics","Yard waste","Construction debris","Estate items","Moving leftovers","Hot tubs","Clothing & boxes","And much more"],
    why_items=[
      {"head":"Serves the Bradley-McMinn Area","body":"Charleston is on our Cleveland and Bradley County route. Fast scheduling, no extra hassle."},
      {"head":"Great for Appliance Haul-Aways","body":"Old refrigerators, washers, dryers — we load and haul appliances of all sizes without you having to move them."},
      {"head":"Upfront Pricing","body":"You know what you're paying before we load a single item. No surprises."},
      {"head":"We Handle the Job","body":"Our crew carries, loads, and cleans up. You just show us what needs to go."},
    ],
    service_area_body=[
      "We serve Charleston, TN and surrounding Bradley and McMinn County communities including areas along US-11 and the surrounding rural and residential neighborhoods.",
      "We also regularly serve nearby Cleveland, Dayton, and Birchwood. Call to confirm your address is covered.",
      'Common Charleston requests include <a href="/appliance-removal-chattanooga-tn.html" style="color:#1a2e4a;font-weight:600;">appliance removal</a>, <a href="/garage-cleanout-chattanooga-tn.html" style="color:#1a2e4a;font-weight:600;">garage cleanouts</a>, and <a href="/furniture-removal-chattanooga-tn.html" style="color:#1a2e4a;font-weight:600;">furniture haul-away</a>.',
    ],
    related_p='We handle <a href="/appliance-removal-chattanooga-tn.html" style="color:#1a2e4a;font-weight:600;">appliance removal</a> and <a href="/garage-cleanout-chattanooga-tn.html" style="color:#1a2e4a;font-weight:600;">garage cleanouts</a> in Charleston. We also serve <a href="/junk-removal-cleveland-tn.html" style="color:#1a2e4a;font-weight:600;">Cleveland</a> and <a href="/junk-removal-dayton-tn.html" style="color:#1a2e4a;font-weight:600;">Dayton</a>.',
    related_links=[
      ("/appliance-removal-chattanooga-tn.html","Appliance Removal"),
      ("/garage-cleanout-chattanooga-tn.html","Garage Cleanout"),
      ("/furniture-removal-chattanooga-tn.html","Furniture Removal"),
      ("/junk-removal-cleveland-tn.html","Cleveland, TN"),
      ("/junk-removal-dayton-tn.html","Dayton, TN"),
    ],
    split_img="/images/washer-dryer-removal.jpg",
    split_img_alt="Washer and dryer removal from a Charleston, TN home",
    split_img_cap="Appliance pickup in Charleston and surrounding areas",
    split_text_h3="Charleston's Appliance & Junk Haulers",
    split_text_p="Old appliances, garage overflows, yard debris — we handle it all in Charleston and the surrounding Bradley-McMinn area. Call for fast, no-pressure service.",
    contact_h2="Ready to Book Junk Removal in Charleston, TN?",
    contact_p="Call for a free quote. We serve Charleston and surrounding communities with fast, professional haul-away service.",
    nearby_pages=[
      ("/junk-removal-cleveland-tn.html","Cleveland, TN"),
      ("/junk-removal-dayton-tn.html","Dayton, TN"),
      ("/junk-removal-birchwood-tn.html","Birchwood, TN"),
    ],
    footer_area_label="Charleston, TN",
    photo_imgs=[
      ("/images/washer-dryer-removal.jpg","Old washer and dryer removed from a Charleston, TN home","Appliances hauled away same day"),
      ("/images/cluttered-garage.jpg","Cluttered garage in Charleston, TN ready for cleanout","Garages cleared start to finish"),
      ("/images/workers-loading.jpg","Junk removal workers serving Charleston, TN area","Professional service near Bradley-McMinn line"),
    ],
  ),

]  # end PAGES


# ── HTML template ─────────────────────────────────────────────────────────────

def build_page(p):
  city      = p["city"]
  state     = p["state"]
  slug      = p["slug"]
  canonical = f"{BASE_URL}/{slug}.html"

  # build photo row html
  photo_rows = ""
  imgs = p["photo_imgs"]
  photo_rows = f"""
    <div class="photo-row">
      <div class="photo-item" style="height:220px"><img src="{imgs[0][0]}" alt="{imgs[0][1]}" loading="lazy" /><div class="photo-caption">{imgs[0][2]}</div></div>
      <div class="photo-item" style="height:220px"><img src="{imgs[1][0]}" alt="{imgs[1][1]}" loading="lazy" /><div class="photo-caption">{imgs[1][2]}</div></div>
      <div class="photo-item" style="height:220px"><img src="{imgs[2][0]}" alt="{imgs[2][1]}" loading="lazy" /><div class="photo-caption">{imgs[2][2]}</div></div>
    </div>"""

  # build remove grid
  remove_lis = "\n        ".join(f"<li>{item}</li>" for item in p["remove_items"])

  # build why list
  why_items_html = ""
  for i, w in enumerate(p["why_items"], 1):
    why_items_html += f"""
        <div class="why-item">
          <div class="why-icon">{i}</div>
          <p><strong>{w['head']}</strong>{w['body']}</p>
        </div>"""

  # build service area body
  _sa_parts = []
  for _i, _para in enumerate(p["service_area_body"]):
      _style = ' style="margin-top:14px;"' if _i > 0 else ''
      _sa_parts.append(f"<p{_style}>{_para}</p>")
  service_area_ps = "\n      ".join(_sa_parts)

  # build related links grid
  related_links_html = "\n        ".join(
    f'<a href="{r[0]}" class="related-link">{r[1]} &#8594;</a>'
    for r in p["related_links"]
  )

  # build nearby pages nav (nav-bar and dropdown)
  nearby_nav = "\n      ".join(
    f'<a href="{n[0]}">{n[1]}</a>'
    for n in p["nearby_pages"]
  )

  # build main body paragraphs
  body_ps = "\n      ".join(f"<p>{para}</p>" for para in p["main_body"])

  return f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>{p['title']}</title>
  <meta name="description" content="{p['meta']}" />
  <meta name="robots" content="index, follow" />
  <link rel="canonical" href="{canonical}" />
  <meta property="og:type" content="website" />
  <meta property="og:site_name" content="Fast Chattanooga Junk Removal" />
  <meta property="og:title" content="{p['title']}" />
  <meta property="og:description" content="{p['meta']}" />
  <meta property="og:url" content="{canonical}" />
  <meta name="twitter:card" content="summary" />
  <meta name="twitter:title" content="{p['title']}" />
  <meta name="twitter:description" content="{p['meta']}" />
  <script type="application/ld+json">
  {{
    "@context": "https://schema.org",
    "@type": "LocalBusiness",
    "name": "Fast Chattanooga Junk Removal",
    "telephone": "+14235563473",
    "url": "https://fastchattanoogajunkremoval.com",
    "priceRange": "$$",
    "openingHours": "Mo-Su 07:00-19:00",
    "areaServed": [
      {{"@type": "City", "name": "Chattanooga"}},
      {{"@type": "City", "name": "{city}"}}
    ],
    "address": {{
      "@type": "PostalAddress",
      "addressLocality": "Chattanooga",
      "addressRegion": "TN",
      "addressCountry": "US"
    }}
  }}
  </script>
  <style>
    *, *::before, *::after {{ box-sizing: border-box; margin: 0; padding: 0; }}
    body {{ font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Arial, sans-serif; color: #1a1a1a; background: #fff; line-height: 1.6; }}
    .container {{ max-width: 900px; margin: 0 auto; padding: 0 20px; }}
    header {{ background: #1a2e4a; color: #fff; padding: 16px 0; }}
    header .container {{ display: flex; align-items: center; justify-content: space-between; flex-wrap: wrap; gap: 10px; }}
    .brand {{ font-size: 1.1rem; font-weight: 700; letter-spacing: 0.02em; color: #fff; text-decoration: none; }}
    .header-phone {{ color: #f97316; font-weight: 700; font-size: 1.1rem; text-decoration: none; }}
    .header-phone:hover {{ text-decoration: underline; }}
    .header-right {{ display: flex; align-items: center; gap: 16px; }}
    .menu-btn {{ background: none; border: 2px solid rgba(255,255,255,0.3); color: #fff; font-size: 1.3rem; cursor: pointer; padding: 4px 10px; border-radius: 4px; line-height: 1; }}
    .menu-btn:hover {{ border-color: #f97316; color: #f97316; }}
    .dropdown-menu {{ background: #1a2e4a; border-bottom: 2px solid #f97316; display: none; }}
    .dropdown-menu.open {{ display: block; }}
    .dropdown-menu .container {{ display: flex; flex-direction: column; padding: 8px 20px 16px; }}
    .dropdown-menu a {{ color: #cbd5e1; text-decoration: none; font-size: 1rem; padding: 11px 0; border-bottom: 1px solid #253d5c; display: block; }}
    .dropdown-menu a:last-child {{ border-bottom: none; }}
    .dropdown-menu a:hover, .dropdown-menu a.active {{ color: #f97316; }}
    .menu-label {{ color: #94a3b8; font-size: 0.75rem; font-weight: 700; text-transform: uppercase; letter-spacing: 0.08em; padding: 12px 0 4px; display: block; }}
    .nav-bar {{ background: #122338; border-bottom: 1px solid #0f1c2e; }}
    .nav-bar .container {{ display: flex; gap: 4px; flex-wrap: wrap; }}
    .nav-bar a {{ color: #cbd5e1; text-decoration: none; font-size: 0.88rem; padding: 8px 12px; display: inline-block; transition: color 0.15s; }}
    .nav-bar a:hover, .nav-bar a.active {{ color: #f97316; }}
    .related-grid {{ display: grid; grid-template-columns: repeat(auto-fill, minmax(200px, 1fr)); gap: 10px; margin-top: 16px; }}
    .related-link {{ display: block; background: #f0f6ff; border: 1px solid #c7d8f0; color: #1a2e4a; text-decoration: none; padding: 14px 18px; border-radius: 6px; font-weight: 600; font-size: 1rem; transition: background 0.15s; }}
    .related-link:hover {{ background: #dbeafe; }}
    .hero {{ background: #f0f6ff; padding: 64px 0 56px; text-align: center; border-bottom: 3px solid #1a2e4a; }}
    .hero h1 {{ font-size: clamp(1.8rem, 5vw, 2.8rem); font-weight: 800; color: #1a2e4a; line-height: 1.2; margin-bottom: 18px; }}
    .hero p {{ font-size: 1.15rem; color: #374151; max-width: 640px; margin: 0 auto 32px; }}
    .btn {{ display: inline-block; background: #f97316; color: #fff; font-size: 1.2rem; font-weight: 700; padding: 16px 40px; border-radius: 6px; text-decoration: none; transition: background 0.2s; letter-spacing: 0.01em; }}
    .btn:hover {{ background: #ea6c0a; }}
    .btn-sub {{ display: block; margin-top: 10px; font-size: 0.9rem; color: #6b7280; }}
    section {{ padding: 52px 0; }}
    section:nth-child(even) {{ background: #f9fafb; }}
    section h2 {{ font-size: clamp(1.4rem, 3.5vw, 2rem); font-weight: 700; color: #1a2e4a; margin-bottom: 20px; }}
    section p {{ font-size: 1.05rem; color: #374151; max-width: 720px; }}
    section p + p {{ margin-top: 14px; }}
    .remove-grid {{ display: grid; grid-template-columns: repeat(auto-fill, minmax(220px, 1fr)); gap: 10px; margin-top: 4px; }}
    .remove-grid li {{ list-style: none; display: flex; align-items: center; gap: 10px; font-size: 1rem; color: #374151; background: #fff; border: 1px solid #e5e7eb; padding: 12px 16px; border-radius: 6px; }}
    .remove-grid li::before {{ content: "\\2713"; color: #f97316; font-weight: 700; font-size: 1.1rem; flex-shrink: 0; }}
    .why-list {{ display: flex; flex-direction: column; gap: 14px; margin-top: 4px; }}
    .why-item {{ display: flex; align-items: flex-start; gap: 12px; }}
    .why-icon {{ background: #1a2e4a; color: #fff; border-radius: 50%; width: 32px; height: 32px; display: flex; align-items: center; justify-content: center; font-size: 0.9rem; font-weight: 700; flex-shrink: 0; margin-top: 2px; }}
    .why-item p {{ font-size: 1rem; }}
    .why-item strong {{ display: block; color: #1a2e4a; font-size: 1.05rem; margin-bottom: 2px; }}
    .contact-box {{ background: #1a2e4a; color: #fff; border-radius: 10px; padding: 40px 36px; text-align: center; max-width: 580px; }}
    .contact-box h2 {{ color: #fff; margin-bottom: 10px; }}
    .contact-box p {{ color: #cbd5e1; margin-bottom: 24px; }}
    .contact-phone {{ display: block; font-size: 2rem; font-weight: 800; color: #f97316; text-decoration: none; margin-bottom: 20px; letter-spacing: 0.02em; }}
    .contact-phone:hover {{ text-decoration: underline; }}
    .contact-note {{ font-size: 0.9rem; color: #94a3b8; margin-top: 12px; }}
    .back-link {{ display: inline-block; margin-top: 20px; font-size: 0.95rem; color: #1a2e4a; text-decoration: none; }}
    .back-link:hover {{ text-decoration: underline; }}
    footer {{ background: #111827; color: #9ca3af; text-align: center; padding: 24px 20px; font-size: 0.9rem; }}
    footer a {{ color: #9ca3af; text-decoration: none; }}
    footer a:hover {{ color: #fff; }}
    @media (max-width: 540px) {{ .hero {{ padding: 44px 0 40px; }} .contact-box {{ padding: 28px 20px; }} .contact-phone {{ font-size: 1.6rem; }} }}

    /* ── PHOTO BLOCKS ── */
    .photo-row {{ display:grid; grid-template-columns:repeat(3,1fr); gap:14px; margin:28px 0; }}
    .photo-row-2 {{ display:grid; grid-template-columns:1fr 1fr; gap:14px; margin:28px 0; }}
    .photo-item {{ position:relative; border-radius:8px; overflow:hidden; height:220px; }}
    .photo-item img {{ width:100%; height:100%; object-fit:cover; display:block; transition:transform .3s; }}
    .photo-item:hover img {{ transform:scale(1.04); }}
    .photo-caption {{ position:absolute; bottom:0; left:0; right:0;
      background:linear-gradient(transparent,rgba(15,28,46,.88));
      color:#fff; font-size:.85rem; font-weight:700; padding:24px 12px 10px; }}
    .photo-split {{ display:grid; grid-template-columns:1fr 1fr; gap:32px; align-items:center; margin:28px 0; }}
    .photo-split .photo-item {{ height:280px; }}
    .photo-split-text h3 {{ font-size:1.15rem; font-weight:700; color:#1a2e4a; margin-bottom:8px; }}
    .photo-split-text p {{ font-size:.97rem; color:#4b5563; line-height:1.6; }}
    .proof-strip-sm {{ background:#f97316; padding:12px 0; margin:0; }}
    .proof-strip-sm .container {{ display:flex; flex-wrap:wrap; gap:0; justify-content:center; }}
    .proof-item-sm {{ display:flex; align-items:center; gap:7px; color:#fff;
      font-size:.88rem; font-weight:700; padding:5px 16px;
      border-right:1px solid rgba(255,255,255,.3); }}
    .proof-item-sm:last-child {{ border-right:none; }}
    .proof-item-sm::before {{ content:"✓"; font-weight:900; }}
    @media(max-width:640px) {{
      .photo-row {{ grid-template-columns:1fr; }}
      .photo-row-2 {{ grid-template-columns:1fr; }}
      .photo-split {{ grid-template-columns:1fr; }}
    }}
    @media(max-width:480px){{
      .proof-strip-sm .container {{ flex-direction:column; align-items:center; }}
      .proof-item-sm {{ border-right:none; border-bottom:1px solid rgba(255,255,255,.2); width:100%; justify-content:center; }}
      .proof-item-sm:last-child {{ border-bottom:none; }}
    }}
    .hero-phone-link {{
      display: block;
      margin-top: 18px;
      font-size: 1.35rem;
      font-weight: 800;
      color: #1a2e4a;
      text-decoration: none;
      letter-spacing: 0.01em;
    }}
    .hero-phone-link::before {{ content: "📞 "; font-size: 1rem; }}
    .hero-phone-link:hover {{ color: #f97316; }}
  </style>
</head>
<body>

  <header>
    <div class="container">
      <a class="brand" href="/"><span style="color:#fff">Chattanooga</span> <span style="color:#f97316">Junk Removal</span></a>
      <div class="header-right">
        <a class="header-phone" href="{PHONE_TEL}">{PHONE_DISPLAY}</a>
        <a class="header-cta" href="{PHONE_TEL}" style="display:inline-block;background:#f97316;color:#fff;font-weight:700;font-size:.88rem;padding:8px 14px;border-radius:5px;text-decoration:none;white-space:nowrap;">Call for a Free Quote</a>
        <button class="menu-btn" id="menuBtn" aria-label="Open menu">&#9776;</button>
      </div>
    </div>
  </header>
  <nav class="dropdown-menu" id="dropdownMenu">
    <div class="container">
      <a href="/">Home</a>
      <span class="menu-label">Services</span>
      <a href="/furniture-removal-chattanooga-tn.html">Furniture Removal</a>
      <a href="/appliance-removal-chattanooga-tn.html">Appliance Removal</a>
      <a href="/garage-cleanout-chattanooga-tn.html">Garage Cleanout</a>
      <a href="/yard-debris-removal-chattanooga-tn.html">Yard Debris Removal</a>
      <a href="/estate-cleanout-chattanooga-tn.html">Estate Cleanout</a>
      <span class="menu-label">Nearby Locations</span>
      {nearby_nav}
      <span class="menu-label">Info</span>
      <a href="/junk-removal-pricing-chattanooga-tn.html">Pricing</a>
      <a href="/contact.html">Contact</a>
    </div>
  </nav>

  <section class="hero">
    <div class="container">
      <h1>Junk Removal in {city}, {state}</h1>
      <p>{p['hero_p']}</p>
      <a class="btn" href="{PHONE_TEL}">&#128222;&nbsp; {p['hero_btn']}</a>
      <a class="hero-phone-link" href="{PHONE_TEL}">{PHONE_DISPLAY}</a>
      <span class="btn-sub">No obligation &bull; Free estimate over the phone</span>
    </div>
  </section>

  <div class="proof-strip-sm"><div class="container">{"".join(f'<div class="proof-item-sm">{item}</div>' for item in p["proof_items"])}</div></div>

  <section id="same-day">
    <div class="container">
      <h2>{p['main_h2']}</h2>
      {body_ps}
    </div>
  </section>

  <section style="padding:8px 0 48px;background:#f3f7fb;">
    <div class="container">
      <h3 style="font-size:1rem;font-weight:700;color:#1a2e4a;margin-bottom:16px;">See Us in Action in the {city} Area</h3>
      {photo_rows}
    </div>
  </section>

  <section id="what-we-remove" style="background:#f9fafb;">
    <div class="container">
      <h2>What We Haul Away in {city}</h2>
      <p style="margin-bottom:24px;">We remove almost anything from {city} homes, garages, and properties. Common items include:</p>
      <ul class="remove-grid">
        {remove_lis}
      </ul>
      <p style="margin-top:20px;">Not sure if we take it? Call us and ask — chances are we can haul it.</p>
    </div>
  </section>

  <section id="why-choose-us">
    <div class="container">
      <h2>Why {city} Residents Choose Us</h2>
      <div class="why-list">{why_items_html}
      </div>
    </div>
  </section>

  <section id="service-area" style="background:#f9fafb;">
    <div class="container">
      <h2>{city} and Surrounding Areas We Serve</h2>
      {service_area_ps}
    </div>
  </section>

  <section id="related-services">
    <div class="container">
      <h2>Related Services Near {city}</h2>
      <p>{p['related_p']}</p>
      <div class="related-grid">
        {related_links_html}
      </div>
    </div>
  </section>

  <section style="padding:8px 0 40px;">
    <div class="container">
      <div class="photo-split">
        <div class="photo-item" style="height:280px"><img src="{p['split_img']}" alt="{p['split_img_alt']}" loading="lazy" /><div class="photo-caption">{p['split_img_cap']}</div></div>
        <div class="photo-split-text">
          <h3>{p['split_text_h3']}</h3>
          <p>{p['split_text_p']}</p>
          <p style="margin-top:14px;"><a href="{PHONE_TEL}" style="color:#f97316;font-weight:700;font-size:1.05rem;">{PHONE_DISPLAY}</a></p>
        </div>
      </div>
    </div>
  </section>

  <section id="contact">
    <div class="container" style="display:flex; justify-content:center;">
      <div class="contact-box">
        <h2>{p['contact_h2']}</h2>
        <p>{p['contact_p']}</p>
        <a class="contact-phone" href="{PHONE_TEL}">{PHONE_DISPLAY}</a>
        <a class="btn" href="{PHONE_TEL}">Call for a Free Quote</a>
        <p class="contact-note">Mon–Sun: 7am – 7pm &bull; Same day appointments available</p>
      </div>
    </div>
    <div class="container" style="text-align:center;">
      <a class="back-link" href="/">&#8592; Back to Chattanooga Junk Removal Home</a>
    </div>
  </section>

  <nav class="nav-bar">
    <div class="container">
      <a href="/">Home</a>
      <a href="/{slug}.html" class="active">{city}, {state}</a>
      {nearby_nav}
    </div>
  </nav>

  <footer>
    <p>&copy; 2025 Chattanooga Junk Removal &bull; Serving {p['footer_area_label']} &amp; surrounding areas &bull; <a href="{PHONE_TEL}">{PHONE_DISPLAY}</a></p>
    <p style="margin-top:10px;"><a href="/">Home</a> &bull; <a href="/furniture-removal-chattanooga-tn.html">Furniture Removal</a> &bull; <a href="/junk-removal-pricing-chattanooga-tn.html">Pricing</a> &bull; <a href="/contact.html">Contact</a> &bull; {"&bull; ".join(f'<a href="{n[0]}">{n[1]}</a> ' for n in p["nearby_pages"])}</p>
  </footer>

  <script>
    var btn = document.getElementById('menuBtn');
    var menu = document.getElementById('dropdownMenu');
    btn.addEventListener('click', function(e) {{ e.stopPropagation(); menu.classList.toggle('open'); }});
    document.addEventListener('click', function() {{ menu.classList.remove('open'); }});
  </script>
</body>
</html>"""


# ── Write all pages ───────────────────────────────────────────────────────────

os.makedirs("public", exist_ok=True)

generated = []
for p in PAGES:
    html = build_page(p)
    path = f"public/{p['slug']}.html"
    with open(path, "w") as f:
        f.write(html)
    generated.append((p['slug'], p['city'], p['state']))
    print(f"  ✓  {path}")

print(f"\nGenerated {len(generated)} pages.")

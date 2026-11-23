#!/usr/bin/env python3
"""Render the Monday 23 November 2026 front page (1024x1024 PNG).

Drawn locally with Pillow. The graded program (main.py) does NOT run this
script: it copies the committed entry.png byte-for-byte, so the sandbox run
needs no network and no third-party packages. This script is kept in the
repo so anyone can see exactly how the image was drawn.
"""
from PIL import Image, ImageDraw, ImageFont

W, H = 1024, 1024
SERIF_B = "/usr/share/fonts/truetype/dejavu/DejaVuSerif-Bold.ttf"
SANS_B = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
SANS = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"

REGION_COLORS = {
    "N. AMERICA": (31, 78, 121),
    "LATIN AMERICA": (46, 125, 50),
    "EUROPE": (106, 27, 154),
    "MIDDLE EAST": (183, 28, 28),
    "AFRICA": (230, 81, 0),
    "SOUTH ASIA": (0, 105, 92),
    "E. ASIA & PACIFIC": (180, 120, 0),
}

# (headline, summary, region, lon, lat) — every story happened or was first
# reported on Monday 23 November 2026, per Reuters/AP/AFP/CNN/The Hindu/BBC.
STORIES = [
    ("Democrats win 258 House seats",
     "Biggest House majority since 1992 as Hubbard beats Foxx in N. Carolina.",
     "N. AMERICA", -77, 39),
    ("US-Iran war widens to Saudi, Bahrain",
     "Houthis claim refinery and radar strikes; Iran claims hits on US bases.",
     "MIDDLE EAST", 47, 26),
    ("Iran claims strikes on US bases",
     "IRGC says it hit Patriot radars in Bahrain; 2 people hurt, US says no impact.",
     "MIDDLE EAST", 50, 26),
    ("Liverpool 4-0 Man Utd",
     "Pochettino's debut is a nightmare: Yoro sent off in 8th minute at Anfield.",
     "EUROPE", -3, 53),
    ("NATO emergency talks on Poland",
     "Poland says three Russian Kh-101 missiles fell on its soil on Friday.",
     "EUROPE", 21, 52),
    ("14 missing after Kyiv-region strike",
     "Russian drone hits a block of flats in Dymer; rescuers dig through rubble.",
     "EUROPE", 31, 50),
    ("Odesa grid crippled; schools remote",
     "Russian strikes cut power, heat and water; schools go online 23-27 Nov.",
     "EUROPE", 31, 46),
    ("Russian warship hit at Benghazi",
     "Corvette Merkury is severely damaged by suspected Ukrainian sea drones.",
     "AFRICA", 20, 32),
    ("Russian ship still burning off Finland",
     "Cargo ship Sparta II, hit by drones in the Baltic, is towed from Finnish waters.",
     "EUROPE", 24, 60),
    ("Netanyahu-Eisenkot talks fail",
     "Second round of coalition talks ends with no deal on an Israeli government.",
     "MIDDLE EAST", 35, 32),
    ("Settler arson hits five villages",
     "Cars and homes set alight in the West Bank; Eisenkot calls it 'Jewish terrorism'.",
     "MIDDLE EAST", 35, 32),
    ("24 civilians killed in S. Sudan",
     "Fresh violence leaves 24 dead, UN and local officials report.",
     "AFRICA", 32, 5),
    ("Drones kill 4 near Khartoum",
     "Strikes blamed on the RSF hit homes and damage a UN building in Sudan.",
     "AFRICA", 32, 16),
    ("Indonesia factory fire: 24 bodies found",
     "Search resumes at the Serang candy factory; dozens of workers still missing.",
     "E. ASIA & PACIFIC", 106, -6),
    ("Nepal PM holds talks with Modi",
     "Balendra Shah, on a state visit to Delhi, reviews energy and border ties.",
     "SOUTH ASIA", 77, 29),
    ("India posts record 720/9 declared",
     "Record Test total in Wellington as India push for a win over New Zealand.",
     "SOUTH ASIA", 175, -41),
    ("S. Korea minister quits in AI scandal",
     "Education minister resigns amid an AI-driven exam cheating scandal.",
     "E. ASIA & PACIFIC", 127, 37),
    ("UN to keep talking on killer robots",
     "Nations agree to continue negotiations on lethal autonomous weapons.",
     "EUROPE", 6, 46),
    ("Bolsonaro 'stable' in intensive care",
     "Brazil's ex-president remains in hospital, his office says.",
     "LATIN AMERICA", -48, -16),
    ("Peru quake 6.7 kills 1, injures 16",
     "Andean tremor rattles Lima and shakes buildings across the region.",
     "LATIN AMERICA", -75, -10),
    ("Haiti police kill 34 in gang raid",
     "At least 34 suspected gang members killed in a raid on Martissant district.",
     "LATIN AMERICA", -72, 19),
    ("Mexico captures cartel boss",
     "'El Chapo Isidro' seized after Sinaloa firefights leave 11 people dead.",
     "LATIN AMERICA", -107, 25),
    ("Nvidia chip scandal grows",
     "Bessent demands answers on how AI chips reached China; SEC probe reported.",
     "N. AMERICA", -122, 37),
    ("Trump orders contractors to check in",
     "Executive order routes Congress information requests through the White House.",
     "N. AMERICA", -77, 39),
    ("ICE detains father and daughter",
     "Pair held at Seattle airport while travelling to a family baptism, lawyer says.",
     "N. AMERICA", -122, 48),
    ("9 shot at California concert",
     "Gunfire at a central California concert leaves 9 hurt, one critically.",
     "N. AMERICA", -120, 37),
    ("Denmark foils 'Russian plot'",
     "Alleged plan to kill rapper Kyivstoner foiled; Moscow defence attache expelled.",
     "EUROPE", 12, 56),
    ("Thousands march in Lisbon",
     "Protesters take to the streets as living costs fuel anger in Portugal.",
     "EUROPE", -9, 39),
    ("Sindarov gets White in Game 1",
     "Chess: Uzbek challenger draws White for the opener vs champion Gukesh, Geneva.",
     "EUROPE", 6, 46),
    ("WHO pleads for peace near Ebola zone",
     "Fighting in DR Congo disrupts the response around the Ebola outbreak area.",
     "AFRICA", 25, 0),
    ("Nigeria: 35 killed; boat capsizes",
     "Revenge attacks kill 35 Fulani in Kano; funeral boat sinks in Bayelsa, 4 dead.",
     "AFRICA", 8, 9),
    ("Two tankers hit near Hormuz",
     "UKMTO reports projectiles strike tankers off Oman; no casualties reported.",
     "MIDDLE EAST", 57, 26),
    ("Pakistan seeks Indus Waters talks",
     "Islamabad asks Delhi for an invitation to discuss the Indus Waters Treaty.",
     "SOUTH ASIA", 73, 33),
    ("Pilgrim bus crash kills 9 in India",
     "Vehicle carrying pilgrims rams a truck in Rajasthan's Kota district.",
     "SOUTH ASIA", 76, 26),
]

# Rough continent outlines (lon, lat) for the map strip.
CONTINENTS = [
    [(-168, 66), (-140, 70), (-120, 72), (-95, 80), (-85, 80), (-75, 72),
     (-65, 60), (-55, 52), (-60, 47), (-70, 44), (-75, 39), (-80, 32),
     (-81, 26), (-90, 21), (-97, 16), (-92, 15), (-83, 9), (-79, 9),
     (-86, 13), (-92, 15), (-97, 16), (-105, 20), (-110, 23), (-114, 29),
     (-120, 34), (-125, 40), (-124, 48), (-135, 58), (-150, 60), (-165, 60)],
    [(-79, 9), (-77, 4), (-80, -3), (-81, -6), (-77, -12), (-72, -18),
     (-70, -23), (-70, -33), (-73, -44), (-70, -52), (-66, -55), (-65, -45),
     (-62, -39), (-57, -34), (-52, -32), (-48, -27), (-41, -22), (-35, -9),
     (-35, -6), (-44, -3), (-50, 0), (-53, 4), (-60, 8), (-70, 11),
     (-75, 10)],
    [(-17, 15), (-17, 21), (-10, 31), (-5, 35), (10, 37), (11, 34),
     (20, 32), (32, 31), (35, 28), (39, 21), (43, 12), (51, 11),
     (48, 10), (44, 0), (40, -10), (40, -18), (36, -26), (32, -29),
     (28, -33), (20, -35), (17, -32), (14, -22), (12, -17), (13, -10),
     (9, 4), (4, 6), (-8, 5), (-13, 8)],
    [(-10, 36), (-9, 43), (-2, 48), (0, 50), (5, 53), (8, 57), (12, 60),
     (18, 62), (21, 65), (25, 70), (31, 70), (32, 66), (40, 68), (45, 66),
     (42, 60), (38, 55), (35, 52), (30, 50), (28, 46), (23, 40), (26, 38),
     (23, 36), (19, 40), (15, 44), (12, 44), (8, 44), (3, 43), (-2, 37),
     (-6, 36)],
    [(40, 68), (50, 69), (60, 69), (70, 72), (80, 73), (90, 75), (100, 77),
     (110, 74), (120, 73), (130, 72), (140, 72), (150, 70), (160, 69),
     (170, 66), (178, 65), (170, 62), (162, 60), (158, 53), (150, 59),
     (142, 55), (140, 50), (135, 43), (130, 42), (127, 40), (122, 38),
     (120, 32), (122, 28), (118, 25), (110, 20), (108, 12), (105, 9),
     (103, 7), (100, 8), (98, 12), (95, 16), (92, 21), (90, 22),
     (86, 20), (82, 17), (80, 13), (77, 8), (75, 12), (72, 20),
     (68, 23), (66, 25), (61, 25), (58, 26), (56, 27), (52, 28),
     (50, 29), (48, 30), (44, 29), (40, 32), (36, 36), (36, 38),
     (33, 40), (30, 41), (28, 41), (24, 42), (22, 44), (24, 47),
     (28, 50), (32, 54), (36, 58), (38, 62)],
    [(113, -22), (114, -30), (115, -35), (120, -34), (124, -33), (129, -32),
     (132, -32), (135, -35), (138, -35), (140, -38), (145, -38), (150, -37),
     (153, -32), (153, -27), (150, -23), (146, -19), (142, -15), (142, -11),
     (140, -17), (136, -15), (135, -12), (132, -11), (130, -13), (126, -14),
     (122, -17), (118, -20)],
    [(-58, 64), (-52, 60), (-45, 60), (-40, 64), (-32, 68), (-25, 70),
     (-20, 74), (-22, 76), (-30, 78), (-45, 80), (-58, 76), (-62, 74)],
]


def wrap(draw, text, font, width):
    words = text.split()
    lines, cur = [], ""
    for w in words:
        trial = (cur + " " + w).strip()
        if draw.textlength(trial, font=font) <= width:
            cur = trial
        else:
            if cur:
                lines.append(cur)
            cur = w
    if cur:
        lines.append(cur)
    return lines


def main():
    img = Image.new("RGB", (W, H), "white")
    d = ImageDraw.Draw(img)
    f_title = ImageFont.truetype(SERIF_B, 58)
    f_date = ImageFont.truetype(SANS_B, 26)
    f_sub = ImageFont.truetype(SANS_B, 15)
    f_lead_h = ImageFont.truetype(SANS_B, 34)
    f_lead_s = ImageFont.truetype(SANS, 17)
    f_head = ImageFont.truetype(SANS_B, 13)
    f_body = ImageFont.truetype(SANS, 11)
    f_tag = ImageFont.truetype(SANS_B, 9)
    f_map = ImageFont.truetype(SANS_B, 11)
    f_foot = ImageFont.truetype(SANS, 11)
    black = (15, 15, 15)
    grey = (90, 90, 90)
    red = (183, 28, 28)

    # ---- Masthead ----
    d.text((512, 8), "THE WORLD IN ONE DAY", font=f_title, fill=black, anchor="ma")
    d.line([(14, 78), (1010, 78)], fill=black, width=3)
    d.text((512, 84), "MONDAY 23 NOVEMBER 2026", font=f_date, fill=red, anchor="ma")
    d.text((512, 116), "35 STORIES  •  7 REGIONS  •  EVERY STORY REPORTED TODAY",
           font=f_sub, fill=black, anchor="ma")
    d.line([(14, 140), (1010, 140)], fill=black, width=2)

    # ---- Lead story: COP31 ----
    ly = 150
    d.rectangle([14, ly, 1010, ly + 102], fill=(253, 238, 238), outline=red, width=2)
    d.text((28, ly + 8), "LEAD  •  CLIMATE  •  ANTALYA, TURKEY",
           font=f_tag, fill=red)
    d.text((28, ly + 26), "COP31 COLLAPSES: NO CLIMATE DEAL",
           font=f_lead_h, fill=black)
    lead_lines = wrap(d,
        "After the longest talks ever, 194 nations reject the Antalya Pact — its draft named no fossil fuels. The EU and island states said no: first failure since 2009.",
        f_lead_s, 950)
    for j, ln in enumerate(lead_lines[:2]):
        d.text((28, ly + 64 + j * 19), ln, font=f_lead_s, fill=(40, 40, 40))

    # ---- World map strip ----
    my0, my1 = 262, 374
    d.text((14, my0), "THE DAY ON THE MAP — 35 STORIES, 7 REGIONS",
           font=f_map, fill=black)
    mx0, mx1 = 14, 1010
    lon0, lon1, lat0, lat1 = -170, 190, 82, -58
    def proj(lon, lat):
        x = mx0 + (lon - lon0) / (lon1 - lon0) * (mx1 - mx0)
        y = (my0 + 20) + (lat0 - lat) / (lat0 - lat1) * (my1 - my0 - 20)
        return x, y
    for poly in CONTINENTS:
        pts = [proj(lon, lat) for lon, lat in poly]
        d.polygon(pts, fill=(214, 226, 235), outline=(90, 110, 130))
    for headline, _s, region, lon, lat in STORIES:
        x, y = proj(lon, lat)
        c = REGION_COLORS[region]
        d.ellipse([x - 5, y - 5, x + 5, y + 5], fill=c, outline="white", width=1)
    # COP31 dot (Antalya)
    x, y = proj(30, 37)
    d.ellipse([x - 6, y - 6, x + 6, y + 6], fill=red, outline="white", width=1)

    # ---- Story grid: 34 stories, 5 cols x 7 rows ----
    gx0, gy0 = 14, 384
    cols, rows = 5, 7
    cw = (1010 - gx0 - (cols - 1) * 6) // cols
    gh = (990 - gy0 - (rows - 1) * 6) // rows
    for i, (headline, summary, region, _lon, _lat) in enumerate(STORIES):
        r, c = divmod(i, cols)
        x0 = gx0 + c * (cw + 6)
        y0 = gy0 + r * (gh + 6)
        col = REGION_COLORS[region]
        d.rectangle([x0, y0, x0 + cw, y0 + gh], outline=(200, 200, 200), width=1)
        d.rectangle([x0, y0, x0 + cw, y0 + 3], fill=col)
        d.text((x0 + 6, y0 + 5), region, font=f_tag, fill=col)
        lines = wrap(d, headline, f_head, cw - 12)[:2]
        yy = y0 + 17
        for ln in lines:
            d.text((x0 + 6, yy), ln, font=f_head, fill=black)
            yy += 13
        slines = wrap(d, summary, f_body, cw - 12)[:3]
        for ln in slines:
            d.text((x0 + 6, yy), ln, font=f_body, fill=(50, 50, 50))
            yy += 11
    # Last cell: the day in numbers
    x0 = gx0 + 4 * (cw + 6)
    y0 = gy0 + 6 * (gh + 6)
    d.rectangle([x0, y0, x0 + cw, y0 + gh], fill=(15, 15, 15))
    d.text((x0 + 6, y0 + 6), "THE DAY IN NUMBERS", font=f_tag, fill=(255, 200, 60))
    for j, ln in enumerate(["194 nations at COP31",
                            "258 House seats for Democrats",
                            "24 bodies found in Serang",
                            "4-0 at Anfield"]):
        d.text((x0 + 6, y0 + 21 + j * 13), ln, font=f_body, fill="white")

    # ---- Footer ----
    d.line([(14, 994), (1010, 994)], fill=black, width=1)
    d.text((512, 1000),
           "Every story above happened or was first reported on Monday 23 November 2026  •  Sources: Reuters, AP, AFP, CNN, The Hindu, BBC, Al Jazeera",
           font=f_foot, fill=grey, anchor="ma")
    img.save("entry.png", optimize=True)
    print("saved entry.png")


if __name__ == "__main__":
    main()

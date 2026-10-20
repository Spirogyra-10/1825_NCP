with open('1825_NCP.kicad_pcb', 'r', encoding='utf-8') as f:
    text = f.read()

import re
from shapely.geometry import Polygon, box

# find all filled_polygons
# Format in KiCad PCB: (filled_polygon (layer "B.Cu") (pts (xy X Y) ...))
matches = re.findall(r'\(filled_polygon\s+\(layer\s+"B.Cu"\)\s+\(pts([\s\S]*?)\)\s*\)', text)
print(f"Total B.Cu filled polygons in PCB: {len(matches)}")

p1_box = box(169.9392 - 0.4, 79.6544 - 0.475, 169.9392 + 0.4, 79.6544 + 0.475)
p2_box = box(171.5892 - 0.4, 79.6544 - 0.475, 171.5892 + 0.4, 79.6544 + 0.475)

for i, pts_str in enumerate(matches):
    pts = re.findall(r'\(xy\s+([-\d\.]+)\s+([-\d\.]+)\)', pts_str)
    coords = [(float(x), float(y)) for x, y in pts]
    if len(coords) >= 3:
        poly = Polygon(coords)
        if poly.intersects(p1_box):
            print(f"CRITICAL: Pad 1 INTERSECTS polygon {i}!")
        d1 = poly.distance(p1_box)
        d2 = poly.distance(p2_box)
        if d1 < 1.0 or d2 < 1.0:
            print(f"Polygon {i}: dist to P1 = {d1:.4f} mm, dist to P2 = {d2:.4f} mm")


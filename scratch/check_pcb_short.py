with open('1825_NCP.kicad_pcb', 'r', encoding='utf-8') as f:
    text = f.read()

import re

# Find all zones in the board
zones = re.findall(r'\(zone\s+[\s\S]*?\n\t\)', text)
print(f"Total zones: {len(zones)}")
for i, z in enumerate(zones):
    net_m = re.search(r'\(net\s+"?([^"\)]+)"?\)', z)
    layers_m = re.search(r'\(layers\s+([^\)]+)\)', z)
    net = net_m.group(1) if net_m else "?"
    layers = layers_m.group(1) if layers_m else "?"
    print(f"Zone {i}: net={net}, layers={layers}")

# Check tracks near R9 (at 170.7642, 79.6544)
# Let's find all segments on B.Cu near (170, 79)
segments = re.findall(r'\(segment\s+\(start\s+([-\d\.]+)\s+([-\d\.]+)\)\s+\(end\s+([-\d\.]+)\s+([-\d\.]+)\)\s+\(width\s+([-\d\.]+)\)\s+\(layer\s+"([^"]+)"\)\s+\(net\s+"?([^"\)]+)"?\)', text)
print(f"Total segments: {len(segments)}")

print("\nSegments on B.Cu near R9 (x: 168-173, y: 77-82):")
for start_x, start_y, end_x, end_y, width, layer, net in segments:
    sx, sy, ex, ey = float(start_x), float(start_y), float(end_x), float(end_y)
    if layer == "B.Cu" and (168 <= sx <= 173 or 168 <= ex <= 173) and (77 <= sy <= 82 or 77 <= ey <= 82):
        print(f"Segment: ({sx:.2f}, {sy:.2f}) -> ({ex:.2f}, {ey:.2f}), width={width}, net={net}")


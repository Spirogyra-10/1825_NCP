with open('1825_NCP.kicad_pcb', 'r', encoding='utf-8') as f:
    text = f.read()

import re

# find all tracks on B.Cu and F.Cu for /PGOOD
pgood_segments = []
for m in re.finditer(r'\(segment\s+\(start\s+([-\d\.]+)\s+([-\d\.]+)\)\s+\(end\s+([-\d\.]+)\s+([-\d\.]+)\)\s+\(width\s+([-\d\.]+)\)\s+\(layer\s+"([^"]+)"\)\s+\(net\s+"?/PGOOD"?\)', text):
    pgood_segments.append(m.groups())

print(f"PGOOD segments: {len(pgood_segments)}")
for s in pgood_segments:
    print(s)

# find all vias for /PGOOD
pgood_vias = []
for m in re.finditer(r'\(via\s+\(at\s+([-\d\.]+)\s+([-\d\.]+)\)\s+\(size\s+([-\d\.]+)\)\s+\(drill\s+([-\d\.]+)\)\s+\(layers\s+([^\)]+)\)\s+\(net\s+"?/PGOOD"?\)', text):
    pgood_vias.append(m.groups())

print(f"PGOOD vias: {len(pgood_vias)}")
for v in pgood_vias:
    print(v)


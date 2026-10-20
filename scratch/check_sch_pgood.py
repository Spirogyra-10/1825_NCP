with open('1825_NCP.kicad_sch', 'r', encoding='utf-8') as f:
    text = f.read()

import re

# find all occurrences of PGOOD in schematic
lines = text.splitlines()
print("Schematic lines with PGOOD:")
for i, line in enumerate(lines):
    if 'PGOOD' in line and not line.strip().startswith('(name "PGOOD"') and not line.strip().startswith('(pin "PGOOD"'):
        print(f"Line {i+1}: {line}")

# find all labels with PGOOD
labels = re.findall(r'\((?:label|global_label|hierarchical_label)\s+"[^"]*PGOOD[^"]*"[\s\S]*?\)', text)
print(f"PGOOD Labels: {len(labels)}")
for l in labels:
    print(l)


import re
from collections import defaultdict

with open("1825_NCP.kicad_pcb", "r", encoding="utf-8") as f:
    content = f.read()

# Extract footprints
# A rough parser for kicad_pcb footprints
fp_pattern = re.compile(r'\(footprint\s+"([^"]+)"[\s\S]*?\n\t\)', re.MULTILINE)
# Better: parse footprint blocks
footprints = []
idx = 0
while True:
    start = content.find('(footprint ', idx)
    if start == -1:
        break
    # find matching parenthesis
    depth = 0
    i = start
    while i < len(content):
        if content[i] == '(':
            depth += 1
        elif content[i] == ')':
            depth -= 1
            if depth == 0:
                footprints.append(content[start:i+1])
                idx = i + 1
                break
        i += 1
    else:
        break

net_to_pads = defaultdict(list)
comp_to_pads = defaultdict(dict)

for fp in footprints:
    ref_m = re.search(r'\(property "Reference" "([^"]+)"', fp)
    val_m = re.search(r'\(property "Value" "([^"]+)"', fp)
    ref = ref_m.group(1) if ref_m else "?"
    val = val_m.group(1) if val_m else ""
    
    # find pads: (pad "num" ... (net "netname" ...)) or (net N "netname")
    pads = re.findall(r'\(pad\s+"([^"]+)"\s+[^\n]+[\s\S]*?\(net\s+(?:\d+\s+)?"([^"]+)"', fp)
    for pad_num, net in pads:
        net_to_pads[net].append(f"{ref}.{pad_num}")
        comp_to_pads[ref][pad_num] = (net, val)

print("=== NET LIST SUMMARY ===")
for net in sorted(net_to_pads.keys()):
    pads_str = ", ".join(sorted(set(net_to_pads[net])))
    print(f"Net: {net:25} -> {pads_str}")

print("\n=== COMPONENT CONNECTIONS ===")
for ref in sorted(comp_to_pads.keys(), key=lambda x: (x[0], int(x[1:]) if x[1:].isdigit() else 999)):
    val = list(comp_to_pads[ref].values())[0][1] if comp_to_pads[ref] else ""
    pads = comp_to_pads[ref]
    pads_desc = ", ".join([f"{p}:{n}" for p, (n, _) in sorted(pads.items(), key=lambda x: int(x[0]) if x[0].isdigit() else 999)])
    print(f"{ref:6} ({val:10}): {pads_desc}")


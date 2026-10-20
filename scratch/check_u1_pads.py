with open('1825_NCP.kicad_pcb', 'r', encoding='utf-8') as f:
    text = f.read()

import re

# find U1 footprint and pads 20, 21, 22, 23, 24
idx = text.find('(property "Reference" "U1"')
start = text.rfind('(footprint ', 0, idx)
end = text.find('\n\t)', idx)
u1_text = text[start:end+3]

pads = re.findall(r'\(pad\s+"(\d+)"[^\n]+[\s\S]*?\(net\s+(?:\d+\s+)?"([^"]+)"', u1_text)
for p, net in pads:
    if int(p) in [19, 20, 21, 22, 23, 24, 25]:
        print(f"U1 Pad {p}: net={net}")


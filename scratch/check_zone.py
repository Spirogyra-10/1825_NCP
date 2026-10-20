with open('1825_NCP.kicad_pcb', 'r', encoding='utf-8') as f:
    text = f.read()

import re

# Let's inspect Zone 1 (+5V)
idx = text.find('(net "+5V")')
# Find the zone block for +5V
zone_starts = [m.start() for m in re.finditer(r'\(zone\s+', text)]
for zs in zone_starts:
    # get next 500 chars
    snippet = text[zs:zs+500]
    if '"+5V"' in snippet:
        # find end of zone
        depth = 0
        ze = zs
        while ze < len(text):
            if text[ze] == '(':
                depth += 1
            elif text[ze] == ')':
                depth -= 1
                if depth == 0:
                    break
            ze += 1
        zone_text = text[zs:ze+1]
        print("Zone snippet:")
        print(zone_text[:600])
        # check min_clearance, etc.
        m_clr = re.search(r'\(clearance\s+([-\d\.]+)\)', zone_text)
        print("Clearance:", m_clr.group(1) if m_clr else "default")


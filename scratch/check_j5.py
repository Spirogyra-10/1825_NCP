with open('1825_NCP.kicad_pcb', 'r', encoding='utf-8') as f:
    text = f.read()

import re

# find J5
idx = text.find('(property "Reference" "J5"')
start = text.rfind('(footprint ', 0, idx)
end = text.find('\n\t)', idx)

print("J5 Footprint:")
print(text[start:end+3])


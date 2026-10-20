with open('1825_NCP.kicad_pcb', 'r', encoding='utf-8') as f:
    text = f.read()

import re

# find footprint containing Reference R9
# Walk backwards from idx to find (footprint
idx = text.find('(property "Reference" "R9"')
start = text.rfind('(footprint ', 0, idx)
end = text.find('\n\t)', idx)

fp_text = text[start:end+3]
print("Footprint header & pads:")
print(fp_text[:2000])


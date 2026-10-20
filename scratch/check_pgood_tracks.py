with open('1825_NCP.kicad_pcb', 'r', encoding='utf-8') as f:
    text = f.read()

import re

for line in text.splitlines():
    if '/PGOOD' in line:
        print(line)


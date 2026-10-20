import sys
sys.stdout.reconfigure(encoding='utf-8')
with open('scratch/extracted_pdf_text.txt', 'r', encoding='utf-8') as f:
    text = f.read()

import re

# Search for startup sequence, programming detection
matches = [m.start() for m in re.finditer(r'programming|detection|startup|start-up|sequence', text, re.IGNORECASE)]
print(f"Matches: {len(matches)}")
for i, m in enumerate(matches[:10]):
    print(f"--- {i} ---")
    print(text[max(0, m-100):min(len(text), m+400)].replace('\n', ' '))


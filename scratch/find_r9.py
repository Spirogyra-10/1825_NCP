with open('1825_NCP.kicad_pcb', 'r', encoding='utf-8') as f:
    text = f.read()

idx = text.find('(property "Reference" "R9"')
if idx != -1:
    print(text[idx-200:idx+2500])


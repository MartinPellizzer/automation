from fpdf import FPDF

pdf = FPDF(orientation='P', unit='pt', format='A4')
pdf.add_page()

pdf.image('logo.jpeg', w=80, h=80)

pdf.set_font(family='Times', style='B', size=24)
pdf.cell(w=0, h=50, txt='Offerta', align='C', border=1, ln=1)

pdf.set_font(family='Times', style='B', size=14)
pdf.cell(w=0, h=15, txt='Description', ln=1)
pdf.set_font(family='Times', size=12)
content = '''
Lorem ipsum dolor sit amet, consectetur adipiscing elit. Quisque euismod, erat vitae tincidunt congue, mi felis varius nisi, quis consectetur nibh ipsum ac urna. Pellentesque iaculis erat massa, in accumsan sapien tempor vel. Orci varius natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Duis convallis enim nisi. Donec imperdiet varius mi non pharetra. Aliquam sit amet dictum sapien. Pellentesque orci eros, malesuada ac tristique non, finibus ut risus.
'''
pdf.multi_cell(w=0, h=15, txt=content)


pdf.set_font(family='Times', style='B', size=14)
pdf.cell(w=100, h=25, txt='Kindom:')

pdf.set_font(family='Times', size=14)
pdf.cell(w=100, h=25, txt='Animalia', ln=1)



pdf.set_font(family='Times', style='B', size=14)
pdf.cell(w=100, h=25, txt='ABC:')

pdf.set_font(family='Times', size=14)
pdf.cell(w=100, h=25, txt='DEF', ln=1)



pdf.output('output.pdf')

import os
os.system('output.pdf')
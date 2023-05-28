from fpdf import FPDF


def format_to_pdf(list_ingr):
    pdf = FPDF()
    pdf.add_page()
    pdf.add_font('DejaVu', '', './recipes/font/DejaVuSansCondensed.ttf', uni=True)
    pdf.set_font('Dejavu', size=14)
    pdf.cell(txt='Список покупок', center=True)
    for i, ingridient in enumerate(list_ingr):
        name = list_ingr['ingridient__name']
        unit = list_ingr['ingridient__measurement__unit']
        amount = list_ingr['amount__sum']
        pdf.cell(40, 10, f'{i + 1}{name} - {amount} {unit}')
        pdf.ln()
    return pdf.output(dest='S')
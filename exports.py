''' Module d'export en html, etc ... '''

from jinja2 import Environment, FileSystemLoader
from generation_donnees import generateInvoice
from facture import Invoice

env = Environment( loader=FileSystemLoader('templates') )


def generateHtml(inv:Invoice):
    template = env.get_template ('invoice.html')
    return template.render(myInvoice=inv)


def generateTestHtml():
    # récupération d'une facture
    f = generateInvoice()
    print(f'Facturé générée : {f}')
    return generateHtml(f)


def generatePdf(content, filename):
    from weasyprint import HTML, CSS
    from weasyprint.fonts import FontConfiguration

    font_conf = FontConfiguration()
    html = HTML(string=content)
    html.write_pdf(filename, font_config=font_conf)


if __name__== '__main__':
    import pathlib
    h = generateTestHtml()
    print(h)
    generatePdf(h,'./invoice.pdf')
    pathlib.Path('./invoice.html').write_text(h)


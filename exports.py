''' Module d'export en html, etc ... '''

from jinja2 import Environment, FileSystemLoader
from generation_donnees import generateInvoice
from facture import Invoice

env = Environment( loader=FileSystemLoader('templates') )

def generateHtml(inv:Invoice):
    template = env.get_template ('invoice.html')
    print(template.render(myInvoice=inv))

def generateTestHtml():
    # récupération d'une facture
    f = generateInvoice()
    print(f'Facturé générée : {f}')
    generateHtml(f)

if __name__== '__main__':
    generateTestHtml()
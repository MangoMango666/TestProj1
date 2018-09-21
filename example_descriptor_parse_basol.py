"""
    Exemple d'utilisation des descripteurs, basé sur le parsing de BASOL
"""
import datetime

import bs4
import pathlib
import prettyprinter as pp

# page html préalablement téléchargée et sauvegardée en local
content = pathlib.Path('./exemple_page_basol.html').read_text()
soup = bs4.BeautifulSoup(content, 'html.parser')

# pp.cpprint(soup)

# --------------- Méthode 1 : Parsing simple sans descripteur
code_basol = soup.select_one("span:nth-of-type(3)").text.strip() # récupération du code BASOL qui est le troisième <span></span> qui se présente
print(f'Code BASOL du site :{code_basol}')

# situation technique du site : TODO

# --------------- Méthode 2 : Parsing  avec descripteurs


class Page:
    def __init__(self, soupe):
        self.soup = soupe


class Field:
    def __init__(self, css_selector):
        self.css_selector = css_selector


class TextInput(Field):
    def __get__(self, page_instance, owner): # va chercher la valeur en parsant le soup à chaque appel
        #print(f'\tAppel de textInput avec {page_instance}')
        element = page_instance.soup.select_one(self.css_selector)
        return element.text.strip()

    def __set__(self, instance, value): # fonction sans utilité à part pour l'exemple
        raise AttributeError('Impossible de faire un set')


class DateInput(TextInput):
    def __get__(self, page_instance, owner):
        value = super().__get__(page_instance, owner)
        return datetime.datetime.strptime(value, "%d/%m/%Y").date()


class BasolPage(Page):
    # descripteurs: attributs de classe décrivant des champs
    code_basol = TextInput("span:nth-of-type(3)")
    region = TextInput("span:nth-of-type(1)")
    commune = TextInput("span:nth-of-type(11)")
    date_publication = DateInput("span:nth-of-type(6)")

    # la méthode __init__ utilisée est en fait celle de la super-classe Page(soup)

    def __str__(self):
        # TODO
        return 'function __str__ not implemented yet'


ma_page = BasolPage(soup)

# TODO : décommenter quand le __str__ est fini : print(f'Objet ma_page : {ma_page}\n')

print(f'Région : {ma_page.region}') # équivalent à BasolPage.region.__get__(ma_page)
print(f'Commune : {ma_page.commune}')
print(f'Code BASOL : {ma_page.code_basol}')
print(f'Date publication : {ma_page.date_publication}')


try:
    ma_page.region = 'test'
    print('On a pu écrire la région. Pas normal !')
except AttributeError as err:
    print("Impossible d'écrire la région. C'est normal.")


print(f'Région : {BasolPage.region.__get__(ma_page)}')
"""
Module pour exercice de la formation Python avance : facturier
"""

from dataclasses import dataclass
from typing import Optional

@dataclass
class Client:
    # le décorateur dataclass (Python 3.7) permet d'indiquer que la classe ne fait que contenir des données
    # et simplifie le code en générant de manière automatique __init__ et __repr__
    name: str
    address: str = ''
    phone: str = ''
    email: Optional[str] = None

class Product:
    ''' Définition d'un produit dans le catalogue. '''

    product_last_ref = 0

    def createRef():
        ''' crée le numéro de référence du produit.

        :return: la référence créée
        '''
        r = Product.product_last_ref
        Product.product_last_ref += 1
        return r

    def __init__(self, leNomProduit: str, prixUnit: float):
        assert isinstance(leNomProduit, str) and len(leNomProduit.strip()) > 0, 'Nom du produit vide'
        self.nomProduit = leNomProduit
        assert isinstance(prixUnit, float), 'prix non-float'
        self.prixUnitaire = prixUnit
        self.reference = Product.createRef()

    def __str__(self):
        return f"{self.nomProduit}, référence: {self.reference}, prix unitaire:{self.prixUnitaire}"


class InvoiceLine:
    ''' Ligne sur la facture avec un seul produit mais un nombre d'unités variable '''

    def __init__(self, unProduit: Product, nbre: int, vat:float=0.2):
        assert unProduit is not None , "produit vide !"
        self.produit = unProduit
        assert isinstance(nbre ,int) and nbre >= 0 , "nombre non-entier ou négatif: {0}".format(nbre)
        self.nombreItems = nbre
        self.vat = vat

    @property
    def montantLigne(self):
        # définir la méthode comme property permet d'appeler la méthode comme si c'était un attribut
        return self.produit.prixUnitaire * self.nombreItems


    @property
    def montantLigneTTC(self):
        # définir la méthode comme property permet d'appeler la méthode comme si c'était un attribut
        return self.montantLigne * ( 1 + self.vat)

    def __repr__(self):
        return f"Produit: {self.produit}, nombre unités={self.nombreItems}, montantHT={self.montantLigne}"


class Invoice:
    """ Instance de facture.
    """

    def __init__(self,  myClient: Client, myDefaultTVA:float=0.2):
        assert isinstance(myDefaultTVA, float), " TVA non-float, instance de " + str(type(myDefaultTVA))
        self.client = myClient
        self.defaultVAT = myDefaultTVA
        self.refFacture = Invoice.createRefFacture()
        self.lignes = []

    def addLine(self, uneLigne: InvoiceLine):
        ''' Ajoute une ligne produit dans la facture

        :param uneLigne: une ligne produit
        :return: rien
        '''
        assert uneLigne is not None, "ligne vide"
        self.lignes.append(uneLigne)

    @property
    def montantTotalHT(self) -> float :
        ''' Calcule montant HT '''
        return sum(ligne.montantLigne for ligne in self.lignes)

    @property
    def montantTotalTTC(self) ->float :
        ''' Calcule le montant TTC.

        :return: le montant TTC
        '''
        return sum(ligne.montantLigneTTC for ligne in self.lignes)

    # numéro interne incrémental de référence
    ref_number = 1

    def createRefFacture() -> str :
        ''' Crée la référence de facture

        :param self:
        :return: la référence créée (pour l'instant une valeur fixe)
        '''
        r = Invoice.ref_number
        Invoice.ref_number += 1
        return f'INV-2018/{r}'

    def __str__(self):
        return f"Facture référence={self.refFacture}, client={self.client}, montant HT={self.montantTotalHT} \
               , montant TTC={self.montantTotalTTC}, lignes:\n" + repr(self.lignes)


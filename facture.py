"""
Module pour exercice de la formation Python avance : facturier
"""

class Produit:
    ''' Définition d'un produit dans le catalogue. '''

    product_last_ref = 0

    def createRef():
        ''' crée le numéro de référence du produit.

        :return: la référence créée
        '''
        r = Produit.product_last_ref
        Produit.product_last_ref += 1
        return r

    def __init__(self, leNomProduit: str, prixUnit: float):
        self.nomProduit = leNomProduit
        self.prixUnitaire = prixUnit
        self.reference = Produit.createRef()

    def __str__(self):
        return f"{self.nomProduit}, référence: {self.reference}, prix unitaire:{self.prixUnitaire}"


class LigneFacture:
    ''' Ligne sur la facture avec un seul produit mais un nombre d'unités variable '''

    def __init__(self, unProduit: Produit, nbre: int):
        assert unProduit is not None , "produit vide !"
        self.produit = unProduit
        assert isinstance(nbre ,int) and nbre >= 0 , "nombre non-entier ou négatif: {0}".format(nbre)
        self.nombreItems = nbre

    @property
    def montantLigne(self):
        # définir la méthode comme property permet d'appeler la méthode comme si c'était un attribut
        return self.produit.prixUnitaire * self.nombreItems

    def __repr__(self):
        return f"Produit: {self.produit}, nombre unités={self.nombreItems}, montantHT={self.montantLigne}\n"


class Facture:
    """ Instance de facture.
    """

    def __init__(self, myTVA: float, myClientName: str):
        assert isinstance(myTVA,float), " TVA non-float, instance de "+str(type(myTVA))
        self.clientName = myClientName
        self.TVA = myTVA
        self.refFacture = Facture.createRefFacture()
        self.lignes = []
        self.montantTotalHT = 0.0

    def addLigne(self, uneLigne: LigneFacture):
        ''' Ajoute une ligne produit dans la facture

        :param uneLigne: une ligne produit
        :return: rien
        '''
        assert uneLigne is not None, "ligne vide"
        self.lignes.append(uneLigne)
        self.montantTotalHT += uneLigne.montantLigne

    def montantTotalTTC(self) ->float :
        ''' Calcule le montant TTC.

        :return: le montant TTC
        '''
        return self.montantTotalHT * (1 + self.TVA)

    ref_number = 1

    def createRefFacture() -> str :
        ''' Crée la référence de facture

        :param self:
        :return: la référence créée (pour l'instant une valeur fixe)
        '''
        r = Facture.ref_number
        Facture.ref_number += 1
        return f'INV-2018/{r}'

    def __str__(self):
        return f"Facture référence={self.refFacture}, client={self.clientName}, montant HT={self.montantTotalHT} \
               , montant TTC={self.montantTotalTTC()}, lignes:\n" + repr(self.lignes)


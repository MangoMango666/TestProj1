class Produit:

    def createRef(self):
        return None

    def __init__(self, leNomProduit: str, prixUnit: float):
        self.nomProduit = leNomProduit
        self.prixUnitaire = prixUnit
        self.reference = self.createRef()

    def __str__(self):
        return "Produit " + str(self.nomProduit) + " référence " + str(self.reference) + " prix unitaire=" + str(
            self.prixUnitaire)


class LigneFacture:

    def __init__(self, unProduit: Produit, nbre: int):
        assert unProduit is not None , "produit vide !"
        self.produit = unProduit
        assert isinstance(nbre ,int) and nbre >= 0 , "nombre non-entier ou négatif"
        self.nombreItems = nbre
        self.montantLigne = self.produit.prixUnitaire * self.nombreItems

    def __repr__(self):
        return "Produit : (" + str(self.produit) + ") nombre unités=" + str(self.nombreItems) + ", montant=" + str(
            self.montantLigne)


class Facture:

    def __init__(self, myTVA: float, myClientName: str):
        assert isinstance(myTVA,float), " TVA non-float, instance de "+str(type(myTVA))
        self.clientName = myClientName
        self.TVA = myTVA
        self.refFacture = self.createRefFacture()
        self.lignes = []
        self.montantTotalHT = 0.0

    def addLigne(self, uneLigne: LigneFacture):
        assert uneLigne is not None, "ligne vide"
        self.lignes.append(uneLigne)
        self.montantTotalHT += uneLigne.montantLigne

    def montantTotalTTC(self):
        return self.montantTotalHT * (1 + self.TVA)

    def createRefFacture(self):
        return 'INV-2018/0001'

    def __str__(self):
        return "Facture référence=" + str(self.refFacture) + ", client=" + str(self.clientName) + ", montant HT=" + str(
            self.montantTotalHT) \
               + ", montant TTC=" + str(self.montantTotalTTC()) + ", lignes=" + repr(self.lignes)


def testFacture():
    prod1 = Produit('vélo', 200.0)
    prod2 = Produit('tricycle', 500.0)

    maFacture = Facture(myTVA=0.2, myClientName='Toto')
    maFacture.addLigne(LigneFacture(prod1, 3))
    maFacture.addLigne(LigneFacture(prod2, 1))

    print('Facture créée : {0}'.format(maFacture))
    pass


testFacture()

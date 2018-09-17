import unittest
from facture import *

class FactureTestCase(unittest.TestCase):

    def setUp(self):
        """ appelé automatiquement en début de test """
        pass

    def tearDown(self):
        """ appelé automatiquement en fin de test """
        pass


    def testFacture(self):
        ''' Fonction de test du module

        :return: rien
        '''
        print('Début testFacture ')
        prod1 = Produit('vélo', 200.0)
        prod2 = Produit('tricycle', 500.0)
        assert prod1.nomProduit == 'vélo'
        assert prod1.prixUnitaire == 200.0

        maFacture = Facture(myTVA=0.2, myClientName='Toto')
        maFacture.addLigne(LigneFacture(prod1, 3))
        maFacture.addLigne(LigneFacture(prod2, 1))
        assert maFacture.montantTotalTTC() == 1320.0

        print('Facture créée : {0}'.format(maFacture))
        print('Fin testFacture ')


    def testFacture_fails(self):
        ''' Fonction de test qui crée volontairement des échecs '''
        print('Début testFacture_fails ')

        # test d'exception pour quantité négative
        with self.assertRaises(AssertionError):
            LigneFacture(Produit('tomate',1.0),-1)


        # test d'exception pour quantité non-entière
        with self.assertRaises(AssertionError):
            LigneFacture(Produit('tomate',1.0),1.5)

        # test d'exception pour quantité non-entière
        with self.assertRaises(AssertionError):
            Facture(myTVA='pas un numérique',myClientName='Toto')

        # test d'exception avec produit None
        with self.assertRaises(AssertionError):
            facture = Facture(myTVA=0.2, myClientName='Toto')
            facture.addLigne(LigneFacture(None,20))

        print('Fin testFacture_fails ')

if __name__ == '__main__':
    unittest.main()
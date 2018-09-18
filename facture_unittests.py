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
        ''' Fonction de test qui crée volontairement des échecs. '''
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

    def test_ref_creations(self):
        ''' Teste les créations sérialisées de référence. '''
        print('Début test_ref_creations ')

        prod1 = Produit('produit 1',10.0)
        print(f'Produit 1 : {prod1}')
        nvlle_ref = Produit.createRef()
        print('Nouvelle référence produit 1 : {0}'.format(nvlle_ref ))
        self.assertEqual(prod1.reference,nvlle_ref-1)

        ref_facture = Facture.createRefFacture()
        print(f'Numéro de facture : {ref_facture}')

        print('Fin test_ref_creations ')

if __name__ == '__main__':
    unittest.main()
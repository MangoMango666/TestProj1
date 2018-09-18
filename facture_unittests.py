import unittest
from facture import *

class FactureTestCase(unittest.TestCase):

    def setUp(self):
        """ appelé automatiquement en début de test """
        pass

    def tearDown(self):
        """ appelé automatiquement en fin de test """
        pass

    def test_produits(self):
        ''' Vérifie les règles de créatiop de produits '''

        # test nom de produit vide
        with self.assertRaises(AssertionError):
            Product(' ', 5.0)

        # test nom de produit vide
        with self.assertRaises(AssertionError):
            Product(' ghkkkj  ', 'ceci n\'est pas un float')

    def testFacture(self):
        ''' Fonction de test du module

        :return: rien
        '''
        print('Début testFacture ')
        prod1 = Product('vélo', 200.0)
        prod2 = Product('tricycle', 500.0)
        assert prod1.nomProduit == 'vélo'
        assert prod1.prixUnitaire == 200.0

        maFacture = Invoice(myDefaultTVA=0.2, myClient=Client(name='Toto'))
        maFacture.addLine(InvoiceLine(prod1, 3, 0.2))
        maFacture.addLine(InvoiceLine(prod2, 1, 0.2))
        assert maFacture.montantTotalTTC == 1320.0

        print('Facture créée : {0}'.format(maFacture))
        print('Fin testFacture ')


    def testFacture_fails(self):
        ''' Fonction de test qui crée volontairement des échecs. '''
        print('Début testFacture_fails ')

        # test d'exception pour quantité négative
        with self.assertRaises(AssertionError):
            InvoiceLine(Product('tomate', 1.0), -1, 0.1)


        # test d'exception pour quantité non-entière
        with self.assertRaises(AssertionError):
            InvoiceLine(Product('tomate', 1.0), 1.5, 0.1)

        # test d'exception pour quantité non-entière
        with self.assertRaises(AssertionError):
            Invoice(myDefaultTVA='pas un numérique', myClient=Client(name='Toto'))

        # test d'exception avec produit None
        with self.assertRaises(AssertionError):
            facture = Invoice(myDefaultTVA=0.2, myClient=Client(name='Toto'))
            facture.addLine(InvoiceLine(None, 20, 0.2))

        print('Fin testFacture_fails ')

    def test_ref_creations(self):
        ''' Teste les créations sérialisées de référence. '''
        print('Début test_ref_creations ')

        prod1 = Product('produit 1', 10.0)
        print(f'Produit 1 : {prod1}')
        nvlle_ref = Product.createRef()
        print('Nouvelle référence produit 1 : {0}'.format(nvlle_ref ))
        self.assertEqual(prod1.reference,nvlle_ref-1)

        ref_facture = Invoice.createRefFacture()
        print(f'Numéro de facture : {ref_facture}')
        ref_facture = Invoice.createRefFacture()
        print(f'Numéro de facture : {ref_facture}')
        for i in range(1,100):
            ref_facture = Invoice.createRefFacture()
        print(f'Numéro de facture : {ref_facture}')
        print('Fin test_ref_creations ')

if __name__ == '__main__':
    unittest.main()
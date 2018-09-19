''' Génération aléatoire de données (de test) '''
from faker import Faker
from faker import providers
from facture import *
import random
import factory


list_of_products_1 = ['brocolis', 'tomate','citrouille','carotte','fenouil']

fake = Faker()


class MyProvider(providers.BaseProvider):
    def product_name(self):
        return random.choice(list_of_products_1)

#    def client_name(self):
#        return fake.


factory.Faker.add_provider(MyProvider)


class ProductFactory(factory.Factory):
    # truc propre à Factory : définir la sous-classe Meta et l'attribut model
    class Meta:
        model = Product

    leNomProduit = factory.Faker('product_name')
    # inutile car la référence est déterminée dans le __ini__  de Product:
    # reference = factory.Sequence(lambda identifier: f'PRO-{identifier}')
    prixUnit = factory.Faker('pyfloat', left_digits=3, right_digits=2, positive=True)


class InvoiceLineFactory(factory.Factory):
    class Meta:
        model = InvoiceLine

    unProduit = factory.SubFactory(ProductFactory)
    nbre = factory.Faker('random_int')


class ClientFactory(factory.Factory):
    class Meta:
        model = Client

    name = factory.Faker('name')
    # TODO : address,  phone: ,  email


class EmptyInvoiceFactory(factory.Factory):
    class Meta:
            model = Invoice

    myClient = factory.SubFactory(ClientFactory)

# test du module


def generateInvoice():
    f = EmptyInvoiceFactory()
    # ajout de lignes de facture
    for i in range(1, random.randint(2, 11)):
        f.addLine(InvoiceLineFactory())
    return f


if __name__== '__main__':
    print('Génération de 10 produits :')
    for i in range (1,10):
        prod = ProductFactory()
        print(f'Produit n°{i} : ', prod)

    print('\nGénération de ligne(s) de facture :')
    for i  in range (1, random.randint(2,11)):
        l = InvoiceLineFactory()
        print(f'Ligne facture : {l}')

    print('\nGénération de  facture(s):')
    for i  in range (1, random.randint(2,5)):
        f = generateInvoice()
        print(f'Facture : {f}')
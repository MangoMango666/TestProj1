"""
    Equivalent de fetch_user_from_api mais avec PyTest
    Voir le fichier pytest.ini
"""

import unittest

import pytest
import responses

from fetch_user_from_api import *

FAKE_USER = {
    'results': [
        {
            'gender': 'male',
            'name': {
                'title': 'mr',
                'first': 'balder',
                'last': 'fjelldal'
            },
            'location': {
                'street': 'frogner terrasse 9834',
                'city': 'skogn',
                'state': 'trøndelag',
                'postcode': '4745',
                'coordinates': {
                    'latitude': '57.4497',
                    'longitude': '-104.3736'
                },
                'timezone': {
                    'offset': '-3:00',
                    'description': 'Brazil, Buenos Aires, Georgetown'
                }
            },
            'email': 'balder.fjelldal@example.com',
            'login': {
                'uuid': '13533bde-e5d2-4d83-a428-0f27b1a8d4e5',
                'username': 'blackleopard103',
                'password': 'corvette',
                'salt': '6vZkZHmO',
                'md5': 'f315c82abf50c6d4ccfa4212427e88e6',
                'sha1': '14f7654bcac4dd274a24bd65ea792c365d8397f0',
                'sha256':
                    'f29b56e8388d0e7cf5bf9edec788eb2b53abb0667f63ffd727654850d'
                    '1f18fdc'
            },
            'dob': {'date': '1995-03-18T21:30:22Z', 'age': 23},
            'registered': {'date': '2004-04-05T08:33:03Z', 'age': 14},
            'phone': '71658283',
            'cell': '99243409',
            'id': {'name': 'FN', 'value': '18039532839'},
            'picture': {
                'large': 'https://randomuser.me/api/portraits/men/48.jpg',
                'medium': 'https://randomuser.me/api/portraits/med/men/48.jpg',
                'thumbnail':
                    'https://randomuser.me/api/portraits/thumb/men/48.jpg'
            },
            'nat': 'NO'
        }
    ],
    'info': {
        'seed': '36bc86c63f61cd5a',
        'results': 1,
        'page': 1,
        'version': '1.2'
    }
}


class TestThisShit:

    ''' Ce premier jeu de tests effectue de réelles requêtes http  '''

    def testOk(self):
        us = createUserFromAPIUrl('https://randomuser.me/api')
        assert isinstance(us, User)
        print('testOk completed')

    def testWrongPage(self):
        with pytest.raises(Exception404):
            createUserFromAPIUrl('https://randomuser.me/apiXXXXXX')
        print('testWrongPage completed')

    def testWrongServer(self):
        with pytest.raises(CannotConnectToAPIException):
            us = createUserFromAPIUrl('https://jklhmhjjklmhjklhjklh/apiXXXXXX')
        print('testWrongServer completed')

    @unittest.skip(' ce test est ignoré grâce au décorateur') # y-compris par pytest !
    def testIgnoré(self): # exemple de test ignoré (temporairement) grâce au décorateur
        raise Exception()

    @pytest.mark.skip(' ce test est ignoré grâce au décorateur') # autre décorateur spécifique Pytest
    def testIgnoré2(self): # exemple de test ignoré (temporairement) grâce au décorateur
        raise Exception()


class TestThisOtherShit:
    ''' Ce jeu de tests utilise des requêtes http simulées '''

    @responses.activate # spécifique au package responses
    def testOkWithMock(self): # test avec un user qui n'est obtenu avec une fausse requête http (simulée)
        responses.add(responses.GET, 'https://randomuser.me/api', json=FAKE_USER)
        us = createUserFromAPIUrl('https://randomuser.me/api')
        assert isinstance(us, User)
        assert us.name =='mr balder fjelldal'
        print('testOkWithMock completed')

    @responses.activate # spécifique au package responses
    def testWrongPageWithMock(self):
        # le serveur va renvoyer une erreur 404
        responses.add(responses.GET, 'https://randomuser.me/api', status=404)
        with pytest.raises(Exception404):
            createUserFromAPIUrl('https://randomuser.me/api')
        print('testWrongPageWithMock completed')

    @responses.activate # spécifique au package responses
    def testWrongServerWithMock(self): # même principe
        # le serveur est ok mais on va demander une URL incorrecte
        responses.add(responses.GET, 'https://randomuser.me/api', status=404)
        with pytest.raises(CannotConnectToAPIException):
            createUserFromAPIUrl('https://randomuserXXXX.me/api')
        print('testWrongServerWithMock completed')

    @responses.activate # spécifique au package responses
    def testServerDownWithMock(self): # même principe
        # pas de responses.add pour simuler que le serveur est HS
        with pytest.raises(CannotConnectToAPIException):
            createUserFromAPIUrl('https://randomuser.me/api')
        print('testWrongServerWithMock completed')


class TestMocker:
    ''' classe de test utilisant le mocker propre à PyTest '''
    def test_my_mock(self, mocker): # nom mocker obligatoire ?

        # affectation de la méthode qui simule
        mocker.patch('fetch_user_from_api.createUserFromAPIUrl', return_value=User.createFromJson(FAKE_USER))
        from fetch_user_from_api import createUserFromAPIUrl # réécarsement du pointeur vers la méthode simulée
        user = createUserFromAPIUrl('https://randomuser.me/api')  # appel de test
        # comparaison avec ce qu'on sait qu'on est censé recevoir
        fake_user = User.createFromJson(FAKE_USER)
        assert user == fake_user
        print('test_my_mock completed')


class TestFixtures:
    ''' Le but des fixtures est de générer des données pour lancer en série un test '''

    USERS = [FAKE_USER, FAKE_USER, FAKE_USER]  # 3 fois le même user, mais serait mieux avec des users différents

    @pytest.fixture() # PyTest repère le décorateur et sait que
    def generate_user_and_title(self):
        # TODO : coder un générateur qui renvoie les objets nécessaires pour les tests
        user = User.createFromJson()
        pass

    # méthode de test qui utilise les fixtures
    def test_(self,generate_user_and_title): # on passe la méthode avec le décorateur comme paramètre
        # TODO : coder le test qui va être appelé pour chaque itération du générateur renvoyé par generate_user_and_title
        pass


if __name__== '__main__':
    pytest.main()

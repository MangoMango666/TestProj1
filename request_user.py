import unittest
from dataclasses import dataclass

import prettyprinter as pp
import requests


@dataclass
class User:
    name: str
    username: str
    email: str


class CannotConnectToAPIException(Exception):
    pass


class Exception404(Exception):
    def __init__(self, http_response: requests.Response):
        super().__init__()
        self.response = http_response

    # def __repr__(self):
    #     print(self.response)
    #     super.__repr__(self)


def createUserFromAPIUrl(url: str) -> User:
    try:
        response = requests.get(url)
        if response.status_code == 404:
            raise Exception404(response)
        assert response.status_code == 200, print(f'Code réponse http: {response.status_code}')
        result = response.json()
        # pp.cpprint(result)

        user_record = result['results'][0]
        # print (user_record)

        name_object = user_record['name']
        return User(name=f"{name_object['title']} {name_object['first']} {name_object['last']} ",username=user_record['login']['username'],email=user_record['email'])

    except requests.exceptions.ConnectionError as err:
        raise CannotConnectToAPIException(...).with_traceback(err.__traceback__)


class TestThisShit(unittest.TestCase):

    def testOk(self):
        us = createUserFromAPIUrl('https://randomuser.me/api')
        assert isinstance(us, User)
        print('testOk completed')

    def testWrongPage(self):
        with self.assertRaises(Exception404):
            createUserFromAPIUrl('https://randomuser.me/apiXXXXXX')
        print('testWrongPage completed')

    def testWrongServer(self):
        with self.assertRaises(CannotConnectToAPIException):
            us = createUserFromAPIUrl('https://jklhmhjjklmhjklhjklh/apiXXXXXX')
        print('testWrongServer completed')


if __name__== '__main__':
    # try:
    #     toto = createUserFromAPIUrl('https://randomuser.me/api')
    #     pp.cpprint(f'User récupéré par API : {toto}')
    # except CannotConnectToAPIException as err :
    #     print(f'Serveur injoignable : \n{err}')
    # except Exception404 as err :
    #     print('Erreur 404 : \n'+repr(err))
    unittest.main()

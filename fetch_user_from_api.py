from dataclasses import dataclass

import requests


@dataclass
class User:
    name: str
    username: str
    email: str

    @classmethod
    def createFromJson(cls, json: str):
        result = json
        # pp.cpprint(result)

        user_record = result['results'][0]
        # print (user_record)

        name_object = user_record['name']
        return cls(name=f"{name_object['title']} {name_object['first']} {name_object['last']}",
                    username=user_record['login']['username'], email=user_record['email'])


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
        return User.createFromJson(response.json())

    except requests.exceptions.ConnectionError as err:
        raise CannotConnectToAPIException(...).with_traceback(err.__traceback__)


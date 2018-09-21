import functools

import requests

URL = 'https://randomuser.me/api'

# ---------------------- Exemple 1 : pas de paramètres et pas de méta-données -----------


def debug_function(function, *args, **kwargs):
    # création d'une fonction wrapper de celle fournie
    def function_wrapper(*args, **kwargs):
        print(f'Debug: Appel de la fonction {function} avec arguments={args} et kwargs={kwargs}')
        result = function(*args, **kwargs)
        return result
    return function_wrapper


def get_user0(url):
    response = requests.get(url)
    return response.json()


print('Appel de get_user0 (sans debug) {0}\n'.format(get_user0(URL)))
# appel de type 1 : sans décorateur
get_user1 = debug_function(get_user0) # réaffectation du pointeur de la fonction vers son wrapper
print('Appel de get_user1 (avec debug) {0}\n'.format(get_user1(URL)))


# appel de type 2 : avec décorateur
@debug_function
def get_user2(url):
    response = requests.get(url)
    return response.json()


print('Appel de get_user2 (avec debug) {0}\n'.format(get_user2(URL)))

# ---------------------- Exemple 1 : avec paramètres et méta-données -----------


import time


def time_function(active: bool):
    def decorator(function):
        @functools.wraps(function) # sert à transmettre automatiquement les méta-données
        def function_wrapper(*args, **kwargs):
            if active:
                start_time = time.process_time()
                result = function(*args, **kwargs)
                end_time = time.process_time()
                print(f'Timer: exécution de la fonction {function} en {end_time - start_time} secondes  avec arguments={args} et kwargs={kwargs}')
                return result
            else:
                return function(*args, **kwargs)
        return function_wrapper
    return decorator


@time_function(active=False)
def get_user3(url):
    response = requests.get(url)
    return response.json()


print('Appel de get_user3 (sans timing) {0}\n'.format(get_user3(URL)))


@time_function(active=True)
def get_user4(url):
    response = requests.get(url)
    return response.json()


print('Appel de get_user4 (avec timing) {0}\n'.format(get_user4(URL)))

decorated_function = time_function(True)
wrapped_function = decorated_function(get_user0)
print('Appel de get_user0 avec timing {0}\n'.format(wrapped_function(URL)))

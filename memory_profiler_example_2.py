"""
    Exemples de memory profiling
    Lancement normal mais il faut d'abord fixer la variable d'environnement
    (sous Linux / l'environnement virtuel : export MEMORY_PROFILING=True )

    Pour visualisation sous forme graphique, besoin installer la librairie matplotlib et le package .deb pyhthon3-tk
    puis lancer les commandes suivantes dans le venv :
        mprof run memory_profiler_example_2.py
        mprof plot
"""
import os
from memory_profiler import profile

ACTIVATE_MEMORY_PROFILING = os.getenv('MEMORY_PROFILING') == 'True'


def activate_profiling(function_name):
    ''' fonction qui active le profiling d'une fonction suivant une variable d'environnement '''
    if ACTIVATE_MEMORY_PROFILING:
        return profile(function_name)
    else:
        return function_name


@activate_profiling
def my_func():
    a = [1] * (10**6) # création d'un tableau avec 1 million de 1
    b = [1] * (2 * 10**7 ) # création d'un tableau avec 2 milliards de 1
    del b # suppression pour libération mémoire
    return a


if __name__ == '__main__':
    for i in range (1,5):
        activate_profiling(my_func())
        print (f'{i} appel(s)')
    print(f'Fini !')


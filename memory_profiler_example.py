"""
    Exemples de memory profiling
    Lancement avec python -m memory_profiler <nom du fichier .py>
    Il n'y pas besoin d'import pour @profile si le module est lancé avec la ligne de commande ci-dessus ;
    le décorateur va être traité à la voléee au moment de l'appel
    Sinon, il faut utiliser : from memory_profiler import profile
"""


@profile # pas besoin d'import, va être traité
def my_func():
    a = [1] * (10**6) # création d'un tableau avec 1 million de 1
    b = [1] * (2 * 10**7 ) # création d'un tableau avec 2 milliards de 1
    del b # suppression pour libération mémoire
    return a


if __name__ == '__main__':
    my_func()


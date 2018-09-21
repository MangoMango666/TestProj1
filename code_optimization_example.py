"""
    4 exemples de fonctions faisant la même chose mais avec des performances croissantes
    f4 prend 40 fois moins de temps que f1
"""

@profile
def f1():
    lst = []
    for i in range (1_000_000)
        lst.append(i)
    return lst

@profile
def f2():
    # utilisation d'un pointeur vers la méthode de append pour éviter la récupération de la méthode
    lst = []
    append = lst.append
    for i in range(1_000_000)
        append(i)
    return lst

@profile
def f3():
    return [i for i in range(1_000_000)]


@profile
def f1():
    return list(range(1_000_000))

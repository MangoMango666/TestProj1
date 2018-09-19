#! /bin/bash
# connection à l'environnement virtuel
cd ../venv/bin
source activate
# lancement de pytest
cd ../../TestProj1/
pytest -l # sans paramètres = recherche automatique des tests en se basant sur les noms de fichiers ; switch -l pour qu'il montre la valeur des variables locales
# quitter l'environnement virtuel
deactivate

# version alternative : ../venv/bin/pytest -l

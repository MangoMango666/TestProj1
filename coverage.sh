#! /bin/bash
# appel de coverage pour savoir quelle fraction du code est utilisé (couvert par les tests)
coverage run --source=. facture_unittests.py
coverage html
firefox htmlcov/index.html 


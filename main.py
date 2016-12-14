#! /usr/bin/env python3

"""
    Fichier principal du projet decoupage.py
"""

import argparse
from parser_stl import ParseurStl

PARSER_GENERAL = argparse.ArgumentParser()
PARSER_GENERAL.add_argument('--chemin', type=str)
ARGUMENTS = PARSER_GENERAL.parse_args()

def test_parser_stl():
    """
        Lecture rapide du contenu binaire du fichier stl
    """
    # Initialisation du parseur
    parseur = ParseurStl(ARGUMENTS.chemin)
    # Affichage des ses differentes caracteristiques
    print("Nb triangle : ", parseur.nombre_triangle)
    print("Triangle 1: ", str(parseur.triangles[0]))

def main():
    """
        Fonction principale qui lance les modules
    """
    # print("Hello World !")
    test_parser_stl()

if __name__ == '__main__':
    main()

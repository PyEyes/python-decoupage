#! /usr/bin/env python3

"""
    Fichier principal du projet decoupage.py
"""

import argparse
from parser_stl import ParseurStl


PARSER_GENERAL = argparse.ArgumentParser()
PARSER_GENERAL.add_argument('--chemin', type=str)
ARGUMENTS = PARSER_GENERAL.parse_args()

def test_lecture_rapide_stl():
    """
        Lecture rapide du contenu binaire du fichier stl
    """
    chemin_fichier_stl = ARGUMENTS.chemin
    parseur = ParseurStl(chemin_fichier_stl)
    print(parseur.contenu)
    print("Nb triangle : ", parseur.nombre_triangle)

def main():
    """
        Fonction principale qui lance les modules
    """
    # print("Hello World !")
    test_lecture_rapide_stl()

if __name__ == '__main__':
    main()

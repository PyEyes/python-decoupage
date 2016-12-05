#! /usr/bin/env python3

"""
    Fichier principal du projet decoupage.py
"""

from parser_stl import  ParseurStl

def main():
    """
        Fonction principale qui lance les modules
    """
    chemin_fichier_stl = ""
    parseur = ParseurStl(chemin_fichier_stl)
    parseur.lire_stl()

if __name__ == '__main__':
    main()

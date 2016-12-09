#! /usr/bin/env python3

"""
    Module de parsing pour les fichiers stl
"""

from struct import unpack

class ParseurStl:
    """
        Ouvre le fichier stl et le convertit en objets
    """
    def __init__(self, p_chemin_fichier_stl):
        self.chemin_fichier_stl = p_chemin_fichier_stl
        with open(self.chemin_fichier_stl, "rb") as stl:
            self.contenu = unpack("<IIII", stl.read())

    def lire_stl(self):
        """
            Lit un fichier stl et stocke ce qu'il lit dans des objets a part
        """
        pass

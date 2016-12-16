#! /usr/bin/env python3

"""
    Module de parsing pour les fichiers stl binaires
"""

import struct
import geometrie

class ParseurStl:
    """
        Ouvre le fichier stl et le convertit en objets
    """
    def __init__(self, p_chemin_fichier_stl):
        self.chemin_fichier_stl = p_chemin_fichier_stl
        self.triangles = []
        with open(self.chemin_fichier_stl, "rb") as stl:
            # Stockage du contenu entier du fichier en binaire
            self.entete = stl.read(80)
            self.nombre_triangle = struct.unpack("<i", stl.read(4))[0]
            self.triangles = []
            for _ in range(self.nombre_triangle):
                coordonnees = []
                for _ in range(4):
                    vecteur = []
                    # Parcours une coordonnee a chaque fois
                    for _ in range(3):
                        vecteur.append(struct.unpack("<f", stl.read(4))[0])
                    coordonnees.append(vecteur)
                self.triangles.append(geometrie.Triangle(coordonnees))
                # 2 bytes de vide
                stl.read(2)

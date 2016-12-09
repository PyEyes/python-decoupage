#! /usr/bin/env python3

"""
    Module de parsing pour les fichiers stl
"""

# import binascii
# from struct import unpack
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
            self.contenu = [bin(i)[2:]for i in stl.read()]
            self.entete = self.contenu[:80] # 0 -> 79 = 80 bytes
            nombre_triangle_binaire = ''.join(self.contenu[80:84]) # 80 -> 83 = 4 bytes
            self.nombre_triangle = int(nombre_triangle_binaire, 2)
            self.corps = self.contenu[84:]

    def convertir_en_triangles(self):
        """
            Parse le corps pour transformer le contenu en triangle
        """
        # Todo: parcourir le corps, puis parser pour obtenir des triangles
        #           que l'on stockera ensuite dans triangle
        # Un triangle => sur 50 octets
        corps = self.corps
        triangle_binaire = corps[0:49]
        # Possibilite: Optimiser len(corps)
        while len(corps) >= 2:
            corps = corps[0:49]
            # TODO : Transformer un byte en float

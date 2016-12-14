#! /usr/bin/env python3

"""
    Structure des constructions geometriques de bases:
        - Les Triangles, qui contiennent un vecteur normal en 3D et des points en 3D
"""

class Triangle:
    """
        Un triangle est compose de un vecteur normal
        et de 3 points, le tout en 3 dimensions
            => Arguments a passer de la forme : tuple = (x, y, z)
    """
    def __init__(self, p_liste_coordonnees):
        # Utilisation des tuples au lieu des classes => optimisation
        self.vecteur_normal = p_liste_coordonnees[0]
        self.points = p_liste_coordonnees[1:]
    def __str__(self):
        chaine = "n("+ ", ".join([str(round(e, 2)) for e in self.vecteur_normal])+"), "
        for indice, vecteur in enumerate(self.points):
            print("vecteur : ", vecteur)
            chaine += "vect_{}(".format(indice+1)
            chaine += ", ".join([str(round(e, 2)) for e in vecteur])
            chaine += "), "
        # Enleve les deux derniers caracteres
        return chaine[:-2]

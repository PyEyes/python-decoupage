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
    def __init__(self, p_tuple_vecteur_normal, p_liste_trois_points_en_tuple):
        # Utilisation des tuples au lieu des classes => optimisation
        self.vecteur_normal = p_tuple_vecteur_normal
        self.points = p_liste_trois_points_en_tuple

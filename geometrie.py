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
        pts_a = self.points[0]
        equation_constante = self.vecteur_normal[0]*pts_a[0] + \
                                self.vecteur_normal[1]*pts_a[1] + \
                                    self.vecteur_normal[2]*pts_a[2]
        self.equation = [self.vecteur_normal[0], self.vecteur_normal[1], equation_constante]

    def __str__(self):
        chaine = "n("+ ", ".join([str(round(e, 2)) for e in self.vecteur_normal])+"), "
        for indice, vecteur in enumerate(self.points):
            print("vecteur : ", vecteur)
            chaine += "vect_{}(".format(indice+1)
            chaine += ", ".join([str(round(e, 2)) for e in vecteur])
            chaine += "), "
        # Enleve les deux derniers caracteres
        return chaine[:-2]

def colineaires(vecteur_un, vecteur_deux):
    """
        Renvoit true si les deux vecteurs sont colineaires
    """
    diviseurs = []
    for coord_un, coord_deux in zip(vecteur_un, vecteur_deux):
        if coord_deux != 0:
            diviseurs.append(coord_un/float(coord_deux))
        else:
            diviseurs.append(None)
    print("Diviseurs : ", diviseurs)
    return (diviseurs[0] == diviseurs[1] and diviseurs[0] == diviseurs[2])
    
class Intersector:
    """
        Gere les intersection entre un plan et une liste de triangle
    """
    def __init__(self, p_triangles, p_coordonnes_plan):
        self.triangles = p_triangles
        self.plan = p_coordonnes_plan

    def intersection_triangle_plan(self, triangle, plan):
        """
            Regarde si un triangle presente une intersection avec le plan ou non
        """
        # test des 3 cas
        # Cas de base
        #
        #
        # secants = True
        # # Tester si colineaire
        # if secants:
        #     print("C'est secant")
        # else:
        #     print("Ce n'est pas secant")

        pass



























# heyds

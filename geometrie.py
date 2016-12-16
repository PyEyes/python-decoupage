#! /usr/bin/env python3

"""
    Structure des constructions geometriques de bases:
        - Les Triangles, qui contiennent un vecteur normal en 3D et des points en 3D
"""

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
    return diviseurs[0] == diviseurs[1] and diviseurs[0] == diviseurs[2]

def equation_droite_3d(point_un, point_deux):
    """
        Renvoit l'equation parametrique d'une droite en 3D
        sous la forme : (u0, u1, u2), (p0, p1, p2)
        avec u le vecteur directeur et p le vecteur des constantes
    """
    vecteur_directeur = []
    for coord_un, coord_deux in zip(point_un, point_deux):
        vecteur_directeur.append(coord_deux - coord_un)
    return vecteur_directeur, point_un

def coordonnees_point_sur_droite(equation, constante_plan_z):
    """
        Renvoit les coordonnees d'un point sur un segment,
        si ce segment est coupe par la constante plan_z.
        Attention a verifier au prealable si le plan coupe la droite
    """
    # Decoupage de l'equation parametrique pour plus de lisibilite
    vecteur_normal = equation[0]
    vecteur_constantes = equation[1]
    # Calcul des coordonnees
    constante_k = (constante_plan_z - vecteur_constantes[2]) / vecteur_normal[2]
    abcisse = constante_k*vecteur_normal[0] + vecteur_constantes[0]
    ordonnee = constante_k*vecteur_normal[1] + vecteur_constantes[1]
    return abcisse, ordonnee, constante_plan_z

class Triangle:
    """
        Un triangle est compose de un vecteur normal
        et de 3 points, le tout en 3 dimensions
            => Arguments a passer de la forme : tuple = (x, y, z)
        Utilisation des tuples au lieu des classes => optimisation
    """
    def __init__(self, p_liste_coordonnees):
        # Recuperation des arguments
        self.vecteur_normal = p_liste_coordonnees[0]
        self.points = p_liste_coordonnees[1:]
        # Couples de points de chaque segment
        # couple = [[xa, ya, za], [xb, yb, zb], [m, p]]
        self.couples = [[self.points[0], self.points[1]],
                        [self.points[1], self.points[2]],
                        [self.points[0], self.points[2]]]
        # Rajout dans couple de l'equation de droite de chaque segment
        for couple in self.couples:
            # Equation parametrique en 3d
            couple.append(equation_droite_3d(couple[0], couple[1]))
        # Equation de plan
        pts_a = self.points[0]
        equation_plan_constante = self.vecteur_normal[0]*pts_a[0] + \
                                self.vecteur_normal[1]*pts_a[1] + \
                                    self.vecteur_normal[2]*pts_a[2]
        self.equation_plan = [self.vecteur_normal[0], self.vecteur_normal[1],\
                                    equation_plan_constante]

    def est_coupe_par_plan(self, constante_plan_z):
        """
            Renvoit les couples coupes par le plan vertical
            d'equation z = constante_plan_z
        """
        # couple = [(xa, ya, za), (xb, yb, zb), (m, p)]
        segments_coupes = []
        for couple in self.couples:
            entre_un_deux = (couple[0][2] <= constante_plan_z and constante_plan_z <= couple[1][2])
            entre_deux_un = (couple[0][2] >= constante_plan_z and constante_plan_z >= couple[1][2])
            if entre_un_deux or entre_deux_un:
                segments_coupes.append(couple)
        return segments_coupes

    def __str__(self):
        chaine = "n("+ ", ".join([str(round(e, 2)) for e in self.vecteur_normal])+"), "
        for indice, vecteur in enumerate(self.points):
            chaine += "vect_{}(".format(indice+1)
            chaine += ", ".join([str(round(e, 2)) for e in vecteur])
            chaine += "), "
        # Enleve les deux derniers caracteres
        return chaine[:-2]

def hauteur_min_max(triangles):
    """
        Retourne la hauteur minimal et maximal
        des triangles
    """
    # Cas de base
    hauteur_min = float("+inf")
    hauteur_max = float("-inf")

    for triangle in triangles:
        for point in triangle.points:
            hauteur = point[2]
            if hauteur > hauteur_max:
                hauteur_max = hauteur
            if hauteur < hauteur_min:
                hauteur_min = hauteur
    return hauteur_min, hauteur_max

def chercher_segments(triangles, constante_plan_z):
    """
        Stocke dans une liste les points qui
        delimitent les segments de crées par le plan
    """
    # Reset des segments
    segments = []
    # Parcours de tous les triangle
    # Transformation du couple des segments coupés en deux points
    for triangle in triangles:
        # Cherche tous les segments qui sont coupes par le plan
        segments_coupes = triangle.est_coupe_par_plan(constante_plan_z)
        # Check si le triangle a bien ete coupé par le plan
        if segments_coupes != []:
            # Segment = [couple_un, couple_deux]
            points = []
            # Segments coupes: les deux segments decrit par un couple chacun
            for couple in segments_coupes:
                # couple = [point_un, point_deux, equation]
                point = coordonnees_point_sur_droite(couple[2], constante_plan_z)
                # point[:2] => abscisse et ordonnee
                points.append(point[:2])
            segments.append(points)
    return segments


    # EOF

#! /usr/bin/env python3

"""
    Test de tous les modules
"""

import geometrie
import parser_stl

CHEMIN_FICHIER_STL_FACILE = "Tux_printable.stl"
CHEMIN_FICHIER_STL_COMPLIQUE = "Pumpkin_whole.stl"
NOMBRE_TRANCHES = 10
CONSTANTE_PLAN_Z = 2

def test_coord_point_droite(equation, constante_plan_z):
    """
        Test si nous trouve bien un point pour z = constante_plan_z
    """
    coordonnees = geometrie.coordonnees_point_sur_droite(equation, constante_plan_z)
    print("Test si trouve le point sur le droite: ")
    print("Equation : ", equation)
    print("Z: ", constante_plan_z)
    constante_k = []
    for i in range(3):
        constante_k.append((coordonnees[i] - equation[1][i])/equation[0][i])
    print("Liste des k : ", constante_k)
    listes_k = []
    k_identique = True
    for k in constante_k:
        if round(k, 1) in listes_k:
            k_identique = False
            break
        else:
            listes_k.append(k)
    if k_identique:
        print("Les k ne sont pas identiques")
    else:
        print("L'equation est valide")
    return coordonnees

def test_parser_stl():
    """
        Lecture rapide du contenu binaire du fichier stl
    """
    # Initialisation du parseur
    parseur = parser_stl.ParseurStl(CHEMIN_FICHIER_STL_FACILE)
    # Affichage des ses differentes caracteristiques
    print("Nb triangle : ", parseur.nombre_triangle)
    print("Triangle 1: ", str(parseur.triangles[0]))

def test_colineaires():
    """
        test colineaires
    """
    print(geometrie.colineaires([0, 1, 5], [5, 7, 8]))
    print(geometrie.colineaires([1, 1, 1], [2, 2, 2]))

def test_equation_droite_3d(point_un, point_deux):
    """
        Test de l'equation de droite de deux segments
        Fonctionne : OK
    """
    print("Test equation droite : ")
    print("Point un : ", point_un)
    print("Point deux : ", point_deux)
    equation = geometrie.equation_droite_3d(point_un, point_deux)
    print("Equation : ", equation)
    return equation


def main():
    """
        Fonction de test principal
    """
    print("Test colineaires: ")
    test_colineaires()
    print("Test parser: ")
    test_parser_stl()
    vecteur_normal = [1, 1, 1]
    point_zero = [0, 0, 0]
    point_un = [5, 3, 10]
    point_deux = [10, 2, 0]
    equation = test_equation_droite_3d(point_un, point_deux)
    coordonnees_points = test_coord_point_droite(equation, CONSTANTE_PLAN_Z)
    print("Coordonnees du point: ", coordonnees_points)
    coordonnees = [vecteur_normal] + [point_zero] + [point_un] + [point_deux]
    print(coordonnees)
    triangle_un = geometrie.Triangle(coordonnees)
    segments_coupes = triangle_un.est_coupe_par_plan(CONSTANTE_PLAN_Z)
    print("Segments coupés: ", segments_coupes)
    print("0 : ", segments_coupes[0])
    print("1 : ", segments_coupes[1])

if __name__ == '__main__':
    main()

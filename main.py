#! /usr/bin/env python3

"""
    Fichier principal du projet decoupage.py
"""

import argparse
from geometrie import Intersector, Triangle
from parser_stl import ParseurStl

PARSER_GENERAL = argparse.ArgumentParser()
PARSER_GENERAL.add_argument('--chemin', type=str)
ARGUMENTS = PARSER_GENERAL.parse_args()

def test_intersection():
    """
        Test les intersections entre un triangle et un plan
    """
    triangles_listes = []
    vect_normal = [1, 1, 1]
    # Points
    # Triangle un coordonnees
    pts_un = [0, 1, 2]
    pts_deux = [0, 3, 4]
    pts_trois = [0, 2, 15]
    tri_coord_un = []
    tri_coord_un.append(vect_normal)
    tri_coord_un.append(pts_un)
    tri_coord_un.append(pts_deux)
    tri_coord_un.append(pts_trois)

    tri_un = Triangle(tri_coord_un)
    triangles_listes.append(tri_un)
    # Calcule equation plan
    print("Points A: ", tri_un.points[0])
    print("Vecteur normal: ", tri_un.vecteur_normal)
    print("Equation plan: ", tri_un.equation)
    # Intersection
    equation_plan = [0, 0, 1]
    intersecteur = Intersector(triangles_listes, equation_plan)
    # resultat_intersection = intersecteur.intersection_triangle_plan(tri_un, equation_plan)
    # print(resultat_intersection)

def test_parser_stl():
    """
        Lecture rapide du contenu binaire du fichier stl
    """
    # Initialisation du parseur
    parseur = ParseurStl(ARGUMENTS.chemin)
    # Affichage des ses differentes caracteristiques
    print("Nb triangle : ", parseur.nombre_triangle)
    print("Triangle 1: ", str(parseur.triangles[0]))

def main():
    """
        Fonction principale qui lance les modules
    """
    # print("Hello World !")
    # test_parser_stl()
    test_intersection()

if __name__ == '__main__':
    main()

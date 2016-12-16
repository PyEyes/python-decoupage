#! /usr/bin/env python3

"""
    Test du svg
    (Doit se trouver dans un fichier test different pour
    eviter tous les prints inutiles)
"""

import svg

CHEMIN_FICHIER_STL_FACILE = "Tux_printable.stl"
CHEMIN_FICHIER_STL_COMPLIQUE = "Pumpkin_whole.stl"

def test_svg(segments):
    """
        Test les svgs
    """
    svg.creer_tranche(600, 400, "triangle.svg", segments, 10, [0, 255, 0])

def main():
    """
        Fonction de test principal du svg
    """
    point_zero = [0, 0, 0]
    point_un = [5, 3, 10]
    point_deux = [10, 2, 0]
    # Affichage triangle
    test_svg([[point_zero, point_un], [point_un, point_deux],\
                    [point_zero, point_deux]])


if __name__ == '__main__':
    main()
    _ = input("")

#! /usr/bin/env python3

"""
    Fichier principal du projet decoupage.py
"""

import argparse
import geometrie
import svg
import parser_stl

# TRAITEMENT DES ARGUMENTS
PARSER_GENERAL = argparse.ArgumentParser(description="slice an STL file : Problem of scaling,\
                                        zoom out to see the figure", \
                    epilog="slice given stlfile into SLICES horizontal slices.\
                        Writes a numbered output svg file for each slice (horizontal way)")
PARSER_GENERAL.add_argument('stl_file', type=str, help="name of stl file to slice (default is 4)")
PARSER_GENERAL.add_argument('-s', '--slices', type=int, help="how many slices you want")
ARGUMENTS = PARSER_GENERAL.parse_args()
# CONSTANTES
if  ARGUMENTS.stl_file != None:
    CHEMIN_FICHIER_STL = ARGUMENTS.stl_file
else:
    CHEMIN_FICHIER_STL = "Tux_printable.stl"

if ARGUMENTS.slices != None:
    NOMBRE_TRANCHES = ARGUMENTS.slices
else:
    NOMBRE_TRANCHES = 4

def calculer_bon_format(x_min, x_max, y_min, y_max):
    """
        Calcule le bon format de l'image
        Renvoit les bonnes dimensions et le bon coefficient d'echelle
        => Probleme de cadrage dans la feuille, figure eloignee
        du centre de la feuille (dezoom)
    """
    delta_x = x_max - x_min
    delta_y = y_max - y_min
    # Image optimale : aux alentours de 800px
    coefficient = 800/(max([delta_x, delta_y]))
    return 1200, 1200, coefficient

def main():
    """
        Fonction principale qui lance les modules
    """
    parseur = parser_stl.ParseurStl(CHEMIN_FICHIER_STL)
    # Calcule de la hauteur
    x_min, x_max, y_min, y_max, hauteur_min, hauteur_max =\
                            geometrie.x_y_hauteur_min_max(parseur.triangles)
    hauteur_generale = hauteur_max - hauteur_min
    pas = hauteur_generale / float(NOMBRE_TRANCHES)
    # For _ in range ne fonctionne que sur des entiers
    # Doit calculer une nouvelle liste pour calculer la constante
    constantes_z = []
    hauteur_actuelle = hauteur_min
    while hauteur_actuelle < hauteur_max:
        nouvelle_hauteur = hauteur_actuelle + pas
        constantes_z.append(nouvelle_hauteur)
        hauteur_actuelle = nouvelle_hauteur
    # Calculer le bon format
    largeur, hauteur, coefficient = calculer_bon_format(x_min, x_max, y_min, y_max)
    # Tranches par tranches
    for indice, constante_z in enumerate(constantes_z):
        segments_coupes = geometrie.chercher_segments(parseur.triangles, constante_z)
        nom_fichier = "tranche_"+str(indice)+".svg"
        svg.creer_tranche(hauteur, largeur, nom_fichier, segments_coupes, coefficient, [0, 255, 0])

if __name__ == '__main__':
    main()

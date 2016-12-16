#! /usr/bin/env python3

"""
    Permet de créer les fichiers svg
"""

def entete(largeur, hauteur):
    """
    Affiche l'entete d'un fichier svg
    """
    return "<svg width='{}' height='{}' >".format(largeur, hauteur)

def affiche_polygon(segments, coefficient, couleur):
    """
    Affiche un polygon
    Segments : [[x1, y1], [x2, y2]]
    Le coefficient permet de modifier l'echelle
    """
    chaine_coordonnes = ""
    for segment in segments:
        for point in segment:
            chaine_coordonnes += str(round(point[0]*coefficient, 2))+","\
                +str(round(point[1]*coefficient, 2))+","


    couleur_str = str(couleur[0])+","+str(couleur[1])+","+str(couleur[1])
    #print("Chaine coordonnees : ", chaine_coordonnes)
    return "<polygon points='{}' style='fill:rgb({});stroke:rgb({});stroke-width:1' />"\
                .format(chaine_coordonnes[:-1], couleur_str, couleur_str)

def creer_tranche(hauteur, largeur, nom_fichier, segments_coupes, coefficient, couleur):
    """
        Creation de la tranche
    """
    header = entete(hauteur, largeur)
    body = affiche_polygon(segments_coupes, coefficient, couleur)
    end = fin()
    with open(nom_fichier, "w") as tranche:
        tranche.write(header+body+end)


def fin():
    """
    Ecrit la fin du fichier svg
    """
    return "</svg>"

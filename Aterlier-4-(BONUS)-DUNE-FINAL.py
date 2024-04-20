# -*- coding: utf-8 -*-

####################################################################
# Avant de commencer a lire le code, voici quelque informations    #
# important pour lire et comprendre le code :                      #
#                                                                  #
# - "import os" permet d'utiliser la commande                      #
#   os.system("cls;clear") elle est uniquement dédié à             #
#   clear la console (c'est à dire la vider totalement             #
#   comme une nouvelle page).                                      #
#   Cela permet d'avoir un résultat plus propre lors de            #
#   l'exécution.                                                   #
#   (Elle n'est pas était interdite d'utilisation, j'ai vérifié    #
#   au près du professeur présentant le cours amphi de l'UE).      #
#                                                                  #
# - La fonction "afficher_erreur" permet d'afficher un message     #
#   d'erreur (j'ai crée cette fonction dans le but d'avoir un code #
#   plus clair).                                                   #
#   Elle n'était pas demandé cependant j'ai trouvé intéréssant     #
#   d'en faire une (pour être plus compréhensible).                #
#                                                                  #
# - ".isdigit" et ".isalpha" sont des outils de python             #
#   permettant de savoir si un caractère est un chiffre,           #
#   ou une lettre. (Elle n'ont pas était interdite d'utilisation,  #
#   j'ai vérifié au près du professeur présentant le cours amphi   #
#   de l'UE).                                                      #
#                                                                  #
# - La fonction "choix_grille" permet de lancer une partie         #
#   en définisant via choix, les paramètres de celle-ci.           #
#   Elle n'était pas demandé cependant j'ai trouvé intéréssant     #
#   d'en faire une (pour être plus compréhensible et pratique      #
#   lors de mes futur test).                                       #
#   Vous pouvez donc tester les affichage avec les différentes     #
#   configurations. (Rien n'interdit de faire cela)                #
#                                                                  #
# - L'ensemble des fonctions font moins de 15 lignes comme         #
#   stipulé (Si on retire tout les commentaire, retour à la        #
#   ligne et print que j'ai mit pour la lisibilité),               #
#   (Hors "afficher_grille", celle-ci avait le droit d'être        #
#   plus longue).                                                  #
#                                                                  #
# - L'ia n'est pas vraiment intéligente, c'est à dire :            #
#       - Elle choisit un pion Aléatoirement.                      #
#       - Elle applique le meilleur mouvement que le pion peut     #
#       faire                                                      #
#   Certains match avec elles peuvent être très très long, comme   #
#   très très cours, tout repose sur l'aléatoire, comme demandée   #
#   Note : Je n'ai pas réussi a faire la sélection du meilleur     #
#          pion, a chaque fois l'IA fesait le meilleur mouvement   #
#          seul problème, l'affichage montré quelque chose de      #
#          totalement différent, et je n'ait pas réussi a le fix   #
####################################################################

import os
import random
import time

random.seed()


##########################################################################################
# DEBUT ATELIER 4 (Standard)                                                             #

####################################################################################
# scan_pos permet de vérfier si le positionnement est sur l'un des bord du plateau #
####################################################################################
def scan_pos(grille, ligne, colonne, element):
    if ligne < 0 or colonne < 0:
        return False
    if ligne == len(grille) or colonne == len(grille):
        return False
    return grille[ligne][colonne] == element


#####################################################################################
# deplacement_ia permet de scanner les déplacement possible:                        #
#   - On liste les mouvement disponible.                                            #
#   - L'ia choisi aléatoirement l'un d'entre eux                                    #
#   - On renvoie les coordonées                                                     #
#####################################################################################


def deplacement_ia(grille, joueur_actuel, ligne, colonne):
    # On test voir quel déplacement est possible #
    mouvement_ia = []
    if scan_pos(grille, ligne + 1, colonne, "-"):
        mouvement_ia.append([ligne + 1, colonne])
    if scan_pos(grille, ligne - 1, colonne, "-"):
        mouvement_ia.append([ligne - 1, colonne])
    if scan_pos(grille, ligne, colonne + 1, "-"):
        mouvement_ia.append([ligne, colonne + 1])
    if scan_pos(grille, ligne, colonne - 1, "-"):
        mouvement_ia.append([ligne, colonne - 1])

    if joueur_actuel == "●":
        joueur_adverse = "○"
    else:
        joueur_adverse = "●"

    ################################################################################
    # Il s'agit du code qui rend l'IA "Intéligente".
    #
    best = 0
    valeur = 0
    # On cherche le meilleur mouvement pour le pion #
    for i in mouvement_ia:
        grille_de_test = grille.copy()
        actuel = capture(grille_de_test, i[0], i[1], joueur_actuel, joueur_adverse)
        if actuel > best:
            best = actuel
            valeur = i

    # Si y'en a pas, on appel le random #
    if valeur == 0:
        choix = random.randint(0, len(mouvement_ia) - 1)
        return mouvement_ia[choix][0], mouvement_ia[choix][1]
    return valeur[0], valeur[1]
    #
    #################################################################################


#####################################################################################
# tour_ia permet de simuler le tour d'une IA naîve :                                #
#   - On analyse les pions présent sur le plateau.                                  #
#   - L'ia choisi aléatoirement l'un d'entre eux                                    #
#   - On appelle la fonction "deplacement_ia"                                       #
#   - On vérifie les captures                                                       #
#####################################################################################

def tour_ia(grille, joueur_actuel):
    # On liste les pions sur le plateau #
    pions_ia = []
    for ligne_scan in range(0, len(grille)):
        for colonne_scan in range(0, len(grille[0])):
            if grille[ligne_scan][colonne_scan] == joueur_actuel:
                pions_ia.append([ligne_scan, colonne_scan])

    # On choisi l'un d'entre eux #
    choix = random.randint(0, len(pions_ia) - 1)
    ligne_depart = pions_ia[choix][0]
    colonne_depart = pions_ia[choix][1]

    # On demande le déplacement a faire #
    ligne_arrivee, colonne_arrivee = deplacement_ia(grille, joueur_actuel, ligne_depart, colonne_depart)

    # On l'applique #
    grille[ligne_depart][colonne_depart] = "-"
    grille[ligne_arrivee][colonne_arrivee] = joueur_actuel

    # On vérifie les capture #
    if joueur_actuel == "●":
        joueur_adverse = "○"
    else:
        joueur_adverse = "●"
    capture(grille, ligne_arrivee, colonne_arrivee, joueur_actuel, joueur_adverse)

    # On précise les déplacement effectuer #
    print(f"\nL'IA a choisi le pion, ligne {ligne_depart + 1}, colonne {colonne_depart + 1}.")
    print(f"et c'est déplacé, ligne {ligne_arrivee + 1}, colonne {colonne_arrivee + 1}.")
    print("\nRappel : Colonne 1 = A, Colonne J = 10\n")


#########################################################################
# partie_joueur_contre_joueur permet de faire une partie de la manière suivante :
# - On montre la grille
# - J1 Tour, puis update grille
# - Vérifie fin de partie
# - J2 Tour, puis update grille
# - Vérifie fin de partie
# En boucle
#########################################################################

def partie_joueur_contre_joueur(grille_choisi, joueur_actuel):
    # On affiche la grille #
    afficher_grille(grille_choisi)

    # print(f"....") permet de lire une variable entre {} dans un print)
    print(f"Tour des pions {joueur_actuel}")

    # Explication de ce while: Il est impossible dans les règles du jeu de finir sur une égalité. #
    # On vérifie si c'est une fin de partie, si oui, fin du code, sinon le code continue #
    while not fin_de_partie(grille_choisi):
        # On commence le tour du joueur actuel #
        tour_joueur(grille_choisi, joueur_actuel)

        # On réaffiche proprement la grille avec les changement #
        afficher_grille(grille_choisi)

        # On vérifie si c'est une fin de partie #
        # Si oui, fin du code #
        fin_de_partie(grille_choisi)
        # Sinon le code continue #

        # On patiente un peu #
        time.sleep(1)

        # On change de joueur, et on affiche le joueur désigné #
        if joueur_actuel == "●":
            joueur_actuel = "○"
        else:
            joueur_actuel = "●"
        print(f"Tour des pions {joueur_actuel}")

        # On commence le tour du joueur actuel #
        tour_joueur(grille_choisi, joueur_actuel)

        # On réaffiche proprement la grille avec les changement #
        afficher_grille(grille_choisi)

        # On patiente un peu #
        time.sleep(1)

        # On change de joueur, et on affiche le joueur désigné #
        if joueur_actuel == "●":
            joueur_actuel = "○"
        else:
            joueur_actuel = "●"
        print(f"Tour des pions {joueur_actuel}")


#########################################################################
# partie_joueur_contre_ia_nul permet de faire une partie de la manière suivante :
# - On montre la grille
# - J1 Tour, puis update grille
# - Vérifie fin de partie
# - IA Tour, puis update grille
# - Vérifie fin de partie
# En boucle
# Je dit IA nul, puisque ici il s'agit de l'ia Naîve, elle n'est pas futé ducoup
#########################################################################

def partie_joueur_contre_ia_nul(grille_choisi, joueur_actuel):
    # On affiche la grille #
    afficher_grille(grille_choisi)

    # print(f"....") permet de lire une variable entre {} dans un print)
    print(f"Tour des pions {joueur_actuel}")

    # Explication de ce while: Il est impossible dans les règles du jeu de finir sur une égalité. #
    # On vérifie si c'est une fin de partie, si oui, fin du code, sinon le code continue #
    while not fin_de_partie(grille_choisi):
        # On commence le tour du joueur actuel #
        tour_joueur(grille_choisi, joueur_actuel)

        # On réaffiche proprement la grille avec les changement #
        afficher_grille(grille_choisi)

        # On vérifie si c'est une fin de partie #
        # Si oui, fin du code #
        fin_de_partie(grille_choisi)
        # Sinon le code continue #

        # On patiente un peu #
        time.sleep(1)

        # On change de joueur, et on affiche le joueur désigné #
        if joueur_actuel == "●":
            joueur_actuel = "○"
        else:
            joueur_actuel = "●"
        print(f"Tour des pions {joueur_actuel}")

        # On commence le tour du joueur actuel #
        tour_ia(grille_choisi, joueur_actuel)

        # On réaffiche proprement la grille avec les changement #
        afficher_grille(grille_choisi)

        # On patiente un peu #
        time.sleep(1)

        # On change de joueur, et on affiche le joueur désigné #
        if joueur_actuel == "●":
            joueur_actuel = "○"
        else:
            joueur_actuel = "●"
        print(f"Tour des pions {joueur_actuel}")


#########################################################################
# choix_jeu permet de choisir le mode de jeu que l'utilisateur souhaite #
#########################################################################

def choix_jeu():
    test_valide = False

    # On veut être sur que l'input est correct #
    while not test_valide:
        configuration = input("Veulliez sélectionner le mode de jeu :\n 1. "
                              "Joueur Contre Joueur\n 2. Joueur contre IA Naîve\n Votre choix : ")

        # Si il est correct on désigne le type de partie #
        # En faisant sa je fait en sorte que sa soit le bon input #
        if configuration == "1":
            return configuration
        elif configuration == "2":
            return configuration
        else:
            # Si il ne l'est pas, retourne une erreur #
            afficher_erreur("input01")


# FIN ATELIER 4 (Standard)                                                               #
##########################################################################################

##########################################################################################
# DEBUT ATELIER 3                                                                        #

#####################################################################################
# capture va être appelé pour vérifié si il y a une capture, elle va appelé
# deux fonctions, capture_verticale et capture_horizontale. Cela va permettre
# de tester toutes les possibilité sur le plateau.
#
# Explication : Les capture se font si un pion est entouré par deux pions adverse
#               de manière orthogonale. Cependant lorsqu'un pion ce déplace entre
#               ces deux pion lui même, il est protéger. Si on fait une fonction
#               qui analyse toute la grille, il nous faudrait faire une variable
#               de protection pour proteger les pions.
#               Pour palier à ce problème, j'ai décidé de juste analyser le déplacement.
#               Donc, on va juste tester toute les possiblité en fonction des endroit
#               ou sont les pions.
#####################################################################################

def capture(grille, ligne_arrivee, colonne_arrivee, joueur_actuel, joueur_adverse):

    nbr_capture = 0
    # On teste toute les possiblité de capture verticalement, -1 c'est dernière ligne (-2 avant dernière) #
    # +1 c'est première ligne (2 deuxième), 0 n'importe quelle ligne. #
    if ligne_arrivee == len(grille) - 1:
        nbr_capture += capture_verticale(grille, ligne_arrivee, colonne_arrivee, joueur_actuel, joueur_adverse, -1)
    elif ligne_arrivee == 0:
        nbr_capture += capture_verticale(grille, ligne_arrivee, colonne_arrivee, joueur_actuel, joueur_adverse, 1)
    elif ligne_arrivee == len(grille) - 2:
        nbr_capture += capture_verticale(grille, ligne_arrivee, colonne_arrivee, joueur_actuel, joueur_adverse, 2)
    elif ligne_arrivee == 1:
        nbr_capture += capture_verticale(grille, ligne_arrivee, colonne_arrivee, joueur_actuel, joueur_adverse, -2)
    else:
        nbr_capture += capture_verticale(grille, ligne_arrivee, colonne_arrivee, joueur_actuel, joueur_adverse, 0)

    # On teste toute les possiblité de capture horizontalement, -1 c'est dernière colonne (-2 avant dernière) #
    # +1 c'est première colonne (2 deuxième), 0 n'importe quelle colonne. #
    if colonne_arrivee == len(grille) - 1:
        nbr_capture += capture_horizontale(grille, ligne_arrivee, colonne_arrivee, joueur_actuel, joueur_adverse, -1)
    elif colonne_arrivee == 0:
        nbr_capture += capture_horizontale(grille, ligne_arrivee, colonne_arrivee, joueur_actuel, joueur_adverse, 1)
    elif colonne_arrivee == len(grille) - 2:
        nbr_capture += capture_horizontale(grille, ligne_arrivee, colonne_arrivee, joueur_actuel, joueur_adverse, 2)
    elif colonne_arrivee == 1:
        nbr_capture += capture_horizontale(grille, ligne_arrivee, colonne_arrivee, joueur_actuel, joueur_adverse, -2)
    else:
        nbr_capture += capture_horizontale(grille, ligne_arrivee, colonne_arrivee, joueur_actuel, joueur_adverse, 0)

    return nbr_capture


def capture_verticale(grille, ligne_arrivee, colonne_arrivee, joueur_actuel, joueur_adverse, position_y):
    nbr_capture_verticale = 0
    # Si au bord faire ça #
    if -1 <= position_y <= 1 and position_y != 0:
        if (grille[ligne_arrivee + position_y][colonne_arrivee] == joueur_adverse and
                grille[ligne_arrivee + (position_y * 2)][colonne_arrivee] == joueur_actuel):
            grille[ligne_arrivee + position_y][colonne_arrivee] = "-"
            nbr_capture_verticale += 1
    # Sinon si une case avant bord faire ça #
    elif -2 <= position_y <= 2 and position_y != 0:
        if grille[ligne_arrivee + (position_y // 2)][colonne_arrivee] == joueur_adverse:
            grille[ligne_arrivee + (position_y // 2)][colonne_arrivee] = "-"
            nbr_capture_verticale += 1
        if (grille[ligne_arrivee - (position_y // 2)][colonne_arrivee] == joueur_adverse and
                grille[ligne_arrivee - position_y][colonne_arrivee] == joueur_actuel):
            grille[ligne_arrivee - (position_y // 2)][colonne_arrivee] = "-"
            nbr_capture_verticale += 1
    # Sinon faire ça #
    else:
        if (grille[ligne_arrivee + 1][colonne_arrivee] == joueur_adverse and
                grille[ligne_arrivee + +2][colonne_arrivee] == joueur_actuel):
            grille[ligne_arrivee + 1][colonne_arrivee] = "-"
            nbr_capture_verticale += 1
        if (grille[ligne_arrivee - 1][colonne_arrivee] == joueur_adverse and
                grille[ligne_arrivee - 2][colonne_arrivee] == joueur_actuel):
            grille[ligne_arrivee - 1][colonne_arrivee] = "-"
            nbr_capture_verticale += 1
    return nbr_capture_verticale


def capture_horizontale(grille, ligne_arrivee, colonne_arrivee, joueur_actuel, joueur_adverse, position_x):
    nbr_capture_horizontale = 0
    # Si au bord faire ça #
    if -1 <= position_x <= 1 and position_x != 0:
        if (grille[ligne_arrivee][colonne_arrivee + position_x] == joueur_adverse and
                grille[ligne_arrivee][colonne_arrivee + (position_x * 2)] == joueur_actuel):
            grille[ligne_arrivee][colonne_arrivee + position_x] = "-"
            nbr_capture_horizontale += 1
    # Sinon si une case avant bord faire ça #
    elif -2 <= position_x <= 2 and position_x != 0:
        if grille[ligne_arrivee][colonne_arrivee + (position_x // 2)] == joueur_adverse:
            grille[ligne_arrivee][colonne_arrivee + (position_x // 2)] = "-"
            nbr_capture_horizontale += 1
        if (grille[ligne_arrivee][colonne_arrivee - (position_x // 2)] == joueur_adverse and
                grille[ligne_arrivee][colonne_arrivee - position_x] == joueur_actuel):
            grille[ligne_arrivee][colonne_arrivee - (position_x // 2)] = "-"
            nbr_capture_horizontale += 1
    # Sinon faire ça #
    else:
        if (grille[ligne_arrivee][colonne_arrivee + 1] == joueur_adverse and
                grille[ligne_arrivee][colonne_arrivee + 2] == joueur_actuel):
            grille[ligne_arrivee][colonne_arrivee + 1] = "-"
            nbr_capture_horizontale += 1
        if (grille[ligne_arrivee][colonne_arrivee - 1] == joueur_adverse and
                grille[ligne_arrivee][colonne_arrivee - 2] == joueur_actuel):
            grille[ligne_arrivee][colonne_arrivee - 1] = "-"
            nbr_capture_horizontale += 1
    return nbr_capture_horizontale


#####################################################################################
# fin_de_partie vérifie si il reste encore des pions sur le plateau.                #
# En fonction des pions restant, la victoire sera désigné, puis le code s'éteindra. #
# Note : Il n'y a pas de possibilité d'égalité selon les règles !                   #
#####################################################################################

def fin_de_partie(grille):
    noir = 0
    blanc = 0

    # On compte chaque pions sur la grille #
    for ligne in range(0, len(grille)):
        for colonne in range(0, len(grille[0])):
            if grille[ligne][colonne] == "●":
                blanc += 1
            if grille[ligne][colonne] == "○":
                noir += 1

    # Si il n'y a plus de pions noir => les blancs on gagné #
    if noir == 0:
        print("Les Blancs ont gagné. Félicitations !")
        input("Entrer pour terminer.... ")
        exit()

    # Si il n'y a plus de pions blanc => les noirs on gagné #
    if blanc == 0:
        print("Les Noirs ont gagné. Félicitations !")
        input("Entrer pour terminer.... ")
        exit()

    # Si il y a encore des pions de chaque côté, la partie continue #
    return False


#######################################################################################
# validation_deplacement vérifie si le joueur actuel peut bien jouer à cet endroit.   #
# Un déplacement n'est possible que si: case vide + déplacement orthogonale de 1 case #
#######################################################################################

def validation_deplacement(ligne_depart, colonne_depart, ligne_arrivee, colonne_arrivee, grille):
    # Es que la case est vide ? #
    if grille[ligne_arrivee][colonne_arrivee] != "-":
        # Si non erreur #
        afficher_erreur("move01")
        return False

    # Es que le déplacement est de 0 ? #
    if (ligne_depart == ligne_arrivee) and (colonne_depart == colonne_arrivee):
        # Si non erreur #
        afficher_erreur("move02")
        return False

    # Es que le déplacement est orthogonale et de 1 ? #
    if ((abs(ligne_depart - ligne_arrivee) == 1) and (abs(colonne_depart - colonne_arrivee) == 0) or
            (abs(ligne_depart - ligne_arrivee) == 0) and (abs(colonne_depart - colonne_arrivee) == 1)):
        # Si oui return True #
        return True
    # Si non erreur #
    afficher_erreur("move02")
    return False


#####################################################################################
# deplacement permet de définir le déplacement du joueur, grâce à l'appel de la     #
# fonction "saisir_coordonnees" il va pouvoir choisir le déplacement souhaitée      #
# puis le renvoyer a tour_joueur, pour que lui mette à jour la grille.              #
# Note : La fonction, serait beaucoup plus optimiser avec des continue, des break,  #
#        ou même de la récursion. Mais c'est interdit.                              #
#####################################################################################

def deplacement(grille, joueur_actuel):
    print("Sélection du pion :", end="\n     ")
    ligne_depart, colonne_depart = saisir_coordonnees(grille)

    # Vérifie si le pion désigné par l'input, est un pion du joueur #
    # Si tout est bon, return True #
    while grille[ligne_depart][colonne_depart] != joueur_actuel:
        # Si l'input n'est pas un pion ou n'appartient pas au joueur, afficher_erreur affiche une erreur #
        # Erreur : Input03 #
        afficher_erreur("input03")
        afficher_grille(grille)
        print("Sélection du pion :", end="\n     ")
        ligne_depart, colonne_depart = saisir_coordonnees(grille)

    print("Sélection de l'endroit ou vous voulez le déplacer :", end="\n     ")
    ligne_arrivee, colonne_arrivee = saisir_coordonnees(grille)

    # Appele "validation_deplacement" pour savoir si le déplacement est possible #
    # Si tout est bon, return True #
    while not validation_deplacement(ligne_depart, colonne_depart, ligne_arrivee, colonne_arrivee, grille):
        # Sinon on repasse par tout les test précédent #
        afficher_grille(grille)
        print("Sélection du pion a déplacer :", end="\n     ")
        ligne_depart, colonne_depart = saisir_coordonnees(grille)

        # Vérifie si le pion désigné par l'input, est un pion du joueur #
        # Si tout est bon, return True #
        while grille[ligne_depart][colonne_depart] != joueur_actuel:
            # Si l'input n'est pas un pion ou n'appartient pas au joueur, afficher_erreur affiche une erreur #
            # Erreur : Input03 #
            afficher_erreur("input03")
            afficher_grille(grille)
            print("Sélection du pion a déplacer :", end="\n     ")
            ligne_depart, colonne_depart = saisir_coordonnees(grille)

        print("Sélection de l'endroit ou vous voulez le déplacer :", end="\n     ")
        ligne_arrivee, colonne_arrivee = saisir_coordonnees(grille)
    return ligne_depart, colonne_depart, ligne_arrivee, colonne_arrivee


#####################################################################################
# tour_joueur permet de simuler le tour d'un joueur :                               #
#   - On appelle la fonction "deplacement"                                          #
#   - On récupère les coordonnées de départ et d'arrivée, on applique les           #
#     changement à la grille.                                                       #
#   - On appelle la fonction "capture"                                              #
#####################################################################################

def tour_joueur(grille, joueur_actuel):
    ligne_depart, colonne_depart, ligne_arrivee, colonne_arrivee = deplacement(grille, joueur_actuel)
    grille[ligne_depart][colonne_depart] = "-"
    grille[ligne_arrivee][colonne_arrivee] = joueur_actuel
    if joueur_actuel == "●":
        joueur_adverse = "○"
    else:
        joueur_adverse = "●"
    capture(grille, ligne_arrivee, colonne_arrivee, joueur_actuel, joueur_adverse)


# FIN ATELIER 3                                                                          #
##########################################################################################


############################################################################
# afficher_grille permet d'afficher le plateau de jeu dans le format voulu #
############################################################################

def afficher_grille(grille):
    chiffre_affichage = 1
    lettre_affichage = ord("A")

    # Au cas où, on verifie que la grille n'est pas vide ou est une n'est pas liste,
    # (malgré qu'il soit impossible que cela ce produise #
    if grille == [] or type(grille[0]) != type([]):
        return False

    # Print les lettre en haut du plateau #
    print("  ", end=" ▌ ")
    for colonne1 in range(0, len(grille[0])):
        if colonne1 == len(grille[0]) - 1:
            print(chr(lettre_affichage), end=" ▐ ")
        else:
            print(chr(lettre_affichage), end=" | ")
        lettre_affichage += 1
    print("")

    # Print le plateau entier (en ajoutant les numéro de case au début) #
    # print("    ▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁")
    print("    ───────────────────────────────────────")
    for ligne in range(0, len(grille)):
        if chiffre_affichage >= 10:
            print(chiffre_affichage, "▌ ", end="")
        else:
            print(f"0{chiffre_affichage}", "▌ ", end="")
        for colonne2 in range(0, len(grille[0])):
            if colonne2 == len(grille[0]) - 1:
                print(grille[ligne][colonne2], "▐ ", end="")
            else:
                print(grille[ligne][colonne2], "| ", end="")
        print("")
        chiffre_affichage += 1
    print("    ───────────────────────────────────────")
    # print("    ▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔")


################################################################################################################
# DEBUT DE LA PARTIE SUR LE TRAITEMENT DE L'INPUT                                                              #


######################################################################################
# saisir_coordonnees, va demandé un va ensuite appeler est_au_bon_format pour        #
# vérifier son format (qui va appelé est_dans_grille) puis va définir les coordonées #
# choisies.                                                                          #
######################################################################################

def saisir_coordonnees(grille):
    saisie_du_joueur = input("Sélectionner la case (Format Type : 'A01' (LettreChiffre)) : ")

    # On appelle les autre fonction pour savoir si l'input est correct #
    # Si l'input n'est pas correct, on redemande un autre input #
    while not est_au_bon_format(saisie_du_joueur, grille):
        afficher_grille(grille)
        saisie_du_joueur = input("Sélectionner la case (Format Type : 'A01' (LettreChiffre)) : ")
        print("")

    # Si tout est correct, on définie les input #
    colonne = ord(saisie_du_joueur[0].upper()) - ord("A")
    ligne = int(saisie_du_joueur[1] + saisie_du_joueur[2]) - 1

    # print(f"...") permet de print une variable entre {} #
    print(f"Vous avez choisi la case : {saisie_du_joueur}\n")

    # On return les valeurs #
    return ligne, colonne


##################################################################################
# est_au_bon_format (appelé par saisir_coordonnees) va vérifié si l'input est    #
# au bon format (A01) (LettreChiffre) puis va appelé est_dans_grille pour savoir #
# l'input est possible.                                                          #
##################################################################################

def est_au_bon_format(saisie_du_joueur, grille):
    # Vérifie si l'input fait bien 3 caractères #
    if len(saisie_du_joueur) == 3:

        # Vérifie si l'input est au format A01 (LettreChiffre) #
        if saisie_du_joueur[0].isalpha() and saisie_du_joueur[1].isdigit() and saisie_du_joueur[2].isdigit():
            temp_colonne = ord(saisie_du_joueur[0].upper()) - ord("A")
            temp_ligne = int(saisie_du_joueur[1] + saisie_du_joueur[2]) - 1

            # Demande a la fonction "est_dans_grille" de vérifier si l'input correspond a une case du plateau #
            if est_dans_grille(temp_ligne, temp_colonne, grille):
                # Si tout est bon, return True #
                return True
        else:
            # Si le format est incorrect, afficher_erreur affiche une erreur #
            # Erreur : Input01 #
            afficher_erreur("input01")
    else:
        afficher_erreur("input01")

    # Si il y a une erreur, return False #
    return False


########################################################################
# est_dans_grille (appelé par est_au_bon_format) va vérifié si l'input #
# correspond a une case dans la grille. (si il est valide)             #
########################################################################

def est_dans_grille(ligne, colonne, grille):
    # Vérifie si l'input ne dépasse pas la grille #
    # Si l'input dépasse la grille, afficher_erreur affiche une erreur et return False #
    if len(grille) <= ligne or ligne < 0 or colonne < 0 or len(grille[0]) <= colonne:
        # Erreur = Input02 #
        afficher_erreur("input02")
        return False

    # Si tout est bon, return True #
    return True


# FIN DE LA PARTIE SUR LE TRAITEMENT DE L'INPUT                                                                #
################################################################################################################

################################################################################################################
# DEBUT DES FONCTIONS FACULTATIVE                                                                              #


##########################################################################
# afficher_erreur permet de print l'erreur dans un format compréhensible #
# pour le joueur. Cela permet d'avoir un code plus propre                #
##########################################################################

def afficher_erreur(error):
    # Permet de clear la console (uniquement possible lors de l'exécution hors IDE) #
    # Cela donne un résultat plus propre #
    os.system("cls;clear")
    print("")
    print("####################################")

    # Les erreur de type Input #
    if len(error) >= 5 and error[0:5] == "input":

        # L'erreur input01 == L'input est dans un mauvais format (ou votre choix n'existe pas) #
        if error == "input01":
            print("Erreur : Mauvais Format !")

        # L'erreur input02 == L'input désigne une case n'existant pas sur le plateau #
        if error == "input02":
            print("Erreur : Out of range ! (Votre input ne correspond pas a une case du plateau !)")

        # L'erreur input03 == Le pion sélectionné n'appartient pas au joueur (ou il n'y a pas de pion) #
        if error == "input03":
            print("Erreur : Ceci n'est pas votre pion ! (Ou ceci n'est pas un pion)")

        print("Votre input est incorrect !")
        print("####################################", end="\n\n")

    if len(error) >= 4 and error[0:4] == "move":

        if error == "move01":
            print("Erreur : Cette case est déjà occupé !")

        if error == "move02":
            print("Erreur : Ce déplacement n'est pas possible ! (Vous ne pouvez pas faire un mouvement en diagonal, "
                  "ou un mouvement sur une case non adjacente, ou sur la même case.)")

        print("Votre mouvement est incorrect !")
        print("####################################", end="\n\n")

    return None


#####################################################################
# choix_grille permet de choisir au début, la grille souhaitée      #
#####################################################################

def choix_grille(grille_debut, grille_milieu, grille_fin):
    test_valide = False

    # On veut être sur que l'input est correct #
    while not test_valide:
        configuration = input("Veulliez sélectionner la configuration de jeu, dans laquelle vous voulez jouer :\n 1. "
                              "Début de partie\n 2. Milieu de partie\n 3. Fin de partie\nVotre choix : ")

        # Si il est correct on désigne la grille #
        if configuration == "1":
            return grille_debut, "●"
        elif configuration == "2":
            return grille_milieu, "○"
        elif configuration == "3":
            return grille_fin, "○"
        else:
            # Si il ne l'est pas, retourne une erreur #
            afficher_erreur("input01")


# FIN DES FONCTIONS FACULTATIVE                                                                                #
################################################################################################################

################################################################################################################
# DEBUT DE PARTIE SUR LES CONFIGURATIONS POSSIBLES                                                             #


# Le plateau au début de la partie #

grille_debut = [
    ["-", "-", "-", "-", "-", "-", "-", "-", "-", "-"],
    ["○", "○", "○", "○", "○", "○", "○", "○", "○", "○"],
    ["-", "-", "-", "-", "-", "-", "-", "-", "-", "-"],
    ["●", "●", "●", "●", "●", "●", "●", "●", "●", "●"],
    ["-", "-", "-", "-", "-", "-", "-", "-", "-", "-"],
    ["-", "-", "-", "-", "-", "-", "-", "-", "-", "-"],
    ["○", "○", "○", "○", "○", "○", "○", "○", "○", "○"],
    ["-", "-", "-", "-", "-", "-", "-", "-", "-", "-"],
    ["●", "●", "●", "●", "●", "●", "●", "●", "●", "●"],
    ["-", "-", "-", "-", "-", "-", "-", "-", "-", "-"]
]

# Le plateau en milieu de partie #

grille_milieu = [
    ["-", "-", "-", "-", "-", "-", "-", "-", "-", "-"],
    ["●", "-", "-", "○", "-", "○", "-", "-", "○", "○"],
    ["-", "○", "○", "-", "●", "-", "-", "○", "●", "-"],
    ["○", "●", "-", "-", "-", "-", "-", "●", "-", "●"],
    ["-", "●", "-", "-", "-", "○", "●", "-", "○", "-"],
    ["-", "-", "○", "-", "-", "-", "○", "-", "-", "-"],
    ["-", "○", "●", "○", "-", "-", "-", "-", "-", "-"],
    ["●", "●", "-", "-", "-", "-", "-", "●", "○", "○"],
    ["-", "-", "-", "●", "-", "●", "-", "-", "-", "●"],
    ["-", "-", "-", "-", "-", "-", "-", "-", "○", "-"]
]
# Le plateau en fin de partie #

grille_fin = [
    ["-", "-", "-", "-", "-", "-", "-", "-", "-", "-"],
    ["-", "-", "-", "-", "-", "●", "-", "-", "-", "-"],
    ["-", "-", "-", "-", "●", "-", "●", "-", "-", "-"],
    ["-", "-", "-", "-", "●", "○", "-", "●", "-", "-"],
    ["-", "●", "-", "-", "-", "-", "●", "-", "-", "-"],
    ["-", "-", "-", "-", "-", "-", "-", "-", "-", "-"],
    ["-", "-", "-", "-", "-", "-", "-", "-", "-", "-"],
    ["-", "-", "-", "-", "-", "-", "-", "-", "-", "-"],
    ["-", "-", "-", "-", "-", "-", "-", "-", "-", "-"],
    ["-", "-", "-", "-", "-", "-", "-", "-", "-", "-"]
]


# FIN DE PARTIE SUR LES CONFIGURATIONS POSSIBLES                                                               #
################################################################################################################

#########################################################################################################
# DEBUT TEST                                                                                            #

def test():
    grille_test = [
        ["-", "-", "-", "-", "-", "-", "-", "-", "-", "-"],
        ["-", "-", "-", "-", "-", "●", "-", "-", "-", "-"],
        ["-", "-", "-", "-", "●", "-", "●", "-", "-", "-"],
        ["-", "-", "-", "-", "●", "-", "○", "●", "-", "-"],
        ["-", "●", "-", "-", "-", "-", "●", "-", "-", "-"],
        ["-", "-", "-", "-", "-", "-", "-", "-", "-", "-"],
        ["-", "-", "-", "-", "-", "-", "-", "-", "-", "-"],
        ["-", "-", "-", "-", "-", "-", "-", "-", "-", "-"],
        ["-", "-", "-", "-", "-", "-", "-", "-", "-", "-"],
        ["-", "-", "-", "-", "-", "-", "-", "-", "-", "-"]
    ]
    capture(grille_test, 3, 6, "○", "●")
    assert grille_test == [
        ["-", "-", "-", "-", "-", "-", "-", "-", "-", "-"],
        ["-", "-", "-", "-", "-", "●", "-", "-", "-", "-"],
        ["-", "-", "-", "-", "●", "-", "●", "-", "-", "-"],
        ["-", "-", "-", "-", "●", "-", "○", "●", "-", "-"],
        ["-", "●", "-", "-", "-", "-", "●", "-", "-", "-"],
        ["-", "-", "-", "-", "-", "-", "-", "-", "-", "-"],
        ["-", "-", "-", "-", "-", "-", "-", "-", "-", "-"],
        ["-", "-", "-", "-", "-", "-", "-", "-", "-", "-"],
        ["-", "-", "-", "-", "-", "-", "-", "-", "-", "-"],
        ["-", "-", "-", "-", "-", "-", "-", "-", "-", "-"]
    ]
    grille_test = [
        ["-", "-", "-", "-", "-", "-", "-", "-", "-", "-"],
        ["-", "-", "-", "-", "-", "●", "-", "-", "-", "-"],
        ["-", "-", "-", "-", "●", "-", "●", "-", "-", "-"],
        ["-", "-", "-", "-", "-", "●", "○", "●", "-", "-"],
        ["-", "●", "-", "-", "-", "-", "●", "-", "-", "-"],
        ["-", "-", "-", "-", "-", "-", "-", "-", "-", "-"],
        ["-", "-", "-", "-", "-", "-", "-", "-", "-", "-"],
        ["-", "-", "-", "-", "-", "-", "-", "-", "-", "-"],
        ["-", "-", "-", "-", "-", "-", "-", "-", "-", "-"],
        ["-", "-", "-", "-", "-", "-", "-", "-", "-", "-"]
    ]
    capture(grille_test, 3, 5, "●", "○")
    assert grille_test == [
        ["-", "-", "-", "-", "-", "-", "-", "-", "-", "-"],
        ["-", "-", "-", "-", "-", "●", "-", "-", "-", "-"],
        ["-", "-", "-", "-", "●", "-", "●", "-", "-", "-"],
        ["-", "-", "-", "-", "-", "●", "-", "●", "-", "-"],
        ["-", "●", "-", "-", "-", "-", "●", "-", "-", "-"],
        ["-", "-", "-", "-", "-", "-", "-", "-", "-", "-"],
        ["-", "-", "-", "-", "-", "-", "-", "-", "-", "-"],
        ["-", "-", "-", "-", "-", "-", "-", "-", "-", "-"],
        ["-", "-", "-", "-", "-", "-", "-", "-", "-", "-"],
        ["-", "-", "-", "-", "-", "-", "-", "-", "-", "-"]
    ]
    grille_test = [
        ["-", "-", "-", "-", "-", "-", "-", "-", "-", "-"],
        ["-", "-", "-", "-", "-", "-", "-", "-", "-", "-"],
        ["-", "-", "-", "-", "-", "-", "-", "-", "-", "-"],
        ["-", "-", "-", "-", "-", "○", "●", "○", "-", "-"],
        ["-", "-", "-", "-", "-", "-", "-", "●", "-", "-"],
        ["-", "-", "-", "-", "-", "-", "-", "○", "-", "-"],
        ["-", "-", "-", "-", "-", "-", "-", "-", "-", "-"],
        ["-", "-", "-", "-", "-", "-", "-", "-", "-", "-"],
        ["-", "-", "-", "-", "-", "-", "-", "-", "-", "-"],
        ["-", "-", "-", "-", "-", "-", "-", "-", "-", "-"]
    ]
    capture(grille_test, 3, 7, "○", "●")
    assert grille_test == [
        ["-", "-", "-", "-", "-", "-", "-", "-", "-", "-"],
        ["-", "-", "-", "-", "-", "-", "-", "-", "-", "-"],
        ["-", "-", "-", "-", "-", "-", "-", "-", "-", "-"],
        ["-", "-", "-", "-", "-", "○", "-", "○", "-", "-"],
        ["-", "-", "-", "-", "-", "-", "-", "-", "-", "-"],
        ["-", "-", "-", "-", "-", "-", "-", "○", "-", "-"],
        ["-", "-", "-", "-", "-", "-", "-", "-", "-", "-"],
        ["-", "-", "-", "-", "-", "-", "-", "-", "-", "-"],
        ["-", "-", "-", "-", "-", "-", "-", "-", "-", "-"],
        ["-", "-", "-", "-", "-", "-", "-", "-", "-", "-"]
    ]
    print("Les test de la fonction capture sont réussi")
    print("La fonction déplacement et tour_joueur ne possède pas de test, puisque nous demandons un input joueur, "
          "et je ne peut pas tester ces fonctions avec des assert sans utiliser des méthode interdite par les règles.")


# FIN TEST                                                                                              #
#########################################################################################################

################################################################################################################
# CODE PRINCIPAL                                                                                               #

test()

# On demande le type de partie, puis on appelle les fonctions correspondantes pour commencer le jeu #
configuration = choix_jeu()
print("")
grille_choisi, joueur_actuel = choix_grille(grille_debut, grille_milieu, grille_fin)
os.system("cls;clear")
print("Lorsque vous exécuter le fichier .py dans l'invite de commande\nsi l'affichage est trop petit, utiliser"
      "Ctrl+Molette pour zoomer (ou l'outil loupe windows)", end="\n\n")

################################################################################################################
# CETTE MINI PARTIE N'EST PAS A EVALUER, enlever les # devant si vous voulez voir un combat IA contre IA       #
#
# afficher_grille(grille_choisi)
# print(f"Tour des pions {joueur_actuel}")
# while not fin_de_partie(grille_choisi):
#   tour_ia(grille_choisi, joueur_actuel)
#   afficher_grille(grille_choisi)
#   fin_de_partie(grille_choisi)
#   time.sleep(1)
#   if joueur_actuel == "●":
#       joueur_actuel = "○"
#   else:
#       joueur_actuel = "●"
#   print(f"Tour des pions {joueur_actuel}")
#   tour_ia(grille_choisi, joueur_actuel)
#   afficher_grille(grille_choisi)
#   time.sleep(1)
#   if joueur_actuel == "●":
#       joueur_actuel = "○"
#   else:
#       joueur_actuel = "●"
#   print(f"Tour des pions {joueur_actuel}")
#                                                                                                              #
################################################################################################################

# On commence un mode de jeu en fonction du choix #
if configuration == "1":
    partie_joueur_contre_joueur(grille_choisi, joueur_actuel)
elif configuration == "2":
    partie_joueur_contre_ia_nul(grille_choisi, joueur_actuel)

#############################################################################################################
# Permet d'éviter que le programme ce ferme soundainement (seulement lors d'une éxécution dans un terminal) #
input("Entrer pour terminer.... ")

#############################################################################################################

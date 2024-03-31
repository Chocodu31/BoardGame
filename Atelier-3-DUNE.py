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
#   stipulé (Si on retire tout les commentaire et retour à la      #
#   ligne que j'ai mit pour la lisibilité),                        #
#   (Hors "afficher_grille", celle-ci avait le droit d'être        #
#   plus longue).                                                  #
####################################################################

import os


##########################################################################################
# DEBUT ATELIER 3                                                                        #

def protection():
    print("")


def capture():
    print("")


def fin_de_partie(grille):
    noir = 0
    blanc = 0
    for ligne in range(0, len(grille)):
        for colonne in range(0, len(grille[0])):
            if grille[ligne][colonne] == "●":
                blanc += 1
            if grille[ligne][colonne] == "○":
                noir += 1
    if noir == 0:
        print("Les Blancs ont gagné. Félicitations !")
        return True
    if blanc == 0:
        print("Les Noirs ont gagné. Félicitations !")
        return True
    return False


#######################################################################################
# validation_deplacement vérifie si le joueur actuel peut bien jouer a cet endroit.   #
# Un déplacement n'est possible que si, case vide + déplacement orthogonale de 1 case #
#######################################################################################
def validation_deplacement(ligne_depart, colonne_depart, ligne_arrivee, colonne_arrivee, grille):
    if grille[ligne_arrivee][colonne_arrivee] != "-":
        afficher_erreur("move01")
        return False
    if (ligne_depart == ligne_arrivee) and (colonne_depart == colonne_arrivee):
        afficher_erreur("move02")
        return False
    if ((abs(ligne_depart - ligne_arrivee) == 1) and (abs(colonne_depart - colonne_arrivee) == 0) or
            (abs(ligne_depart - ligne_arrivee) == 0) and (abs(colonne_depart - colonne_arrivee) == 1)):
        return True
    afficher_erreur("move02")
    return False


#####################################################################################
# tour_joueur permet de simuler le tour d'un joueur, elle va passer par la fonction #
# "saisir_coordonnees" pour définir le mouvement que le joueur souhaite faire.      #
# Elle va ensuite appliqué ce mouvement a la grille, et définir les protection.     #
#####################################################################################

def tour_joueur(grille, joueur_actuel):
    ligne_depart, colonne_depart = saisir_coordonnees(grille)

    # Vérifie si le pion désigné par l'input, est un pion du joueur #
    # Si tout est bon, return True #
    while grille[ligne_depart][colonne_depart] != joueur_actuel:
        # Si l'input n'est pas un pion ou n'appartient pas au joueur, afficher_erreur affiche une erreur #
        # Erreur : Input03 #
        afficher_erreur("input03")
        ligne_depart, colonne_depart = saisir_coordonnees(grille)

    ligne_arrivee, colonne_arrivee = saisir_coordonnees(grille)

    # Appele "validation_deplacement" pour savoir si le déplacement est possible #
    while not validation_deplacement(ligne_depart, colonne_depart, ligne_arrivee, colonne_arrivee, grille):
        ligne_depart, colonne_depart = saisir_coordonnees(grille)
        while grille[ligne_depart][colonne_depart] != joueur_actuel:
            afficher_erreur("input03")
            ligne_depart, colonne_depart = saisir_coordonnees(grille)
        ligne_arrivee, colonne_arrivee = saisir_coordonnees(grille)


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
# Petite note : Il est stipulé dans le document que le tour du joueur ne doit pas    #
#               être pris en compte, c'est ce que j'ai fait.                         #
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
    print(f"Vous avez choisi : grille[{ligne}][{colonne}] = {grille[ligne][colonne]}")

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
            return grille_debut, [], "●"
        elif configuration == "2":
            return grille_milieu, [{3, 7}], "○"
        elif configuration == "3":
            return grille_fin, [], "○"
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

# On demande la grille voulu, on copie les informations de partie et on affiche la grille #
grille_choisi, pions_proteger, joueur_actuel = choix_grille(grille_debut, grille_milieu, grille_fin)
print("Lorsque vous exécuter le fichier .py dans l'invite de commande\nsi l'affichage est trop petit, utiliser"
      "Ctrl+Molette pour zoomer (ou l'outil loupe windows)", end="\n\n")
afficher_grille(grille_choisi)

# print(f"....") permet de lire une variable entre {} dans un print)
print(f"Tour des pions {joueur_actuel}")

#################################################################################
# Début de jeu suffit de mettre cela dans une boucle pour faire une vrai partie #
tour_joueur(grille_choisi, joueur_actuel)

# On vérifie si c'est une fin de partie #
fin_de_partie(grille_choisi)

# On change de joueur #
if joueur_actuel == "●":
    joueur_actuel = "○"
else :
    joueur_actuel = "●"

tour_joueur(grille_choisi, joueur_actuel)

# On vérifie si c'est une fin de partie #
fin_de_partie(grille_choisi)

# Permet d'éviter que le programme ce ferme soundainement (seulement lors d'une éxécution dans un terminal) #
input("Entrer pour terminer.... ")

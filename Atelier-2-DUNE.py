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
# - La fonction "show_error" permet d'afficher un message d'erreur #
#   (j'ai crée cette fonction dans le but d'avoir un code plus     #
#   clair).                                                        #
#   Elle n'était pas demandé cependant j'ai trouvé intéréssant     #
#   d'en faire une (pour être plus compréhensible).                #
#                                                                  #
# - ".isdigit" et ".isalpha" sont des outils de python             #
#   permettant de savoir si un caractère est un chiffre,           #
#   ou une lettre. (Elle n'ont pas était interdite d'utilisation,  #
#   j'ai vérifié au près du professeur présentant le cours amphi   #
#   de l'UE).                                                      #
#                                                                  #
# - La fonction "debuter_partie" permet de lancer une partie       #
#   en définisant via choix, les paramètres de celle-ci.           #
#   Elle n'était pas demandé cependant j'ai trouvé intéréssant     #
#   d'en faire une (pour être plus compréhensible et pratique).    #
#                                                                  #
# - L'ensemble des fonctions font moins de 15 lignes comme         #
#   stipulé (Si on retire tout les commentaire et retour à la      #
#   ligne que j'ai mit pour la lisibilité),                        #
#   (Hors "afficher_grille", celle-ci avait le droit d'être        #
#   plus longue).                                                  #
#                                                                  #
# - Puisque jeu de cet atelier ressemble fortement a un plateau    #
#   de jeu de dame/échec, je me suis donc caler sur les même       #
#   notation, c'est a dire la notation suivante :                  #
#    - Les Lettre représentes des colones (de gauche à droite)     #
#    - Les Chiffres représentes des lignes (de haut en bas)        #
#   Il n'y avait pas d'obligation pour ce choix (seulement des     #
#   conseils).                                                     #
####################################################################

import os


############################################################################
# afficher_grille permet d'afficher le plateau de jeu dans le format voulu #
############################################################################

def afficher_grille(grille):
    chiffre_show = 1
    lettre_show = ord("A")

    # Print les lettre en haut du plateau #
    print("  ", end=" ▌ ")
    for colonne1 in range(0, len(grille[0])):
        if colonne1 == len(grille[0]) - 1:
            print(chr(lettre_show), end=" ▐ ")
        else:
            print(chr(lettre_show), end=" | ")
        lettre_show += 1
    print("")

    # Print le plateau entier (en ajoutant les numéro de case au début) #
    # print("    ▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁")
    print("    ───────────────────────────────────────")
    for ligne in range(0, len(grille)):
        if chiffre_show >= 10:
            print(chiffre_show, "▌ ", end="")
        else:
            print(f"0{chiffre_show}", "▌ ", end="")
        for colonne2 in range(0, len(grille[0])):
            if colonne2 == len(grille[0]) - 1:
                print(grille[ligne][colonne2], "▐ ", end="")
            else:
                print(grille[ligne][colonne2], "| ", end="")
        print("")
        chiffre_show += 1
    print("    ───────────────────────────────────────")
    # print("    ▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔")


################################################################################################################
# DEBUT DE LA PARTIE SUR LE TRAITEMENT DE L'INPUT                                                              #


###################################################################################
# input_convertor, va convertir l'input en donnée lisible, mais va d'abord appelé #
# est_au_bon_format pour vérifié si l'input est au bon format.                    #
###################################################################################

def input_convertor(grille, player_turn):
    player_input = input("Sélectionner le pion (Format Type : 'A01' (LettreChiffre)) : ")

    # On appelle les autre fonction pour savoir si l'input est correct #
    # Si l'input n'est pas correct, on redemande un autre input #
    while not est_au_bon_format(player_input, grille, player_turn):
        player_input = input("Sélectionner le pion (Format Type : 'A01' (LettreChiffre)) : ")
        print("")

    # Si tout est correct, on définie les input #
    colonne = ord(player_input[0].upper()) - ord("A")
    ligne = int(player_input[1] + player_input[2]) - 1

    print(ligne, colonne)


############################################################################
# est_au_bon_format (appelé par input_convertor) va vérifié si l'input est #
# au bon format (A01) (LettreChiffre) puis va appelé est_dans_grille       #
# pour savoir l'input est possible                                         #
############################################################################

def est_au_bon_format(player_input, grille, player_turn):
    # Vérifie si l'input fait bien 3 caractères #
    if len(player_input) == 3:

        # Vérifie si l'input est au format A01 (LettreChiffre) #
        if player_input[0].isalpha() and player_input[1].isdigit() and player_input[2].isdigit():
            temp_colonne = ord(player_input[0].upper()) - ord("A")
            temp_ligne = int(player_input[1] + player_input[2]) - 1

            # Demande a la fonction "est_dans_grille" de vérifier si l'input correspond a une case du plateau #
            if est_dans_grille(temp_ligne, temp_colonne, grille):

                # Vérifie si le pion désigné par l'input, est un pion du joueur #
                # Si tout est bon, return True #
                if grille[temp_ligne][temp_colonne] == player_turn:
                    return True

                else:
                    # Si l'input n'est pas un pion ou n'appartient pas au joueur, show_error affiche une erreur #
                    # Erreur : Input03 #
                    show_error("input03")
        else:
            # Si le format est incorrect, show_error affiche une erreur #
            # Erreur : Input01 #
            show_error("input01")
    else:
        show_error("input01")

    # Si il y a une erreur, return False #
    return False


########################################################################
# est_dans_grille (appelé par est_au_bon_format) va vérifié si l'input #
# correspond a une case dans la grille. (si il est valide)             #
########################################################################

def est_dans_grille(ligne, colonne, grille):
    # Vérifie si l'input ne dépasse pas la grille #
    # Si l'input dépasse la grille, show_error affiche une erreur et return False #
    if len(grille) <= ligne or ligne < 0 or colonne < 0 or len(grille[0]) <= colonne:
        # Erreur = Input02 #
        show_error("input02")
        return False

    # Si tout est bon, return True #
    return True


# FIN DE LA PARTIE SUR LE TRAITEMENT DE L'INPUT                                                                #
################################################################################################################


#####################################################################
# show_error permet de print l'erreur dans un format compréhensible #
# pour le joueur. Cela permet d'avoir un code plus propre           #
#####################################################################

def show_error(error):
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
    return None


def debuter_partie():
    test_valide = False
    while not test_valide:
        configuration = input("Veulliez sélectionner la configuration de jeu, dans laquelle vous voulez jouer :\n 1. "
                              "Début de partie\n 2. Milieu de partie\n 3. Fin de partie\nVotre choix : ")
        for i in range(1, 3):
            if configuration == str(i):
                test_valide = True
    # faut faire une vérification ici mais j'ai la flemme (surtout j'arrive pas)
    tour_joueur = input("Veulliez sélectionner qui est la première personne a jouer :\n 1. ●"
                        "\n 2. ○\nVotre choix : ")


################################################################################################################
# DEBUT DE PARTIE SUR LES CONFIGURATIONS POSSIBLES                                                             #

# Le plateau au début de la partie #

grille_start = [
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

grille_mid = [
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

debuter_partie()
print("Lorsque vous exécuter le fichier .py dans l'invite de commande\nsi l'affichage est trop petit, utiliser"
      "Ctrl+Molette pour zoomer (ou l'outil loupe windows)", end="\n\n")
afficher_grille(grille_start)
player_turn = "●"
print(f"Tour des pions {player_turn}")
input_convertor(grille_start, player_turn)

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
#   (Elle n'était pas interdite d'utilisation, j'ai vérifié    #
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
# - La fonction "choix_grille" permet de lancer une partie         #
#   en définisant via choix, les paramètres de celle-ci.           #
#   Elle n'était pas demandé cependant j'ai trouvé intéréssant     #
#   d'en faire une (pour être plus compréhensible et pratique      #
#   lors de mes futur test).                                       #
#   Vous pouvez donc tester les affichage avec les différentes     #
#   configurations.                                                #
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
#   (Cela ne change rien au code)                                  #
####################################################################

import os


############################################################################
# afficher_grille permet d'afficher le plateau de jeu dans le format voulu #
############################################################################

def afficher_grille(grille):
    chiffre_show = 1
    lettre_show = ord("A")

    # Au cas où, on verifie que la grille n'est pas vide ou est une n'est pas liste,
    # (malgré qu'il soit impossible que cela ce produise #
    if grille == [] or type(grille[0]) != type([]):
        return False

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


######################################################################################
# saisir_coordonnees, va demandé un va ensuite appeler est_au_bon_format pour        #
# vérifier son format (qui va appelé est_dans_grille) puis va définir les coordonées #
# choisies.                                                                          #
# Petite note : Il est stipulé dans le document que le tour du joueur ne doit pas    #
#               être pris en compte, c'est ce que j'ai fait.                         #
######################################################################################

def saisir_coordonnees(grille):
    player_input = input("Sélectionner le pion (Format Type : 'A01' (LettreChiffre)) : ")

    # On appelle les autre fonction pour savoir si l'input est correct #
    # Si l'input n'est pas correct, on redemande un autre input #
    while not est_au_bon_format(player_input, grille):
        afficher_grille(grille)
        player_input = input("Sélectionner le pion (Format Type : 'A01' (LettreChiffre)) : ")
        print("")

    # Si tout est correct, on définie les input #
    colonne = ord(player_input[0].upper()) - ord("A")
    ligne = int(player_input[1] + player_input[2]) - 1

    # print(f"...") permet de print une variable entre {} #
    print(
        f"Les coordonée dans la grille sont\n Colonne : {colonne + 1}\n Ligne : {ligne + 1}\n"
        f"Vous avez choisi : grille[{ligne}][{colonne}] = {grille[ligne][colonne]}")

    # On return les valeurs #
    return ligne, colonne


##################################################################################
# est_au_bon_format (appelé par saisir_coordonnees) va vérifié si l'input est    #
# au bon format (A01) (LettreChiffre) puis va appelé est_dans_grille pour savoir #
# l'input est possible.                                                          #
##################################################################################

def est_au_bon_format(player_input, grille):
    # Vérifie si l'input fait bien 3 caractères #
    if len(player_input) == 3:

        # Vérifie si l'input est au format A01 (LettreChiffre) #
        if player_input[0].isalpha() and player_input[1].isdigit() and player_input[2].isdigit():
            temp_colonne = ord(player_input[0].upper()) - ord("A")
            temp_ligne = int(player_input[1] + player_input[2]) - 1

            # Demande a la fonction "est_dans_grille" de vérifier si l'input correspond a une case du plateau #
            if est_dans_grille(temp_ligne, temp_colonne, grille):
                # Si tout est bon, return True #
                return True
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

################################################################################################################
# DEBUT DES FONCTIONS FACULTATIVE                                                                              #


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


#####################################################################
# choix_grille permet de choisir au début, la grille souhaitée      #
#####################################################################

def choix_grille(grille_start, grille_mid, grille_fin):
    test_valide = False

    # On veut être sur que l'input est correct #
    while not test_valide:
        configuration = input("Veulliez sélectionner la configuration de jeu, dans laquelle vous voulez jouer :\n 1. "
                              "Début de partie\n 2. Milieu de partie\n 3. Fin de partie\nVotre choix : ")

        # Si il est correct on désigne la grille #
        if configuration == "1":
            return grille_start
        elif configuration == "2":
            return grille_mid
        elif configuration == "3":
            return grille_fin
        else:
            # Si il ne l'est pas, retourne une erreur #
            show_error("input01")


# FIN DES FONCTIONS FACULTATIVE                                                                                #
################################################################################################################

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

# On demande la grille voulu, on l'affiche, et on demande un input #
grille_selected = choix_grille(grille_start, grille_mid, grille_fin)
print("Lorsque vous exécuter le fichier .py dans l'invite de commande\nsi l'affichage est trop petit, utiliser"
      "Ctrl+Molette pour zoomer (ou l'outil loupe windows)", end="\n\n")
afficher_grille(grille_selected)
ligne_selected, colonne_selected = saisir_coordonnees(grille_selected)

print(ligne_selected, colonne_selected)

input("Entrer pour terminer.... ")

################################################################################################################
# DEBUT DE PARTIE SUR LES TEST DE FONCTIONS                                                                    #

# print("----------------\n DEBUT TEST\n----------------")
# assert est_dans_grille(100, 100, grille_start) == False
# print("----------------\n TEST REUSSI\n----------------")
# assert est_dans_grille(0, 0, grille_start) == True
# print("----------------\n TEST REUSSI\n----------------")
# assert est_au_bon_format("AO1", grille_start) == False
# print("----------------\n TEST REUSSI\n----------------")
# assert est_au_bon_format("A04", grille_start) == True
# print("----------------\n TEST REUSSI\n----------------")

# FIN DE PARTIE SUR LES TEST DE FONCTIONS                                                                      #
################################################################################################################

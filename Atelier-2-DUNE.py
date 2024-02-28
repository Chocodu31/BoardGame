####################################################################
# Avant de commencer a lire le code, il y a quelques précision que #
# je voudrais faire :                                              #
# - Les print("####################################") permettent   #
#   d'afficher un message d'erreur                                 #
# -
####################################################################


###########################
# Print le plateau de jeu #
###########################

def show_board(grille):
    chiffre_show = 1
    lettre_show = ord("A")
    # Print les lettre en haut du plateau#
    print("  ", end=" ▌ ")
    for k in range(0, len(grille[0])):
        if k == len(grille[0]) - 1:
            print(chr(lettre_show), end=" ▐ ")
        else:
            print(chr(lettre_show), end=" | ")
        lettre_show += 1
    print("")

    # Print le plateau entier (en ajoutant les numéro de case au début #
    print("    ▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁")
    for y in range(0, len(grille)):
        if chiffre_show >= 10:
            print(chiffre_show, "▌ ", end="")
        else:
            print(f"0{chiffre_show}", "▌ ", end="")
        for x in range(0, len(grille[0])):
            if x == len(grille[0]) - 1:
                print(grille[y][x], "▐ ", end="")
            else:
                print(grille[y][x], "| ", end="")
        print("")
        chiffre_show += 1
    print("    ▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔")


################################################################################################################
# DEBUT PARTIE : TRAITEMENT DE L'INPUT                                                                         #


###################################################################################
# input_convertor, va convertir l'input en donnée lisible, mais va d'abord appelé #
# est_au_bon_format pour vérifié si l'input est au bon format.                    #
###################################################################################

def input_convertor(grille, player_turn):
    player_input = input("Sélectionner le pion (Format Type : 'A01' (LettreChiffre)) : ")
    print("")

    # On appelle les autre fonction pour savoir si l'input est correct #
    while not est_au_bon_format(player_input, grille, player_turn):

        # Si l'input n'est pas correct, on affiche un Message d'Erreur #
        print("Votre input est incorrect !")
        print("####################################", end="\n\n")
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
                if grille[temp_ligne][temp_colonne] == player_turn:
                    # Si tout est bon, return True #
                    return True
                else:
                    # Si l'input n'est pas un pion ou n'appartient pas au joueur, on affiche un Message d'Erreur #
                    print("####################################")
                    print("Erreur : Ceci n'est pas votre pion ! (Ou ceci n'est pas un pion)")
    else:
        # Si le format est incorrect, on affiche un Message d'Erreur #
        print("####################################")
        print("Erreur : Mauvais Format !")
        # Ce message apparait aussi lorsque le pion sélectionnée n'apartient pas au joueur #

    # Si il y a une erreur, return False #
    return False


########################################################################
# est_dans_grille (appelé par est_au_bon_format) va vérifié si l'input #
# correspond a une case dans la grille. (si il est valide)             #
########################################################################

def est_dans_grille(ligne, colonne, grille):

    # Vérifie si l'input ne dépasse pas la grille #
    if len(grille) <= ligne or ligne < 0 or colonne < 0 or len(grille[0]) <= colonne:

        # Si l'input dépasse la grille, on affiche un Message d'Erreur #
        print("####################################")
        print("Erreur : Out of range ! (Votre input ne correspond pas a une case du plateau !)")
        # Si il y a une erreur, return False #
        return False

    # Si tout est bon, return True #
    return True


# FIN PARTIE : TRAITEMENT DE L'INPUT                                                                           #
################################################################################################################


# Le plateau #
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

show_board(grille_start)
player_turn = "●"

print(f"Tour des pions {player_turn}")
input_convertor(grille_start, player_turn)

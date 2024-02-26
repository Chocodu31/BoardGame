####################################################################
# Avant de commencer a lire le code, il y a quelques précision que #
# je voudrais faire :                                              #
# - Pour des questions de facilité, de lisibilité, et de           #
#   compréhension la première case d'un plateau de jeu est         #
#   considéré comme A0. (Rien de l'interdit).                      #
# -
####################################################################


###########################
# Print le plateau de jeu #
###########################

def show_board(grille):
    chiffre_show = 0
    lettre_show = ord("A")
    # Print the Letter #
    print(" ", end=" ▌ ")
    for k in range(0, len(grille[0])):
        if k == len(grille[0]) - 1:
            print(chr(lettre_show), end=" ▐ ")
        else:
            print(chr(lettre_show), end=" | ")
        lettre_show += 1
    print("")

    # Print the board #
    print("   ▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁")
    for y in range(0, len(grille)):
        print(chiffre_show, "▌ ", end="")
        for x in range(0, len(grille[0])):
            if x == len(grille[0]) - 1:
                print(grille[y][x], "▐ ", end="")
            else:
                print(grille[y][x], "| ", end="")
        print("")
        chiffre_show += 1
    print("   ▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔")


###################################################################################################
# DEBUT PARTIE : TRAITEMENT DE L'INPUT                                                            #

###################################################################################
# input_convertor, va convertir l'input en donnée lisible, mais va d'abord appelé #
# est_au_bon_format pour vérifié si l'input est au bon format.                    #
###################################################################################

def input_convertor(grille):
    playerinput = input("Sélectionner le pion (Format Type : 'A0' (LettreChiffre)) : ")

    # On appelle les autre fonction pour savoir si l'input est correct #
    while not est_au_bon_format(playerinput, grille):
        print("Mauvais format")
        playerinput = input("Sélectionner le pion (Format Type : 'A0' (LettreChiffre)) : ")
    colonne = ord(playerinput[0].upper()) - ord("A")
    ligne = int(playerinput[1])

    print(ligne, colonne)


############################################################################
# est_au_bon_format (appelé par input_convertor) va vérifié si l'input est #
# au bon format (A0) (LettreChiffre) puis va appelé est_dans_grille        #
# pour savoir l'input est possible                                         #
############################################################################

def est_au_bon_format(playerinput, grille):
    if len(playerinput) == 2:
        if playerinput[0].isalpha() and playerinput[1].isdigit():
            temp_colonne = ord(playerinput[0].upper()) - ord("A")
            temp_ligne = int(playerinput[1]) - 1
            if est_dans_grille(temp_ligne, temp_colonne, grille):
                return True
    return False


########################################################################
# est_dans_grille (appelé par est_au_bon_format) va vérifié si l'input #
# correspond a une case dans la grille.                                #
########################################################################

def est_dans_grille(ligne, colonne, grille):
    if len(grille) <= ligne or len(grille[0]) <= colonne:
        print("Out of range !")
        return False
    return True

# FIN PARTIE : TRAITEMENT DE L'INPUT                                                              #
###################################################################################################



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
input_convertor(grille_start)
# Affiche le plateau
def show(grille):
    for i in range(len(grille)):
        print(grille[i])

    
# Affiche les mouvement possible du pion choisi sur le plateau et demande quel move faire
def premove(grille, x1, y1, player):
    movegrille = list(map(list, grille))
    if movegrille[y1][x1 - 1] == "-":
        movegrille[y1][x1 - 1] = "4"
    if movegrille[y1][x1 + 1] == "-":
        movegrille[y1][x1 + 1] = "2"
    if movegrille[y1 - 1][x1] == "-":
        movegrille[y1 - 1][x1] = "1"
    if movegrille[y1 + 1][x1] == "-":
        movegrille[y1 + 1][x1] = "3"
    show(movegrille)
    while True:
        choice = int(input("Choose your move (0 = cancel)"))
        if choice == 0:
            return False
        elif choice == 1:
            showgrille

# Tour du Joueur 1 (□)
def p1turn(grille, dico):
    player = 1
    print("Player_1 turn !")
    print("Choose a piece")
    while True:
        letter = input(" Coordonée X (Lettres) : ")
        if letter in (dico):
            x1 = int(dico[letter])
            y1 = int(input(" Coordonée Y (Chiffre) : "))
            if (y1 < 1 or y1 >= len(grille[0])):
                print("Error : Out of range !")
            elif grille[y1][x1] == "□":
                # Si la position du pion est correcte
                print("You selected", letter, y1, ": ", grille[y1][x1])
                if premove(grille, x1, y1, player) == False:
                    continue
                else:
                    break
            else:
                print("Error : The case is empty, or it's not your piece !")
        else:
            print("Error : Out of range !")
    show(grille)


# Plateau de jeu
grille = [
    ["XX", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J"],
    ["01", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-"],
    ["02", "□", "□", "□", "□", "□", "□", "□", "□", "□", "□"],
    ["03", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-"],
    ["04", "■", "■", "■", "■", "■", "■", "■", "■", "■", "■"],
    ["05", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-"],
    ["06", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-"],
    ["07", "□", "□", "□", "□", "□", "□", "□", "□", "□", "□"],
    ["08", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-"],
    ["09", "■", "■", "■", "■", "■", "■", "■", "■", "■", "■"],
    ["10", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-"]
]

dico = {"A": 1, "B": 2, "C": 3, "D": 4, "E": 5, "F": 6, "G": 7, "H": 8, "I": 9, "J": 10}
show(grille)
p1turn(grille, dico)

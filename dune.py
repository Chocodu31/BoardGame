# Affiche le plateau
def show(grille):
    for i in range(len(grille)):
        print(grille[i])


# Affiche les mouvement possible du pion choisi sur le plateau et demande quel move faire
def moveshow(grille, x1, y1, player):
    valid = 0
    movegrille = list(map(list, grille))
    if movegrille[y1 - 1][x1] == "-":
        movegrille[y1 - 1][x1] = "1"
        valid += 1
    if movegrille[y1][x1 + 1] == "-":
        movegrille[y1][x1 + 1] = "2"
        valid += 1
    if movegrille[y1 + 1][x1] == "-":
        movegrille[y1 + 1][x1] = "3"
        valid += 1
    if movegrille[y1][x1 - 1] == "-":
        movegrille[y1][x1 - 1] = "4"
        valid += 1
    if valid == 0:
        return 0
    show(movegrille)
    while True:
        select = int(input("Choose your move between 1, 2, 3, and 4 (if they exist) ! (0 for cancel) : "))
        if select == 0:
            return 0
        elif select == 1 and movegrille[y1 - 1][x1] == "1":
            grille[y1][x1] = "-"
            grille[y1 - 1][x1] = player
            return "Up"
        elif select == 2 and movegrille[y1][x1 + 1] == "2":
            grille[y1][x1] = "-"
            grille[y1][x1 + 1] = player
            return "Right"
        elif select == 3 and movegrille[y1 + 1][x1] == "3":
            grille[y1][x1] = "-"
            grille[y1 + 1][x1] = player
            return "Down"
        elif select == 4 and movegrille[y1][x1 - 1] == "4":
            grille[y1][x1] = "-"
            grille[y1][x1 - 1] = player
            return "Left"
        print("Out of range !")


# Tour du Joueur 1 (□)
def p1turn(grille, dico):
    player = "□"
    print("Player_1 turn ! (□)")
    while True:
        print("Choose a piece")
        letter = input(" Coordonée X (Lettres) : ")
        if letter in (dico):
            x1 = int(dico[letter])
            y1 = int(input(" Coordonée Y (Chiffre) : "))
            if y1 < 1 or y1 >= len(grille[0]):
                print("Error : Out of range !")
            elif grille[y1][x1] == "□":
                # Si la position du pion est correcte
                print("You selected", letter, y1, ": ", grille[y1][x1])
                choice = moveshow(grille, x1, y1, player)
                if choice == 0:
                    print("Can't move that !")
                    continue
                elif choice == "Up":
                    break
            else:
                print("Error : The case is empty, or it's not your piece !")
        else:
            print("Error : Out of range !")
    show(grille)


# Tour du Joueur 2 (■)
def p2turn(grille, dico):
    player = "■"
    print("Player_2 turn ! (■)")
    while True:
        print("Choose a piece")
        letter = input(" Coordonée X (Lettres) : ")
        if letter in (dico):
            x1 = int(dico[letter])
            y1 = int(input(" Coordonée Y (Chiffre) : "))
            if y1 < 1 or y1 >= len(grille[0]):
                print("Error : Out of range !")
            elif grille[y1][x1] == "■":
                # Si la position du pion est correcte
                print("You selected", letter, y1, ": ", grille[y1][x1])
                choice = moveshow(grille, x1, y1, player)
                if choice == 0:
                    print("Can't move that !")
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
status = {0: "Dead", 1: "Alive", 2: "Protected"}
dico = {"A": 1, "B": 2, "C": 3, "D": 4, "E": 5, "F": 6, "G": 7, "H": 8, "I": 9, "J": 10, "a": 1, "b": 2, "c": 3, "d": 4,
        "e": 5, "f": 6, "g": 7, "h": 8, "i": 9, "j": 10}
pions1 = []
pions2 = []
# Begining analysis
for i in range(1, len(grille[0])):
    for k in range(1, len(grille)):
        if grille[i][k] == "□":
            pions1.append([i, k, 1])
        elif grille[i][k] == "■":
            pions2.append([i, k, 1])
print(pions1)
show(grille)
while True:
    p1turn(grille, dico)
    p2turn(grille, dico)
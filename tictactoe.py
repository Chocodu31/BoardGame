def xturn(grille):
    print("X turn !")
    while True:
        x1 = int(input(" Coordonée X (ligne) : ")) - 1
        y1 = int(input(" Coordonée Y (colonne) : ")) - 1
        if (x1 < 0 or x1 >= len(grille)) or (y1 < 0 or y1 >= len(grille[0])):
            print("Error : Out of range !")
        elif grille[x1][y1] == "-":
            grille[x1][y1] = "X"
            break
        else:
            print("Someone Already played here !")
    show(grille)


def oturn(grille):
    print("O turn !")
    while True:
        x1 = int(input(" Coordonée X (ligne) : ")) - 1
        y1 = int(input(" Coordonée Y (colonne) : ")) - 1
        if (x1 < 0 or x1 >= len(grille)) or (y1 < 0 or y1 >= len(grille[0])):
            print("Error : Out of range !")
        elif grille[x1][y1] == "-":
            grille[x1][y1] = "O"
            break
        else:
            print("Someone Already played here !")
    show(grille)


def win(grille):
    for i in range(len(grille)):
        if grille[i] == ["X", "X", "X"] or (
                grille[0][i] == grille[1][i] and grille[1][i] == grille[2][i] and grille[0][i] == "X") or (
                grille[0][0] == grille[1][1] and grille[1][1] == grille[2][2] and grille[0][0] == "X") or (
                grille[0][2] == grille[1][1] and grille[1][1] == grille[2][0] and grille[0][2] == "X"):
            print("X win !")
            return True
        if grille[i] == ["O", "O", "O"] or (
                grille[0][i] == grille[1][i] and grille[1][i] == grille[2][i] and grille[0][i] == "O") or (
                grille[0][0] == grille[1][1] and grille[1][1] == grille[2][2] and grille[0][0] == "O") or (
                grille[0][2] == grille[1][1] and grille[1][1] == grille[2][0] and grille[0][2] == "O"):
            print("O win !")
            return True
    return False


def draw(grille):
    tiret = 0
    for i in range(len(grille)):
        for k in range(len(grille[0])):
            if grille[i][k] == "-":
                tiret += 1
    if tiret > 0:
        return False
    print("Draw !")
    return True


def show(grille):
    for i in range(len(grille)):
        print(grille[i])


grille = [
    ["-", "-", "-"],
    ["-", "-", "-"],
    ["-", "-", "-"],
]
print("Tic-Tac-Toe")
show(grille)
while True:
    xturn(grille)
    if win(grille) or draw(grille):
        exit()
    oturn(grille)
    if win(grille) or draw(grille):
        exit()

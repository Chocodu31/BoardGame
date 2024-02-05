class TicTacToe:

    ######################################
    # Parameter for all the game (Board) #
    ######################################

    def __init__(self):
        self.grille = [
            ["-", "-", "-"],
            ["-", "-", "-"],
            ["-", "-", "-"],
        ]

    ###################
    # Print the board #
    ###################

    def show_board(self):
        print("—————————————————")
        for i in range(len(self.grille)):
            for k in range(len(self.grille)):
                print("|", self.grille[i][k], end=" | ")
            print("")
        print("—————————————————")

    #################################
    # The turn for the X (Player 1) #
    #################################

    def xturn(self):
        print("X turn !")
        while True:

            #############################
            # Movement look like this : #
            #      xx   y1   y2   y3    #
            #      x1 ["-", "-", "-"]   #
            #      x2 ["-", "-", "-"]   #
            #      x3 ["-", "-", "-"]   #
            #############################

            x1 = int(input(" Coordonée X (ligne) : ")) - 1
            y1 = int(input(" Coordonée Y (colonne) : ")) - 1

            # Check if it can be put there #
            if (x1 < 0 or x1 >= len(self.grille)) or (y1 < 0 or y1 >= len(self.grille[0])):
                print("Error : Out of range !")
            elif self.grille[x1][y1] == "-":
                self.grille[x1][y1] = "X"
                break
            else:
                print("Someone Already played here !")

    #################################
    # The turn for the O (Player 2) #
    #################################

    def oturn(self):
        print("O turn !")
        while True:
            x1 = int(input(" Coordonée X (ligne) : ")) - 1
            y1 = int(input(" Coordonée Y (colonne) : ")) - 1

            # Check if it can be put there #
            if (x1 < 0 or x1 >= len(self.grille)) or (y1 < 0 or y1 >= len(self.grille[0])):
                print("Error : Out of range !")
            elif self.grille[x1][y1] == "-":
                self.grille[x1][y1] = "O"
                break
            else:
                print("Someone Already played here !")

    ########################
    # Check if there a win #
    ########################

    def win(self):
        for i in range(len(self.grille)):
            if self.grille[i] == ["X", "X", "X"] or (
                    self.grille[0][i] == self.grille[1][i] and self.grille[1][i] == self.grille[2][i] and self.grille[0][i] == "X") or (
                    self.grille[0][0] == self.grille[1][1] and self.grille[1][1] == self.grille[2][2] and self.grille[0][0] == "X") or (
                    self.grille[0][2] == self.grille[1][1] and self.grille[1][1] == self.grille[2][0] and self.grille[0][2] == "X"):
                print("X win !")
                return True
            if self.grille[i] == ["O", "O", "O"] or (
                    self.grille[0][i] == self.grille[1][i] and self.grille[1][i] == self.grille[2][i] and self.grille[0][i] == "O") or (
                    self.grille[0][0] == self.grille[1][1] and self.grille[1][1] == self.grille[2][2] and self.grille[0][0] == "O") or (
                    self.grille[0][2] == self.grille[1][1] and self.grille[1][1] == self.grille[2][0] and self.grille[0][2] == "O"):
                print("O win !")
                return True
        return False

    #########################
    # Check if there a draw #
    #########################

    def draw(self):
        tiret = 0
        for i in range(len(self.grille)):
            for k in range(len(self.grille[0])):
                if self.grille[i][k] == "-":
                    tiret += 1
        if tiret > 0:
            return False
        print("Draw !")
        return True

    ##################
    # Start the game #
    ##################

    def start(self):
        print("Tic-Tac-Toe")
        # Show board #
        self.show_board()
        while True:
            # X turn, then show board #
            self.xturn()
            self.show_board()
            # Check if there a draw, or a win #
            if self.win() or self.draw():
                exit()
            # O turn, then show board
            self.oturn()
            self.show_board()
            # Check if there a draw, or a win #
            if self.win() or self.draw():
                exit()


tic_tac_toe = TicTacToe()
tic_tac_toe.start()

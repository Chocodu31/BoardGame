class Dune:

    ##################################################################################
    # Parameter for all the game (Board, corresponding status, corresponding letter) #
    ##################################################################################

    def __init__(self):
        # The board
        self.grille = [
            ["  ", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J"],
            ["01", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-"],
            ["02", "○", "○", "○", "○", "○", "○", "○", "○", "○", "○"],
            ["03", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-"],
            ["04", "●", "●", "●", "●", "●", "●", "●", "●", "●", "●"],
            ["05", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-"],
            ["06", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-"],
            ["07", "○", "○", "○", "○", "○", "○", "○", "○", "○", "○"],
            ["08", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-"],
            ["09", "●", "●", "●", "●", "●", "●", "●", "●", "●", "●"],
            ["10", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-"]
        ]

        ########################################
        # Maybe find another way
        self.status_dico = {0: "Dead", 1: "Alive", 2: "Protected"}
        ########################################

        ########################################
        # I need to replace this with ASCII code
        self.letter_dico = {"A": 1, "B": 2, "C": 3, "D": 4, "E": 5, "F": 6, "G": 7, "H": 8, "I": 9, "J": 10,
                            "a": 1, "b": 2, "c": 3, "d": 4, "e": 5, "f": 6, "g": 7, "h": 8, "i": 9, "j": 10}
        ########################################

        self.pions1 = []
        self.pions2 = []

    ###################
    # Print the board #
    ###################

    def show_board(self):

        # Print the Letter #
        print(self.grille[0][0], end=" ▌ ")
        for k in range(1, len(self.grille[0])):
            if k == len(self.grille[0])-1:
                print(self.grille[0][k], end=" ▐ ")
            else:
                print(self.grille[0][k], end=" | ")
        print("")

        # Print the board #
        print("    ▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁")
        for y in range(1, len(self.grille)):
            print(self.grille[y][0], "▌ ", end="")
            for x in range(1, len(self.grille[0])):
                if x == len(self.grille[0])-1:
                    print(self.grille[y][x], "▐ ", end="")
                else:
                    print(self.grille[y][x], "| ", end="")
            print("")
        print("    ▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔")

    ######################
    # Turn of the Player #
    ######################

    def player_turn(self):
        print("bruh")

    ########################
    # Check if there a win #
    ########################

    def win_test(self):
        print("bruh")

    #######################################
    # Will update the status of the piece #
    #######################################

    def piece_status(self):
        print("bruh")

    #############
    # TEST HERE #
    #############

    def begining_analysis(self):
        for i in range(1, len(self.grille[0])):
            for k in range(1, len(self.grille)):
                if self.grille[i][k] == "○":
                    self.pions1.append([i, k])
                elif self.grille[i][k] == "●":
                    self.pions2.append([i, k])

    ##################
    # Start the game #
    ##################

    def start(self):
        print("")
        print("             Dune game (Partonia)")
        print("")
        self.show_board()
        self.begining_analysis()


dune = Dune()
dune.start()

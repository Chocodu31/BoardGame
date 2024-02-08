class Dune:

    ##################################################################################
    # Parameter for all the game (Board, corresponding status, corresponding letter) #
    ##################################################################################

    def __init__(self):

        # The board #
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
            if k == len(self.grille[0]) - 1:
                print(self.grille[0][k], end=" ▐ ")
            else:
                print(self.grille[0][k], end=" | ")
        print("")

        # Print the board #
        print("    ▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁")
        for y in range(1, len(self.grille)):
            print(self.grille[y][0], "▌ ", end="")
            for x in range(1, len(self.grille[0])):
                if x == len(self.grille[0]) - 1:
                    print(self.grille[y][x], "▐ ", end="")
                else:
                    print(self.grille[y][x], "| ", end="")
            print("")
        print("    ▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔")

    #################################################
    # Turn input into readable data                 #
    # Clearly easier and faster with dictionary btw #
    #################################################

    def input_convertor(self, playerinput):
        x1 = 0
        y1 = 0
        if len(playerinput) == 2:

            # Detect if there a letter and a number in the playerinput #
            if (playerinput[0].isalpha() and playerinput[1].isdigit()) or (
                    playerinput[1].isalpha() and playerinput[0].isdigit()):
                if playerinput[0].isalpha():
                    x1 = ord(playerinput[0].upper()) - ord("A") + 1
                    y1 = playerinput[1]
                elif playerinput[1].isalpha():
                    x1 = ord(playerinput[1].upper()) - ord("A") + 1
                    y1 = playerinput[0]
                print(x1, y1)
                return True
            return False
        return False

    ######################
    # Turn of the Player #
    ######################

    def player_turn(self):
        print("bruh")
        playerinput = input("Input : ")
        self.input_convertor(playerinput)


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
        self.player_turn()

dune = Dune()
dune.start()

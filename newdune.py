class Dune:

    # Lorsque le jeu ce lance, les paramètre de base sont amorcé ici
    def __init__(self):
        # Plateau de jeu
        self.grille = [
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
        self.status = {0: "Dead", 1: "Alive", 2: "Protected"}
        self.dico = {"A": 1, "B": 2, "C": 3, "D": 4, "E": 5, "F": 6, "G": 7, "H": 8, "I": 9, "J": 10, "a": 1, "b": 2, "c": 3, "d": 4,
                "e": 5, "f": 6, "g": 7, "h": 8, "i": 9, "j": 10}

    def show_board(self):
        for i in range(len(self.grille)):
            print(self.grille[i])

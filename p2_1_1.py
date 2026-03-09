import random


class Dice_spiel:
    def __init__(self, min_wurf=1, max_wurf=6):
        self.min_wurf = min_wurf
        self.max_wurf = max_wurf
        self.amount_of_roll = 0
        self.statistics = {i: 0 for i in range(self.min_wurf, self.max_wurf + 1)}

    def roll_dice(self):
        number = random.randint(self.min_wurf, self.max_wurf)
        self.statistics[number] += 1
        self.amount_of_roll += 1
        return number

    def play_game(self):
        print("Willkommen zum Würfelspiel!")
        while True:
            input("Drücke Enter, um zu würfeln...")
            wurf = self.roll_dice()
            print(
                f"Du hast eine {wurf} geworfen! \nDu hast {self.amount_of_roll} Würfe gemacht. \nDie Statistik der Würfe: {self.statistics}"
            )
            if wurf == 6:
                self.reset_game()
                print("Glückwunsch! Du hast gewonnen!")
                break
            else:
                print("Versuche es erneut!")

    def reset_game(self):
        self.amount_of_roll = 0
        self.statistics = {i: 0 for i in range(self.min_wurf, self.max_wurf + 1)}


if __name__ == "__main__":
    spiel = Dice_spiel()
    spiel.play_game()

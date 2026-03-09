import random


class Dice_spiel:
    def __init__(self, min_wurf=1, max_wurf=6):
        self.min_wurf = min_wurf
        self.max_wurf = max_wurf

    def roll_dice(self):
        return random.randint(self.min_wurf, self.max_wurf)

    def play_game(self):
        print("Willkommen zum Würfelspiel!")
        while True:
            input("Drücke Enter, um zu würfeln...")
            wurf = self.roll_dice()
            print(f"Du hast eine {wurf} geworfen!")
            if wurf == 6:
                print("Glückwunsch! Du hast gewonnen!")
                break
            else:
                print("Versuche es erneut!")


if __name__ == "__main__":
    spiel = Dice_spiel()
    spiel.play_game()

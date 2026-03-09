import json
import random


class Dice_spiel:
    def __init__(self, min_wurf=1, max_wurf=6):
        self.min_wurf = min_wurf
        self.max_wurf = max_wurf
        self.load_game()

    def roll_dice(self):
        number = random.randint(self.min_wurf, self.max_wurf)
        self.statistics[number] += 1
        self.amount_of_roll += 1
        return number

    def reset_game(self):
        self.amount_of_roll = 0
        self.statistics = {i: 0 for i in range(self.min_wurf, self.max_wurf + 1)}

    def save_game(self, filename="dice_game_stats.json  "):
        with open(filename, "w") as file:
            json.dump(
                {
                    "amount_of_roll": self.amount_of_roll,
                    "statistics": self.statistics,
                },
                file,
                indent=4,
            )
        print(f"Spielstatistik wurde in {filename} gespeichert.")

    def load_game(self, filename="dice_game_stats.json  "):
        try:
            with open(filename, "r") as file:
                data = json.load(file)
                self.amount_of_roll = data.get("amount_of_roll", 0)
                row_stats = data.get("statistics", {})
                self.statistics = {int(k): v for k, v in row_stats.items()}
            print(f"Spielstatistik wurde aus {filename} geladen.")
        except FileNotFoundError:
            print("Keine gespeicherte Statistik gefunden. Starte ein neues Spiel.")
            self.reset_game()

    def play_game(self):
        print("Willkommen zum Würfelspiel!")
        while True:
            input("Drücke Enter, um zu würfeln...")
            wurf = self.roll_dice()
            print(
                f"Du hast eine {wurf} geworfen! \nDu hast {self.amount_of_roll} Würfe gemacht. \nDie Statistik der Würfe: {self.statistics}"
            )
            if wurf == 6:
                self.save_game()
                print("Glückwunsch! Du hast gewonnen!")
                self.reset_game()
                break
            else:
                print("Versuche es erneut!")


if __name__ == "__main__":
    spiel = Dice_spiel()
    spiel.play_game()

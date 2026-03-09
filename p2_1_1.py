import json
import os
import random

import yaml


class Dice_spiel:
    def __init__(self, min_wurf=1, max_wurf=6, filename="dice_game_stats"):
        self.min_wurf = min_wurf
        self.max_wurf = max_wurf
        self.filename = filename
        self.load_game()

    def roll_dice(self):
        number = random.randint(self.min_wurf, self.max_wurf)
        self.statistics[number] = self.statistics.get(number, 0) + 1
        self.amount_of_roll += 1
        return number

    def reset_game(self):
        self.amount_of_roll = 0
        self.statistics = {i: 0 for i in range(self.min_wurf, self.max_wurf + 1)}

    def save_game(self):
        format_choice = (
            input(
                "Möchtest du die Statistik als JSON oder YAML speichern? (json/yaml): "
            )
            .strip()
            .lower()
        )

        data_to_save = {
            "amount_of_roll": self.amount_of_roll,
            "statistics": self.statistics,
        }

        if format_choice == "yaml":
            full_path = f"{self.filename}.yaml"
            with open(self.filename + ".yaml", "w") as file:
                yaml.dump(
                    data_to_save,
                    file,
                )
                self.file_extention = ".yaml"
                print(f"Spielstatistik wurde in {full_path} gespeichert.")
        else:
            with open(self.filename + ".json", "w") as file:
                full_path = f"{self.filename}.json"
                json.dump(
                    data_to_save,
                    file,
                    indent=4,
                )
                self.file_extention = ".json"
            print(f"Spielstatistik wurde in {full_path} gespeichert.")

    def load_game(self):
        yaml_path = f"{self.filename}.yaml"
        json_path = f"{self.filename}.json"
        if os.path.exists(yaml_path):
            with open(yaml_path, "r") as file:
                data = yaml.safe_load(file)
                self.amount_of_roll = data.get("amount_of_roll", 0)
                self.statistics = data.get("statistics", {})
                print(f"Spielstatistik wurde aus {yaml_path} geladen.")
        elif os.path.exists(json_path):
            with open(json_path, "r") as file:
                data = json.load(file)
                self.amount_of_roll = data.get("amount_of_roll", 0)
                raw_stats = data.get("statistics", {})
                self.statistics = {int(k): v for k, v in raw_stats.items()}
                print(f"Spielstatistik wurde aus {json_path} geladen.")
        else:
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

from __future__ import annotations

from pathlib import Path
import argparse
from terminaltables import SingleTable

from agentics.events import clear, difficulty_screen, days_screen, main_screen
from agentics.classes import Player
from stockwolf.main import load_data, build_world
from stockwolf.engine.simulation import Simulation


def load_world(path: Path | None = None):
    """Load countries and market using StockWolf data."""
    data_path = path or Path(__file__).resolve().parents[1] / "stockwolf" / "data" / "official.yaml"
    data = load_data(data_path)
    countries, market, _ = build_world(data)
    return countries, market


def run(data_path: str | Path | None = None) -> None:
    """Run the integrated StockWolf/agentics game loop."""
    clear()
    try:
        logo = """\
           ___  ___  __  _______
          / _ \/ _ \/ / / / ___/
         / // / , _/ /_/ / (_ /
        /____/_/|_|\____/\___/  ___
           | | /| / / _ | / _ \/ __/
           | |/ |/ / __ |/ , _/\ \
           |__/|__/_/ |_/_/|_/___/"""
        title_screen = [
            [logo],
            ["        Created by Max Bridgland"],
            ["     Based on the DOS Game of the 80s"],
            [""],
            ["   Press ENTER to Play or Ctrl+C to Quit"],
            [""],
            ["  Version: 1.2.1  Report Bugs on GitHub"],
            ["https://github.com/M4cs/Drugwars/issues/new"],
        ]
        print(SingleTable(title_screen).table)
        input()

        player = Player()
        clear()
        diff = difficulty_screen()
        if diff == 0:
            player.shark.balance = 5500
        elif diff == 1:
            player.shark.balance = 6500
        elif diff == 2:
            player.shark.balance = 8000

        player.days_end = days_screen()

        countries, market = load_world(Path(data_path) if data_path else None)
        sim = Simulation(countries, market, [player])

        while True:
            main_screen(player)
            sim.tick()
    except KeyboardInterrupt:
        exit()


def cli() -> None:
    """Entry point for the console script."""
    parser = argparse.ArgumentParser(description="Run StockWolf agentics game")
    parser.add_argument("--yaml", "-y", type=Path, help="Path to YAML world file")
    args = parser.parse_args()
    run(args.yaml)


if __name__ == "__main__":
    cli()

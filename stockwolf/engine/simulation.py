from typing import List
from ..agents.country import CountryAgent
from ..agents.market import Market

class Simulation:
    def __init__(self, countries: List[CountryAgent], market: Market, players: List['Player']):
        self.countries = countries
        self.market = market
        self.players = players
        self.tick_count = 0

    def tick(self) -> None:
        self.tick_count += 1
        for country in self.countries:
            country.apply_policy(self.market)
        self.market.tick()

    def run(self, ticks: int = 10) -> None:
        for _ in range(ticks):
            self.tick()

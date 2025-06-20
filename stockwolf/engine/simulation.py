from __future__ import annotations

from typing import List, TYPE_CHECKING, Optional
from ..agents.country import CountryAgent
from ..agents.market import Market
from ..agents.regulator import RegulatorAgent
from ..agents.bank import BankAgent

if TYPE_CHECKING:
    from ..agents.player import Player

class Simulation:
    def __init__(
        self,
        countries: List[CountryAgent],
        market: Market,
        players: List['Player'],
        regulators: Optional[List[RegulatorAgent]] | None = None,
        banks: Optional[List[BankAgent]] | None = None,
    ):
        self.countries = countries
        self.market = market
        self.players = players
        self.regulators = regulators or []
        self.banks = banks or []
        self.tick_count = 0

    def tick(self) -> None:
        self.tick_count += 1
        for regulator in self.regulators:
            regulator.inspect_market(self.market)
        for bank in self.banks:
            bank.provide_liquidity(self.market)
        for country in self.countries:
            country.apply_policy(self.market)
        self.market.tick()

    def run(self, ticks: int = 10) -> None:
        for _ in range(ticks):
            self.tick()

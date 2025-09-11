from __future__ import annotations

from dataclasses import dataclass, field
from typing import List, TYPE_CHECKING

from ..agents.market import Market
from ..agents.country import CountryAgent
from ..agents.regulator import RegulatorAgent
from ..agents.bank import BankAgent

if TYPE_CHECKING:
    from ..agents.player import Player


@dataclass
class AgentSystem:
    """Core container managing the game's agents.

    This class holds collections of the different agent types and
    coordinates their interactions on each tick. Agents can be registered
    dynamically, allowing tests or future features to inject behaviour at
    runtime.
    """

    countries: List[CountryAgent] = field(default_factory=list)
    market: Market = field(default_factory=Market)
    players: List["Player"] = field(default_factory=list)
    regulators: List[RegulatorAgent] = field(default_factory=list)
    banks: List[BankAgent] = field(default_factory=list)
    tick_count: int = 0

    def add_country(self, country: CountryAgent) -> None:
        self.countries.append(country)

    def add_player(self, player: "Player") -> None:
        self.players.append(player)

    def add_regulator(self, regulator: RegulatorAgent) -> None:
        self.regulators.append(regulator)

    def add_bank(self, bank: BankAgent) -> None:
        self.banks.append(bank)

    def tick(self) -> None:
        """Advance the simulation by a single tick."""
        self.tick_count += 1
        for regulator in self.regulators:
            regulator.inspect_market(self.market)
        for bank in self.banks:
            bank.provide_liquidity(self.market)
        for country in self.countries:
            country.apply_policy(self.market)
        self.market.tick()

    def run(self, ticks: int = 1) -> None:
        """Run the system for ``ticks`` iterations."""
        for _ in range(ticks):
            self.tick()

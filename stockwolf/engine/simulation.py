from __future__ import annotations

from typing import List, TYPE_CHECKING, Optional
from ..agents.country import CountryAgent
from ..agents.market import Market
from ..agents.regulator import RegulatorAgent
from ..agents.bank import BankAgent
from .agent_system import AgentSystem

if TYPE_CHECKING:
    from ..agents.player import Player


class Simulation(AgentSystem):
    def __init__(
        self,
        countries: List[CountryAgent],
        market: Market,
        players: List["Player"],
        regulators: Optional[List[RegulatorAgent]] | None = None,
        banks: Optional[List[BankAgent]] | None = None,
    ) -> None:
        super().__init__(
            countries=countries,
            market=market,
            players=players,
            regulators=regulators or [],
            banks=banks or [],
        )

from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .player import Player

@dataclass
class Company:
    name: str
    ticker: str
    share_price: float
    dividend_yield: float = 0.0

    def pay_dividend(self, player: 'Player') -> float:
        """Return dividend amount for one share."""
        dividend = self.share_price * self.dividend_yield
        player.cash += dividend
        return dividend

    def expand(self) -> None:
        """Simple expansion increasing share price."""
        self.share_price *= 1.02

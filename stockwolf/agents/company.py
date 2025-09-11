"""Publicly traded company agent."""

from __future__ import annotations

from dataclasses import dataclass


@dataclass
class Company:
    """Represents a listed company with a share price."""

    name: str
    ticker: str
    share_price: float
    dividend_yield: float = 0.0
    country: str | None = None

    def pay_dividend(self, player: "Player") -> float:
        """Pay a dividend to *player* based on share price."""

        dividend = self.share_price * self.dividend_yield
        player.cash += dividend
        return dividend

    def expand(self) -> None:
        """Simple growth hook used in examples and tests."""

        self.share_price *= 1.02


__all__ = ["Company"]


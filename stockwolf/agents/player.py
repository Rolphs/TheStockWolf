"""Player agent representing a human or AI participant.

The player tracks available cash and a simple stock portfolio. It can
buy and sell shares from :class:`Company` instances listed on the
market.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Dict


@dataclass
class Player:
    """Basic player model with cash and owned shares."""

    name: str = "AI"
    cash: float = 10000.0
    portfolio: Dict[str, int] = field(default_factory=dict)

    @property
    def money(self) -> float:
        """Alias for :attr:`cash` used by some legacy code."""

        return self.cash

    @money.setter
    def money(self, value: float) -> None:
        self.cash = value

    def buy(self, company: "Company", quantity: int) -> None:
        """Buy shares of *company* adding them to the portfolio."""

        cost = company.share_price * quantity
        if self.cash >= cost:
            self.cash -= cost
            self.portfolio[company.ticker] = (
                self.portfolio.get(company.ticker, 0) + quantity
            )

    def sell(self, company: "Company", quantity: int, market_country: str | None = None) -> None:
        """Sell *quantity* shares if the player holds enough of them."""

        if self.portfolio.get(company.ticker, 0) >= quantity:
            self.portfolio[company.ticker] -= quantity
            price = company.share_price
            if market_country and company.country and market_country == company.country:
                price *= 1.1 if company.share_price > 0 else 0.9
            self.cash += price * quantity

    def value(self, market: "Market") -> float:
        """Total value of cash plus owned shares using market prices."""

        total = self.cash
        for ticker, qty in self.portfolio.items():
            if ticker in market.companies:
                total += market.companies[ticker].share_price * qty
        return total


__all__ = ["Player"]


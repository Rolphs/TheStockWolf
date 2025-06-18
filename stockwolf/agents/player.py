from __future__ import annotations

from dataclasses import dataclass, field
from typing import Dict, TYPE_CHECKING

if TYPE_CHECKING:
    from .company import Company
    from .market import Market

@dataclass
class Player:
    name: str = 'AI'
    cash: float = 10000.0
    portfolio: Dict[str, int] = field(default_factory=dict)

    def buy(self, company: 'Company', quantity: int) -> None:
        cost = company.share_price * quantity
        if self.cash >= cost:
            self.cash -= cost
            self.portfolio[company.ticker] = self.portfolio.get(company.ticker, 0) + quantity

    def sell(self, company: 'Company', quantity: int) -> None:
        if self.portfolio.get(company.ticker, 0) >= quantity:
            self.portfolio[company.ticker] -= quantity
            self.cash += company.share_price * quantity

    def value(self, market: 'Market') -> float:
        total = self.cash
        for ticker, qty in self.portfolio.items():
            if ticker in market.companies:
                total += market.companies[ticker].share_price * qty
        return total

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Dict, TYPE_CHECKING
import random

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

    def sell(self, company: 'Company', quantity: int, market_country: str | None = None) -> None:
        if self.portfolio.get(company.ticker, 0) >= quantity:
            self.portfolio[company.ticker] -= quantity
            price = company.share_price
            if market_country and company.country and market_country == company.country:
                # Polarize price when trading in the country of origin
                price *= random.choice([1.1, 0.9])
            self.cash += price * quantity

    def value(self, market: 'Market') -> float:
        total = self.cash
        for ticker, qty in self.portfolio.items():
            if ticker in market.companies:
                total += market.companies[ticker].share_price * qty
        return total

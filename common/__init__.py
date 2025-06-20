from __future__ import annotations

from dataclasses import dataclass, field
from typing import Dict, Any
import random


@dataclass
class Player:
    name: str = 'AI'
    cash: float = 10000.0
    portfolio: Dict[str, int] = field(default_factory=dict)

    @property
    def money(self) -> float:
        return self.cash

    @money.setter
    def money(self, value: float) -> None:
        self.cash = value

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
                price *= random.choice([1.1, 0.9])
            self.cash += price * quantity

    def value(self, market: 'Market') -> float:
        total = self.cash
        for ticker, qty in self.portfolio.items():
            if ticker in market.companies:
                total += market.companies[ticker].share_price * qty
        return total


@dataclass
class Company:
    name: str
    ticker: str
    share_price: float
    dividend_yield: float = 0.0
    country: str | None = None

    def pay_dividend(self, player: Player) -> float:
        dividend = self.share_price * self.dividend_yield
        player.cash += dividend
        return dividend

    def expand(self) -> None:
        self.share_price *= 1.02


@dataclass
class Market:
    companies: Dict[str, Company] = field(default_factory=dict)
    liquidity: float = 1.0

    def list_company(self, company: Company) -> None:
        self.companies[company.ticker] = company

    def update_prices(self) -> None:
        for company in self.companies.values():
            company.share_price *= self.liquidity

    def tick(self) -> None:
        self.update_prices()


@dataclass
class CountryAgent:
    name: str
    tax_rate: float
    interest_rate: float
    regulation: Dict[str, Any] = field(default_factory=dict)

    def apply_policy(self, market: Market) -> None:
        adjustment = 1 - self.tax_rate
        market.liquidity *= adjustment
        for company in market.companies.values():
            company.share_price *= 1 + (self.interest_rate - 0.05) * 0.01
            if getattr(company, 'country', None) == self.name:
                company.share_price *= random.choice([1.05, 0.95])


@dataclass
class RegulatorAgent:
    name: str = 'Regulator'
    power: float = 1.0


@dataclass
class BankAgent:
    name: str = 'Bank'
    funds: float = 1_000_000.0


@dataclass
class PlayerAgent:
    name: str = 'Bot'
    funds: float = 5000.0

__all__ = [
    'Player',
    'Company',
    'Market',
    'CountryAgent',
    'RegulatorAgent',
    'BankAgent',
    'PlayerAgent',
]

"""Financial market where companies are traded."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Dict


@dataclass
class Market:
    """A collection of listed companies and a liquidity factor."""

    companies: Dict[str, "Company"] = field(default_factory=dict)
    liquidity: float = 1.0

    def list_company(self, company: "Company") -> None:
        """List a new *company* on the market."""

        self.companies[company.ticker] = company

    def update_prices(self) -> None:
        """Update prices for all companies based on market liquidity."""

        for company in self.companies.values():
            company.share_price *= self.liquidity

    def tick(self) -> None:
        """Advance the market one step."""

        self.update_prices()


__all__ = ["Market"]


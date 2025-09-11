"""Country agent governing local economic policies."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Dict, Any
import random


@dataclass
class CountryAgent:
    """Adjusts market conditions based on taxation and interest rates."""

    name: str
    tax_rate: float
    interest_rate: float
    regulation: Dict[str, Any] = field(default_factory=dict)

    def apply_policy(self, market: "Market") -> None:
        """Modify market liquidity and company prices."""

        adjustment = 1 - self.tax_rate
        market.liquidity *= adjustment
        for company in market.companies.values():
            company.share_price *= 1 + (self.interest_rate - 0.05) * 0.01
            if getattr(company, "country", None) == self.name:
                company.share_price *= random.choice([1.05, 0.95])


__all__ = ["CountryAgent"]


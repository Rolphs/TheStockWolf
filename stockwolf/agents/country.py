from __future__ import annotations

from dataclasses import dataclass, field
from typing import Dict, Any, TYPE_CHECKING

if TYPE_CHECKING:
    from .market import Market

@dataclass
class CountryAgent:
    name: str
    tax_rate: float
    interest_rate: float
    regulation: Dict[str, Any] = field(default_factory=dict)

    def apply_policy(self, market: 'Market') -> None:
        """Apply country policy effects to the market each tick."""
        # simple example: adjust liquidity based on tax rate
        adjustment = 1 - self.tax_rate
        market.liquidity *= adjustment
        # interest_rate could affect company share prices globally
        for company in market.companies.values():
            company.share_price *= 1 + (self.interest_rate - 0.05) * 0.01

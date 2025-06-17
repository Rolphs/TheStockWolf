from dataclasses import dataclass, field
from typing import Dict

from .company import Company

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

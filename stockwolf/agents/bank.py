"""Bank agent providing liquidity to the market."""

from __future__ import annotations

from dataclasses import dataclass


@dataclass
class BankAgent:
    """Simplified bank with a pool of funds."""

    name: str = "Bank"
    funds: float = 1_000_000.0

    def provide_liquidity(self, market: "Market") -> None:
        """Increase market liquidity slightly each tick."""

        market.liquidity *= 1.01


__all__ = ["BankAgent"]


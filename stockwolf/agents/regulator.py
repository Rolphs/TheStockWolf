"""Regulator agent overseeing market activity."""

from __future__ import annotations

from dataclasses import dataclass


@dataclass
class RegulatorAgent:
    """Simple regulator with configurable power."""

    name: str = "Regulator"
    power: float = 1.0

    def inspect_market(self, market: "Market") -> None:
        """Inspect the market each tick.

        The default implementation does nothing but can be overridden
        by game logic or tests.
        """

        pass


__all__ = ["RegulatorAgent"]


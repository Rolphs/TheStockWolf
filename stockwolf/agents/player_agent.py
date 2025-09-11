"""Autonomous AI player agent used as competition."""

from dataclasses import dataclass


@dataclass
class PlayerAgent:
    """Minimal representation of an AI controlled player."""

    name: str = "Bot"
    funds: float = 5000.0


__all__ = ["PlayerAgent"]


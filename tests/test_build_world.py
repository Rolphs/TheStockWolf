import os
import sys
import yaml

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from stockwolf.main import build_world
from stockwolf.agents.market import Market


def test_build_world_creates_agents_and_lists_companies(monkeypatch):
    yaml_data = """
    countries:
      - name: AlphaLand
        tax_rate: 0.1
        interest_rate: 0.05
        companies:
          - name: One Corp
            ticker: ONE
            share_price: 10
      - name: BetaVille
        tax_rate: 0.2
        interest_rate: 0.07
        companies:
          - name: Two LLC
            ticker: TWO
            share_price: 20
          - name: Three Inc
            ticker: TRI
            share_price: 30
    """
    data = yaml.safe_load(yaml_data)

    calls = []
    original = Market.list_company

    def spy(self, company):
        calls.append(company.ticker)
        return original(self, company)

    monkeypatch.setattr(Market, "list_company", spy)

    countries, market, players = build_world(data)

    assert len(countries) == 2
    assert len(calls) == 3
    assert players[0].portfolio == {}

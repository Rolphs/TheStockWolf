import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from stockwolf.agents.market import Market
from stockwolf.agents.country import CountryAgent
from stockwolf.agents.regulator import RegulatorAgent
from stockwolf.agents.bank import BankAgent
from stockwolf.engine.simulation import Simulation


def test_regulators_and_banks_called(monkeypatch):
    market = Market()
    country = CountryAgent('X', tax_rate=0.1, interest_rate=0.05)
    regulator = RegulatorAgent()
    bank = BankAgent()

    calls = {
        'reg': 0,
        'bank': 0,
    }

    def inspect(self, m):
        calls['reg'] += 1

    def provide(self, m):
        calls['bank'] += 1

    monkeypatch.setattr(RegulatorAgent, 'inspect_market', inspect)
    monkeypatch.setattr(BankAgent, 'provide_liquidity', provide)

    sim = Simulation([country], market, [], regulators=[regulator], banks=[bank])
    sim.tick()

    assert calls['reg'] == 1
    assert calls['bank'] == 1

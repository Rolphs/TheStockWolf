import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from stockwolf.engine.agent_system import AgentSystem
from stockwolf.agents.country import CountryAgent
from stockwolf.agents.regulator import RegulatorAgent
from stockwolf.agents.bank import BankAgent
from stockwolf.agents.player import Player


def test_agent_system_registration_and_tick(monkeypatch):
    system = AgentSystem()
    country = CountryAgent('X', tax_rate=0.1, interest_rate=0.05)
    regulator = RegulatorAgent()
    bank = BankAgent()
    player = Player()

    calls = {'reg': 0, 'bank': 0, 'player': 0}

    def inspect(self, market):
        calls['reg'] += 1

    def provide(self, market):
        calls['bank'] += 1

    def act(self):
        calls['player'] += 1

    monkeypatch.setattr(RegulatorAgent, 'inspect_market', inspect)
    monkeypatch.setattr(BankAgent, 'provide_liquidity', provide)
    monkeypatch.setattr(Player, 'act', act, raising=False)

    system.add_country(country)
    system.add_regulator(regulator)
    system.add_bank(bank)
    system.add_player(player)
    system.tick()

    assert calls['reg'] == 1
    assert calls['bank'] == 1
    assert calls['player'] == 1
    assert system.tick_count == 1

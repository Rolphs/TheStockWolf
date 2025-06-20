import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from stockwolf.agents.regulator import RegulatorAgent
from stockwolf.agents.bank import BankAgent
from stockwolf.agents.player_agent import PlayerAgent


def test_regulator_defaults():
    agent = RegulatorAgent()
    assert agent.name == 'Regulator'
    assert agent.power == 1.0


def test_bank_defaults():
    agent = BankAgent()
    assert agent.name == 'Bank'
    assert agent.funds == 1_000_000.0


def test_player_agent_defaults():
    agent = PlayerAgent()
    assert agent.name == 'Bot'
    assert agent.funds == 5000.0

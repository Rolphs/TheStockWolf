import os
import sys
import yaml

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from stockwolf.main import build_world
from stockwolf.agents.regulator import RegulatorAgent
from stockwolf.agents.bank import BankAgent


def test_build_world_loads_optional_agents():
    yaml_data = """
    countries:
      - name: Land
        tax_rate: 0.1
        interest_rate: 0.05
    regulators:
      - name: Watchdog
        power: 2.0
    banks:
      - name: Central
        funds: 500000
    """
    data = yaml.safe_load(yaml_data)

    countries, market, players, regulators, banks = build_world(data)

    assert len(regulators) == 1
    assert isinstance(regulators[0], RegulatorAgent)
    assert regulators[0].name == 'Watchdog'
    assert len(banks) == 1
    assert isinstance(banks[0], BankAgent)
    assert banks[0].name == 'Central'

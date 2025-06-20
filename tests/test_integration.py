import os
import sys
import yaml

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from stockwolf.main import load_data, build_world
from stockwolf.engine.simulation import Simulation
from common import Player as BasePlayer
from agentics.classes import Player, CompanyPrices


def test_hybrid_loop_basic(tmp_path):
    yaml_data = """
    countries:
      - name: FooLand
        tax_rate: 0.1
        interest_rate: 0.05
        companies:
          - name: FooCorp
            ticker: FOO
            share_price: 10
    """
    path = tmp_path / "world.yaml"
    path.write_text(yaml_data)
    data = load_data(path)

    countries, market, _ = build_world(data)
    player = Player()
    setattr(player, 'foo', 0)
    comp = market.companies['FOO']

    BasePlayer.buy(player, comp, 2)
    initial_cash = player.cash
    initial_price = comp.share_price

    sim = Simulation(countries, market, [player])
    sim.run(ticks=2)

    new_price = market.companies['FOO'].share_price
    assert new_price != initial_price
    assert player.cash == initial_cash
    assert player.portfolio['FOO'] == 2
    assert player.value(market) == player.cash + new_price * 2


def test_yaml_propagates_to_inventory(tmp_path):
    yaml_data = """
    countries:
      - name: BarLand
        tax_rate: 0.1
        interest_rate: 0.05
        companies:
          - name: BarCorp
            ticker: BAR
            share_price: 5
    """
    path = tmp_path / "world.yaml"
    path.write_text(yaml_data)

    player = Player()
    prices = CompanyPrices(player, data_path=path)

    assert 'bar' in prices.available_companies
    assert getattr(player, 'bar', 0) == 0


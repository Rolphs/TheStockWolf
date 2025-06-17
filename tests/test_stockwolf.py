import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from stockwolf.agents.company import Company
from stockwolf.agents.player import Player
from stockwolf.agents.market import Market
from stockwolf.agents.country import CountryAgent
from stockwolf.engine.simulation import Simulation


def test_player_buy_sell():
    comp = Company(name='Test', ticker='T', share_price=10)
    player = Player()
    market = Market({'T': comp})
    player.buy(comp, 5)
    assert player.portfolio['T'] == 5
    assert player.cash == 10000 - 50
    player.sell(comp, 2)
    assert player.portfolio['T'] == 3
    assert player.cash == 10000 - 50 + 20


def test_simulation_tick():
    comp = Company(name='Test', ticker='T', share_price=10)
    market = Market({'T': comp})
    country = CountryAgent('Testland', tax_rate=0.1, interest_rate=0.05)
    sim = Simulation([country], market, [])
    sim.tick()
    assert sim.tick_count == 1
    assert market.companies['T'].share_price != 10  # price should change

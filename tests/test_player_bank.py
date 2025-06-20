import os
import sys
import pytest

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from agentics.classes import Player
from agentics.helpers import round_down


def test_player_buy_updates_inventory_and_money():
    p = Player()
    p.buy('umbrella', 5, 10)
    assert p.umbrella == 5
    assert p.money == 2000 - 5 * 10


def test_player_sell_updates_inventory_and_money():
    p = Player()
    p.umbrella = 8
    p.sell('umbrella', 3, 20)
    assert p.umbrella == 5
    assert p.money == 2000 + 3 * 20


def test_can_buy_exceed_coat_space_false():
    p = Player()
    p.max_trench = 10
    assert not p.can_buy(price=1, amount=20)


def test_bank_interest():
    p = Player()
    p.bank.balance = 1000
    p.bank.interest()
    assert p.bank.balance == int(round_down(1000 * 1.05))


def test_shark_interest():
    p = Player()
    p.shark.balance = 1000
    p.shark.interest()
    assert p.shark.balance == int(round_down(1000 * 1.08))


def test_shark_borrow_too_much():
    p = Player()
    p.money = 2000
    p.shark.balance = 1000
    assert not p.shark.check_can_borrow(1500)


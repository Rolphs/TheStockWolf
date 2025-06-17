import os
import sys
import pytest

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from drugwars import events

@pytest.mark.parametrize("r,expected", [
    (1,2), (2,2), (3,2), (4,2), (5,2), (6,2),
    (7,3), (8,3), (9,3),
    (10,4)
])
def test_cops_for_roll(r, expected):
    assert events.cops_for_roll(r) == expected


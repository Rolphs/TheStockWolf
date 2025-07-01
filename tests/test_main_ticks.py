import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from stockwolf.main import main


def _write_yaml(path):
    yaml_data = """
    countries:
      - name: Foo
        tax_rate: 0.1
        interest_rate: 0.05
    """
    path.write_text(yaml_data)


def test_main_runs_specified_ticks(tmp_path):
    path = tmp_path / "world.yaml"
    _write_yaml(path)
    sim = main(path, ticks=1)
    assert sim.tick_count == 1

    sim = main(path, ticks=3)
    assert sim.tick_count == 3

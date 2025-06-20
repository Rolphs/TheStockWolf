import argparse
import yaml
from .agents.country import CountryAgent
from .agents.company import Company
from .agents.market import Market
from .agents.player import Player
from .agents.regulator import RegulatorAgent
from .agents.bank import BankAgent
from .engine.simulation import Simulation
from pathlib import Path


def load_data(path: Path):
    with open(path) as f:
        return yaml.safe_load(f)


def build_world(data):
    market = Market()
    countries = []
    for cdata in data['countries']:
        comps = []
        for comp_data in cdata.get('companies', []):
            comp_data.setdefault('country', cdata['name'])
            comps.append(Company(**comp_data))
        country = CountryAgent(
            name=cdata['name'],
            tax_rate=cdata['tax_rate'],
            interest_rate=cdata['interest_rate'],
        )
        for comp in comps:
            market.list_company(comp)
        countries.append(country)

    regulators = [RegulatorAgent(**r) for r in data.get('regulators', [])]
    banks = [BankAgent(**b) for b in data.get('banks', [])]

    player = Player(name='Human')
    return countries, market, [player], regulators, banks


def main(path: str | Path | None = None) -> None:
    path = Path(path or Path(__file__).resolve().parent / 'data' / 'official.yaml')
    data = load_data(path)
    countries, market, players, regulators, banks = build_world(data)
    sim = Simulation(countries, market, players, regulators=regulators, banks=banks)
    sim.run(ticks=5)
    print(f"Simulation finished after {sim.tick_count} ticks")
    print(f"Player value: {players[0].value(market):.2f}")


def cli() -> None:
    """Entry point for console script."""
    parser = argparse.ArgumentParser(description="Run StockWolf simulation")
    parser.add_argument("--yaml", "-y", type=Path, help="Path to YAML world file")
    args = parser.parse_args()
    main(args.yaml)


if __name__ == '__main__':
    cli()

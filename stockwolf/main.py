import yaml
from .agents.country import CountryAgent
from .agents.company import Company
from .agents.market import Market
from .agents.player import Player
from .engine.simulation import Simulation
from pathlib import Path


def load_data(path: Path):
    with open(path) as f:
        return yaml.safe_load(f)


def build_world(data):
    market = Market()
    countries = []
    for cdata in data['countries']:
        comps = [Company(**comp) for comp in cdata.get('companies', [])]
        country = CountryAgent(name=cdata['name'], tax_rate=cdata['tax_rate'], interest_rate=cdata['interest_rate'])
        for comp in comps:
            market.list_company(comp)
        countries.append(country)
    player = Player(name='Human')
    return countries, market, [player]


def main(path: str = None):
    path = Path(path or Path(__file__).resolve().parent / 'data' / 'sample.yaml')
    data = load_data(path)
    countries, market, players = build_world(data)
    sim = Simulation(countries, market, players)
    sim.run(ticks=5)
    print(f"Simulation finished after {sim.tick_count} ticks")
    print(f"Player value: {players[0].value(market):.2f}")


if __name__ == '__main__':
    main()

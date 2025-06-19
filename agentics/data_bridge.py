from __future__ import annotations

from pathlib import Path
from typing import List, Dict, Any

from stockwolf.main import load_data


def load_yaml(path: Path | str) -> List[Dict[str, Any]]:
    """Load company data from a YAML file using ``stockwolf.main.load_data``.

    Parameters
    ----------
    path:
        Path to the YAML configuration.

    Returns
    -------
    list of dict
        A list of company dictionaries extracted from the file.
    """
    data = load_data(Path(path))
    companies: List[Dict[str, Any]] = []
    for cdata in data.get("countries", []):
        for comp in cdata.get("companies", []):
            companies.append(comp)
    return companies

"""Utility helpers for user input and game calculations."""

import os
import math

def check_ans_yn(a):
    """Return ``1`` for yes, ``2`` for no and ``0`` otherwise.

    Parameters
    ----------
    a : str
        The raw input string from the user.

    Returns
    -------
    int
        ``1`` for a *yes* response (``"y"`` or ``"r"``), ``2`` for a *no*
        response (``"n"`` or ``"f"``) and ``0`` for anything else.

    Examples
    --------
    >>> check_ans_yn('y')
    1
    >>> check_ans_yn('n')
    2
    """

    if a.lower() == "y" or a.lower() == "r":
        return 1
    elif a.lower() == "n" or a.lower() == "f":
        return 2
    else:
        return 0

def check_company_inp(a):
    """Map the user's input to a company name.

    Parameters
    ----------
    a : str
        Player input representing a company. Only the first character is used.

    Returns
    -------
    str or None
        The canonical company name or ``None`` if the input does not match any
        known company.

    Examples
    --------
    >>> check_company_inp('c')
    'acme'
    >>> check_company_inp('x') is None
    True
    """

    a = a.lower()
    companies = {
        "a": "acme",
        "g": "globex",
        "i": "initech",
        "u": "umbrella",
        "c": "cyberdyne",
        "s": "soylent",
    }
    if len(a) == 0:
        return None
    for k, v in companies.items():
        if k == a[0]:
            return v
    return None

def check_ans_bsj(a):
    """Return ``1`` for buy, ``2`` for sell, ``3`` for jet and ``0`` otherwise."""

    if a.lower() == "b":
        return 1
    elif a.lower() == "s":
        return 2
    elif a.lower() == "j":
        return 3
    else:
        return 0

def clear():
    """Clear the terminal screen."""

    os.system("cls" if os.name == "nt" else "clear")

def round_down(n, decimals=0):
    """Return ``n`` rounded down to ``decimals`` places."""

    multiplier = 10 ** decimals
    return int(math.floor(n * multiplier) / multiplier)

def get_price(prices, company):
    """Return the price of ``company`` from a :class:`~agentics.classes.CompanyPrices` instance."""

    return getattr(prices, company)

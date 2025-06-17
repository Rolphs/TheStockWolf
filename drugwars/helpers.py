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

def check_drug_inp(a):
    """Map the user's input to a drug name.

    Parameters
    ----------
    a : str
        Player input representing a drug. Only the first character is used.

    Returns
    -------
    str or None
        The canonical drug name or ``None`` if the input does not match any
        known drug.

    Examples
    --------
    >>> check_drug_inp('c')
    'cocaine'
    >>> check_drug_inp('x') is None
    True
    """

    a = a.lower()
    drugs = {
        "c": "cocaine",
        "h": "heroin",
        "a": "acid",
        "w": "weed",
        "s": "speed",
        "l": "ludes",
    }
    if len(a) == 0:
        return None
    for k, v in drugs.items():
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

def get_price(prices, drug):
    """Return the price of ``drug`` from a :class:`~drugwars.classes.Prices` instance."""

    if drug == "cocaine":
        return prices.cocaine
    elif drug == "heroin":
        return prices.heroin
    elif drug == "acid":
        return prices.acid
    elif drug == "weed":
        return prices.weed
    elif drug == "speed":
        return prices.speed
    elif drug == "ludes":
        return prices.ludes

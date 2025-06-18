"""Game object models for the Drugwars simulation."""

from random import randint, choice, seed, shuffle
from .helpers import round_down

class Shark:
    """Loan shark tracking the player's debt."""

    def __init__(self, player):
        self.player = player
        self.balance = 5500

    def interest(self):
        self.balance = int(round_down(self.balance * 1.08))

    def check_can_borrow(self, amount):
        if self.balance == 0 and amount <= int(round_down(self.player.money)):
            return True
        else:
            if amount <= int(round_down(self.balance)) and amount <= int(round_down(self.player.money)):
                return True
            else:
                return False
    
    def check_can_dep(self, amount):
        if amount <= self.player.money:
            return True
        else:
            return False

    def deposit(self, amount):
        self.player.money -= amount
        self.balance -= amount
    
    def withdraw(self, amount):
        self.player.money += amount
        self.balance += amount

class Bank:
    """Simple interest-bearing account for the player."""

    def __init__(self, player):
        self.player = player
        self.balance = 0

    def interest(self):
        self.balance = int(round_down(self.balance * 1.05))

    def deposit(self, amount):
        self.player.money -= amount
        self.balance += amount
    
    def withdraw(self, amount):
        self.player.money += amount
        self.balance -= amount

    def check_can_wd(self, amount):
        if amount <= self.balance:
            return True
        else:
            return False
    
    def check_can_dep(self, amount):
        if amount <= self.player.money:
            return True
        else:
            return False

class Stash:
    """Storage for excess shares not carried in the coat."""

    def __init__(self, player):
        self.player = player
        self.acme = 0
        self.globex = 0
        self.initech = 0
        self.umbrella = 0
        self.cyberdyne = 0
        self.soylent = 0

    def withdraw(self, company, amount):
        if hasattr(self.player, company):
            pref = getattr(self.player, company)
            pref += amount
            setattr(self.player, company, pref)
            sref = getattr(self, company)
            sref -= amount
            setattr(self, company, sref)

    def transfer(self, company, amount):
        if hasattr(self.player, company):
            pref = getattr(self.player, company)
            pref -= amount
            setattr(self.player, company, pref)
            sref = getattr(self, company)
            sref += amount
            setattr(self, company, sref)
    
    def can_transfer(self, company, amount):
        if hasattr(self.player, company):
            pref = getattr(self.player, company)
            return pref >= amount
        return False

    def can_withdraw(self, company, amount):
        if hasattr(self, company):
            pref = getattr(self, company)
            return pref >= amount
        return False

class Player:
    """State of the current player including inventory and money."""

    def __init__(self):
        self.is_first_round = True
        self.money = 2000
        self.guns = 0
        self.days = 0
        self.days_end = 30
        self.health = 20
        self.max_trench = 100
        self.acme = 0
        self.globex = 0
        self.initech = 0
        self.umbrella = 0
        self.cyberdyne = 0
        self.soylent = 0
        self.bank = Bank(self)
        self.stash = Stash(self)
        self.shark = Shark(self)
        self.current_area = "Bronx"
    
    def buy(self, company, amount, price):
        pref = getattr(self, company)
        pref += amount
        setattr(self, company, pref)
        self.money -= (amount * price)

    def len_inventory(self):
        return (self.acme + self.globex + self.initech + self.umbrella + self.cyberdyne + self.soylent)

    def coat_space(self):
        return self.max_trench - (self.acme + self.globex + self.initech + self.umbrella + self.cyberdyne + self.soylent)
    
    def get_max(self, company, price):
        max_amt = int(round_down(self.money / price))
        if max_amt > self.coat_space():
            return self.coat_space()
        else:
            return max_amt

    def get_max_sell(self, company):
        if company == 'acme':
            return self.acme
        elif company == 'globex':
            return self.globex
        elif company == 'initech':
            return self.initech
        elif company == 'umbrella':
            return self.umbrella
        elif company == 'cyberdyne':
            return self.cyberdyne
        elif company == 'soylent':
            return self.soylent

    def can_buy(self, price, amount):
        return self.money >= (price * amount) and (self.len_inventory() + amount) <= self.max_trench

    def can_sell(self, amount, company):
        pref = getattr(self, company)
        return pref - amount >= 0

    def get_amt(self, company):
        if hasattr(self, company):
            return getattr(self, company)
        return None

    def sell(self, company, amount, price):
        pref = getattr(self, company)
        pref -= amount
        setattr(self, company, pref)
        self.money += (amount * price)

class CompanyPrices:
    """Generate random share prices and place events."""

    def __init__(self, player):
        seed(randint(-10000, 10000))
        self.player = player
        self.acme = randint(15000, 29999)
        self.globex = randint(5000, 13999)
        self.initech = randint(1000, 4999)
        self.umbrella = randint(300, 899)
        self.cyberdyne = randint(90, 249)
        self.soylent = randint(10, 89)
        self.actions = []
        events = [
            lambda self: self.regulators_probe_acme(),
            lambda self: self.investors_buy_acme(),
            lambda self: self.regulators_probe_globex(),
            lambda self: self.investors_buy_globex(),
            lambda self: self.cheap_initech(),
            lambda self: self.cheap_acme(),
            lambda self: self.cheap_globex(),
            lambda self: self.cheap_soylent(),
            lambda self: self.cheap_cyberdyne(),
            lambda self: self.cheap_umbrella(),
        ]
        shuffle(events)
        self.action = None
        self.has_done_action = False
        if not self.player.is_first_round:
            for a in events:
                if self.has_done_action:
                    break
                else:
                    a(self)
        if len(self.actions) > 0:
            self.action = self.actions[0]
    
    def regulators_probe_acme(self):
        if 1 == randint(1, 35):
            self.acme *= 2
            self.actions.append("** Regulators investigated Acme! Shares are rising!! **")

    def investors_buy_acme(self):
        if 1 == randint(1, 35):
            self.acme *= 4
            self.actions.append("** Investors are hyped about Acme. Shares are skyrocketing!! **")

    def regulators_probe_globex(self):
        if 1 == randint(1, 25):
            self.globex *= 2
            self.actions.append("** Regulators hit Globex headquarters! Shares are rising!!! **")

    def investors_buy_globex(self):
        if 1 == randint(1, 35):
            self.globex *= 4
            self.actions.append("** Traders everywhere want Globex. Shares are skyrocketing!! **")
    
    def cheap_initech(self):
        if 1 == randint(1, 25):
            self.initech /= 4
            self.actions.append("** Initech discovered a cost-cutting breakthrough. Shares are cheap! **")
    
    def cheap_soylent(self):
        if 1 == randint(1, 20):
            self.soylent /= 4
            self.actions.append("** Soylent factory fiasco! Shares are extremely cheap **")
    
    def cheap_umbrella(self):
        if 1 == randint(1, 20):
            self.umbrella /= 4
            self.actions.append("** Umbrella giveaway promotion! Shares are practically free! **")

    def cheap_globex(self):
        if 1 == randint(1, 35):
            self.globex /= 4
            self.actions.append("** Globex shares flood the place! Prices have dropped!! **")

    def cheap_acme(self):
        if 1 == randint(1, 40):
            self.acme /= 4
            self.actions.append("** Retro comeback for Acme! Shares are on sale! **")

    def cheap_cyberdyne(self):
        if 1 == randint(1, 20):
            self.cyberdyne /= 4
            self.actions.append("** Cyberdyne expansion stalls. Shares are dropping! **")

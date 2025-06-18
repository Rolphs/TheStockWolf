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
        self.company_a = 0
        self.company_b = 0
        self.company_c = 0
        self.company_d = 0
        self.company_e = 0
        self.company_f = 0

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
        self.company_a = 0
        self.company_b = 0
        self.company_c = 0
        self.company_d = 0
        self.company_e = 0
        self.company_f = 0
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
        return (self.company_a + self.company_b + self.company_c + self.company_d + self.company_e + self.company_f)

    def coat_space(self):
        return self.max_trench - (self.company_a + self.company_b + self.company_c + self.company_d + self.company_e + self.company_f)
    
    def get_max(self, company, price):
        max_amt = int(round_down(self.money / price))
        if max_amt > self.coat_space():
            return self.coat_space()
        else:
            return max_amt

    def get_max_sell(self, company):
        """Return how many shares of ``company`` the player holds."""
        if hasattr(self, company):
            return getattr(self, company)
        return 0

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
        self.company_a = randint(15000, 29999)
        self.company_b = randint(5000, 13999)
        self.company_c = randint(1000, 4999)
        self.company_d = randint(300, 899)
        self.company_e = randint(90, 249)
        self.company_f = randint(10, 89)
        self.actions = []
        events = [
            lambda self: self.regulators_probe_company_a(),
            lambda self: self.investors_buy_company_a(),
            lambda self: self.regulators_probe_company_b(),
            lambda self: self.investors_buy_company_b(),
            lambda self: self.cheap_company_c(),
            lambda self: self.cheap_company_a(),
            lambda self: self.cheap_company_b(),
            lambda self: self.cheap_company_f(),
            lambda self: self.cheap_company_e(),
            lambda self: self.cheap_company_d(),
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
    
    def regulators_probe_company_a(self):
        if 1 == randint(1, 35):
            self.company_a *= 2
            self.actions.append("** Regulators investigated Company A! Shares are rising!! **")

    def investors_buy_company_a(self):
        if 1 == randint(1, 35):
            self.company_a *= 4
            self.actions.append("** Investors are hyped about Company A. Shares are skyrocketing!! **")

    def regulators_probe_company_b(self):
        if 1 == randint(1, 25):
            self.company_b *= 2
            self.actions.append("** Regulators hit Company B headquarters! Shares are rising!!! **")

    def investors_buy_company_b(self):
        if 1 == randint(1, 35):
            self.company_b *= 4
            self.actions.append("** Traders everywhere want Company B. Shares are skyrocketing!! **")
    
    def cheap_company_c(self):
        if 1 == randint(1, 25):
            self.company_c /= 4
            self.actions.append("** Company C discovered a cost-cutting breakthrough. Shares are cheap! **")
    
    def cheap_company_f(self):
        if 1 == randint(1, 20):
            self.company_f /= 4
            self.actions.append("** Company F factory fiasco! Shares are extremely cheap **")
    
    def cheap_company_d(self):
        if 1 == randint(1, 20):
            self.company_d /= 4
            self.actions.append("** Company D giveaway promotion! Shares are practically free! **")

    def cheap_company_b(self):
        if 1 == randint(1, 35):
            self.company_b /= 4
            self.actions.append("** Company B shares flood the place! Prices have dropped!! **")

    def cheap_company_a(self):
        if 1 == randint(1, 40):
            self.company_a /= 4
            self.actions.append("** Retro comeback for Company A! Shares are on sale! **")

    def cheap_company_e(self):
        if 1 == randint(1, 20):
            self.company_e /= 4
            self.actions.append("** Company E expansion stalls. Shares are dropping! **")

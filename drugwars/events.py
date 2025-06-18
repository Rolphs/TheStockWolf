"""High level game events and menus for the Drugwars text game."""

from terminaltables import SingleTable
from .helpers import (
    check_ans_yn,
    clear,
    round_down,
    check_ans_bsj,
    check_company_inp,
    get_price,
)
from .classes import CompanyPrices
from random import randint, choice


def cops_for_roll(r):
    """Return how many cops appear based on ``r``.

    Parameters
    ----------
    r : int
        A random roll between 1 and 10.

    Returns
    -------
    int
        Number of officers that should spawn.

    Examples
    --------
    >>> cops_for_roll(10)
    4
    """
    if 1 <= r <= 6:
        return 2
    elif 7 <= r <= 9:
        return 3
    else:
        return 4

def cops_chase(player):
    """Run the random police chase encounter."""

    if 1 == randint(1, 10):
        r = randint(1, 10)
        cops = cops_for_roll(r)
        print(SingleTable([["Officer Headass and " + str(cops) + " other(s) are chasing you!"]]).table)
        if player.guns >= 1:
            while True:
                print(SingleTable([["Would you like to (R)un or (F)ight?"], ["HP: " + str(player.health) + "/ 20"]]).table)
                a = input("\n> ")
                aout = check_ans_yn(a)
                if aout == 1:
                    if 1 == randint(1,3):
                        company = choice(["company_a", "company_b", "company_c", "company_d", "company_e", "company_f"])
                        pc = player.get_amt(company)
                        if pc > 0:
                            amnt = randint(1, 10)
                            pc -= amnt
                            clear()
                            print(SingleTable([["You got away but you dropped " + str(amnt) + " shares of " + company.capitalize() + " while running!!"]]).table)
                        else:
                            print(SingleTable([["You got away!"]]).table)
                        input("Press ENTER to Continue")
                        break
                    else:
                        if randint(1, 6) in [1,6]:
                            player.health -= 1
                            clear()
                            print(SingleTable([["You got hit by one of their shots and lost some health!"]]).table)
                        else:
                            company = choice(["company_a", "company_b", "company_c", "company_d", "company_e", "company_f"])
                            pc = player.get_amt(company)
                            if pc > 0:
                                amnt = randint(1, 10)
                                pc -= amnt
                                clear()
                                print(SingleTable([["You got away but you dropped " + str(amnt) + " shares of " + company.capitalize() + " while running!!"]]).table)
                            else:
                                print(SingleTable([["You got away!"]]).table)
                            input("Press ENTER to Continue")
                            break
                elif aout == 2:
                    if 1 == randint(1,6):
                        cops -= 1
                        if cops == 0:
                            company = choice(["company_a", "company_b", "company_c", "company_d", "company_e", "company_f"])
                            pc = player.get_amt(company)
                            if pc > 0:
                                amnt = randint(1, 10)
                                pc -= amnt
                                clear()
                                print(SingleTable([["You got away but you dropped " + str(amnt) + " shares of " + company.capitalize() + " while running!!"]]).table)
                            else:
                                print(SingleTable([["You got away!"]]).table)
                            input("Press ENTER to Continue")
                            break
                        clear()
                        print(SingleTable([["You took one of them out!"]]).table)
                    else:
                        player.health -= 1
                        clear()
                        print(SingleTable([["You got hit by one of their shots and lost some health!"]]).table)
        else:
            while True:
                print(SingleTable([["Press ENTER to Try and Run"], ["HP: " + str(player.health) + "/ 20"]]).table)
                input()
                if 1 == randint(1,3):
                    company = choice(["company_a", "company_b", "company_c", "company_d", "company_e", "company_f"])
                    pc = player.get_amt(company)
                    if pc > 0:
                        amnt = randint(1, 10)
                        pc -= amnt
                        clear()
                        print(SingleTable([["You got away but you dropped " + str(amnt) + " shares of " + company.capitalize() + " while running!!"]]).table)
                    else:
                        print(SingleTable([["You got away!"]]).table)
                    input("Press ENTER to Continue")
                    break
                else:
                    player.health -= 1
                    clear()
                    print(SingleTable([["You got hit by one of their shots and lost some health!"]]).table)
            clear()
            print(SingleTable([["You got away from the pigs!"]]).table)
            input("Press ENTER to Continue")


def ask_bank(player):
    """Prompt the player about visiting the bank."""

    clear()
    while True:
        print(SingleTable([['Would you like to visit the bank?']]).table)
        ans = input("\n> ")
        aout = check_ans_yn(ans)
        if aout == 1:
            clear()
            visit_bank(player)
            break
        elif aout == 2:
            clear()
            break

def ask_loan_shark(player):
    """Ask the player if they want to visit the loan shark."""

    clear()
    while True:
        print(SingleTable([['Would you like to visit the loan shark?']]).table)
        ans = input("\n> ")
        aout = check_ans_yn(ans)
        if aout == 1:
            clear()
            visit_loan_shark(player)
            break
        elif aout == 2:
            clear()
            break

def ask_stash(player):
    """Ask if the player wants to move items to or from their stash."""

    clear()
    while True:
        print(SingleTable([['Would you like to stash any shares?']]).table)
        ans = input("\n> ")
        aout = check_ans_yn(ans)
        if aout == 1:
            clear()
            visit_stash(player)
            break
        elif aout == 2:
            clear()
            break

def visit_stash(player):
    """Interactively deposit to or withdraw shares from the stash."""

    stashes = ["company_a", "company_b", "company_c", "company_d", "company_e", "company_f"]
    for stash in stashes:
        clear()
        while True:
            print(SingleTable([['How much ' + stash + ' would you like to deposit?'], ['Stash: ' + str(getattr(player.stash, stash)) + ' | Coat: ' + str(getattr(player, stash))]]).table)
            try:
                ans = int(input("\n> "))
                if ans == 0:
                    break
                else:
                    if player.stash.can_transfer(stash, ans):
                        player.stash.transfer(stash, ans)
                        break
                    else:
                        clear()
                        print(SingleTable([["You don't have that much!"]]).table)
            except ValueError as e:
                clear()
                print(SingleTable([["That isn't a number!"]]).table)
        while True:
            print(SingleTable([['How much ' + stash + ' would you like to take out?'], ['Stash: ' + str(getattr(player.stash, stash)) + ' | Coat: ' + str(getattr(player, stash))]]).table)
            try:
                ans = int(input("\n> "))
                if ans == 0:
                    break
                else:
                    if player.stash.can_withdraw(stash, ans):
                        player.stash.withdraw(stash, ans)
                        break
                    else:
                        clear()
                        print(SingleTable([["You don't have that much in your stash!"]]).table)
            except ValueError as e:
                clear()
                print(SingleTable([["That isn't a number!"]]).table)

def visit_bank(player):
    """Handle depositing to and withdrawing from the bank."""

    clear()
    if player.money > 0:
        while True:
            print(SingleTable([['How much would you like to deposit?'], ['Bank: ' + str(player.bank.balance) + ' | Wallet: ' + str(player.money)]]).table)
            try:
                ans = input("\n> ")
                if ans.lower() == "h" or ans.lower() == "half":
                    if player.bank.check_can_dep(int(round_down(player.money / 2))):
                        player.bank.deposit(int(round_down(player.money / 2)))
                        break
                ans = int(ans)
                if ans == 0:
                    break
                else:
                    if player.bank.check_can_dep(ans):
                        player.bank.deposit(ans)
                        break
                    else:
                        clear()
                        print(SingleTable([["You don't have that much!"]]).table)
            except ValueError as e:
                clear()
                print(SingleTable([["That isn't a number!"]]).table)
    clear()
    if player.bank.balance > 0:
        while True:
            print(SingleTable([['How much would you like to withdraw?'], ['Bank: ' + str(player.bank.balance) + ' | Wallet: ' + str(player.money)]]).table)
            try:
                ans = input("\n> ")
                if ans.lower() == "a" or ans.lower() == "all":
                    player.bank.withdraw(player.bank.balance)
                    break
                if ans.lower() == "h" or ans.lower() == "half":
                    player.bank.withdraw(int(round_down(player.shark.balance / 2)))
                    break
                ans = int(ans)
                if ans == 0:
                    break
                else:
                    if player.bank.check_can_wd(ans):
                        player.bank.withdraw(ans)
                        break
                    else:
                        clear()
                        print(SingleTable([["You don't have that much!"]]).table)
            except ValueError as e:
                clear()
                print(SingleTable([["That isn't a number!"]]).table)

def visit_loan_shark(player):
    """Repay or borrow money from the loan shark."""

    clear()
    while True:
        print(SingleTable([['How much would you like to repay?'], ['Debt: ' + str(player.shark.balance) + ' | Wallet: ' + str(player.money)]]).table)
        try:
            ans = input("\n> ")
            if ans.lower() == "a" or ans.lower() == "all":
                if player.shark.check_can_dep(player.shark.balance):
                    player.shark.deposit(player.shark.balance)
                    break
            if ans.lower() == "h" or ans.lower() == "half":
                if player.shark.check_can_dep(int(round_down(player.shark.balance / 2))):
                    player.shark.deposit(int(round_down(player.shark.balance / 2)))
                    break
            ans = int(ans)
            if ans == 0:
                break
            elif ans > player.shark.balance:
                clear()
                print(SingleTable([["That's more than you owe!"]]).table)
            else:
                if player.shark.check_can_dep(ans):
                    player.shark.deposit(ans)
                    break
                else:
                    clear()
                    print(SingleTable([["You don't have enough!"]]).table)
        except ValueError as e:
            clear()
            print(SingleTable([["That isn't a number!"]]).table)
    clear()
    while True:
        print(SingleTable([['How much would you like to borrow?'], ['Debt: ' + str(player.shark.balance) + ' | Wallet: ' + str(player.money)]]).table)
        try:
            ans = int(input("\n> "))
            if ans == 0:
                break
            else:
                if player.shark.check_can_borrow(ans):
                    player.shark.withdraw(ans)
                    break
                else:
                    clear()
                    print(SingleTable([["You can't take more than you owe or have already!"]]).table)
        except ValueError as e:
            clear()
            print(SingleTable([["That isn't a number!"]]).table)

def upgrade_coat(p):
    """Offer the player a trench coat upgrade for additional inventory."""

    clear()
    while True:
        price = randint(150, 250)
        if p.money >= price:
            print(SingleTable([["** Would you like to buy 15 more pockets for more shares? It's $" + str(price) + " **"], ["Wallet: ", p.money]]).table)
            a = input("\n> ")
            ao = check_ans_yn(a)
            if ao == 1:
                p.max_trench += 15
                p.money -= price
                clear()
                print(SingleTable([["You bought more trench pockets for $" + str(price)]]).table)
                input("Press ENTER to Continue")
                break
            elif ao == 2:
                break
            else:
                clear()
                print(SingleTable([["Please enter Y or N"]]).table)
                break
            input("Press ENTER to Continue")
            clear()
        else:
            break

def get_mugged(p):
    """Random chance for the player to lose money to a mugger."""

    clear()
    if 1 == randint(1, 8):
        clear()
        print(SingleTable([["You got mugged!! You lost " + str(p.money - int(round_down(p.money * 0.80))) + " dollars!"]]).table)
        p.money = int(round_down(p.money * 0.80))
        input("Press ENTER to Continue")
        clear()

def find_companies(p):
    """Chance to discover random shares on the ground."""

    clear()
    if 1 == randint(1, 10):
        clear()
        amnt = randint(1, 10)
        choice_num = randint(1, 6)
        cstr = ""
        if p.len_inventory() + amnt <= p.max_trench:
            if choice_num == 1:
                cstr = "Company A"
                p.company_a += amnt
            if choice_num == 2:
                cstr = "Company B"
                p.company_b += amnt
            if choice_num == 3:
                cstr = "Company C"
                p.company_c += amnt
            if choice_num == 4:
                cstr = "Company D"
                p.company_d += amnt
            if choice_num == 5:
                cstr = "Company E"
                p.company_e += amnt
            if choice_num == 6:
                cstr = "Company F"
                p.company_f += amnt
            print(SingleTable([["You found " + str(amnt) + " shares of " + cstr + " on the ground... \n NICE"]]).table)
            input("Press ENTER to Continue")

def buy_gun(p):
    """Random event offering the player a gun purchase."""

    clear()
    if 1 == randint(1, 5):
        clear()
        while True:
            price = randint(200, 300)
            print(SingleTable([["** Would you like to buy a gun for $" + str(price) + "? **"], ["Wallet: ", p.money]]).table)
            a = input("\n> ")
            ao = check_ans_yn(a)
            if ao == 1:
                p.guns += 1
                p.money -= price
                clear()
                print(SingleTable([["You bought a gun for $" + str(price)]]).table)
                input("Press ENTER to Continue")
                break
            elif ao == 2:
                break
            else:
                clear()
                print(SingleTable([["Please enter Y or N"]]).table)
                break
            input("Press ENTER to Continue")

def you_win(p):
    """Display the end screen and final score."""

    clear()
    score = int(round_down((p.bank.balance + p.money - p.shark.balance) / 10000000 * 100))
    if score > 100:
        score = 100
    if p.bank.balance + p.money - p.shark.balance < 0:
        score = 0
    print(SingleTable([["GAME OVER", f"You Reached {p.days_end} Days!"]]).table)
    print(SingleTable([["Your Total Money:", p.bank.balance + p.money - p.shark.balance]]).table)
    print(SingleTable([["Your Score:", str(score) + " out of 100"]]).table)
    if score >= 0 and score <= 30:
        print(SingleTable([["Dealer Rank", "Small Time Pusha... WEAK"]]).table)
    elif score >= 31 and score <= 50:
        print(SingleTable([["Dealer Rank", "Own The Block... NOT BAD"]]).table)
    elif score >= 51 and score <= 75:
        print(SingleTable([["Dealer Rank", "Run The Town... PRETTY GOOD"]]).table)
    elif score >= 76 and score <= 99:
        print(SingleTable([["Dealer Rank", "Kingpin... GOD DAMN"]]).table)
    else:
        print(SingleTable([["Dealer Rank", "PABLO ESCOBAR... YOU ARE A GOD"]]).table)
    exit()

def buy_menu(prices, inventory_table, pricing_table, money_table, p):
    """Prompt the player to purchase shares."""

    while True:
        print(SingleTable(inventory_table()).table)
        print(SingleTable(pricing_table(), title="Prices").table)
        print(SingleTable(money_table(), title="Money").table)
        print(SingleTable([["What would you like to buy?"]]).table)
        desired = input("\n> ")
        if not check_company_inp(desired):
            clear()
            print(SingleTable([["Enter the first letter of a company to choose!"]]).table)
        else:
            # Get some useful variables that will clean up the code a lot
            company = check_company_inp(desired)
            price = round_down(get_price(prices, company))
            max_allowed = p.get_max(company, price)
            
            print(SingleTable([["How much would you like to buy?"], [f"Max Allowed: {str(max_allowed)}"]]).table)
            desiredamnt = input("\n> ")

            # Calculate amount 
            try:
                amnt = int(desiredamnt)
            except ValueError:
                if desiredamnt.count('%') > 0:
                    if int(desiredamnt.replace('%', '')) > 100:
                        tmp = 100
                    else:
                        tmp = int(desiredamnt.replace('%', ''))

                    amnt = round_down(max_allowed * (tmp / 100))
                else:
                    if desiredamnt == 'a' or desiredamnt == 'all':
                        amnt = max_allowed
                    elif desiredamnt == 'h' or desiredamnt == 'half':
                        amnt = round_down(max_allowed / 2)
                    else:
                        clear()
                        print(SingleTable([["That isn't a valid amount!"]]).table)
                        continue
            
            # Buy the company
            if p.can_buy(price, amnt):
                p.buy(company, amnt, price)
                clear()
                print(SingleTable([[f"You bought {str(amnt)} shares of {company}!"]]).table)
                break
            else:
                clear()
                print(SingleTable([["You don't have enough money/coat space to buy that!"]]).table)
                break

def sell_menu(prices, inventory_table, pricing_table, money_table, p):
    """Allow the player to sell shares from their inventory."""

    while True:
        print(SingleTable(inventory_table()).table)
        print(SingleTable(pricing_table(), title="Prices").table)
        print(SingleTable(money_table(), title="Money").table)
        print(SingleTable([["What would you like to sell?"]]).table)
        desired = input("\n> ")
        if not check_company_inp(desired):
            clear()
            print(SingleTable([["Enter the first letter of a company to choose!"]]).table)
        else:
            # Get some useful variables that will clean up the code a lot
            company = check_company_inp(desired)
            price = round_down(get_price(prices, company))
            max_allowed = p.get_max_sell(company)

            print(SingleTable([["How much would you like to sell?"], [f"You have: {str(p.get_amt(company))} {company}"]]).table)
            desiredamnt = input("\n> ")

            # Calculate amount
            try:
                amnt = int(desiredamnt)
            except ValueError:
                if desiredamnt.count('%') > 0:
                    if int(desiredamnt.replace('%', '')) > 100:
                        tmp = 100
                    else:
                        tmp = int(desiredamnt.replace('%', ''))

                    amnt = round_down(max_allowed * (tmp / 100))
                else:
                    if desiredamnt == 'a' or desiredamnt == 'all':
                        amnt = max_allowed
                    elif desiredamnt == 'h' or desiredamnt == 'half':
                        amnt = round_down(max_allowed / 2)
                    else:
                        clear()
                        print(SingleTable([["That isn't a valid amount!"]]).table)
                        continue

            # Sell the company
            if p.can_sell(amnt, company):
                p.sell(company, amnt, price)
                clear()
                print(SingleTable([[f"You sold {str(amnt)} shares of {company}!"]]).table)
                break
            else:
                clear()
                print(SingleTable([["You don't have that many shares!"]]).table)
                break

def location_menu(p):
    """Move the player to a new location."""

    while True:
        clear()
        loc_index = ['Bronx', 'Ghetto', 'Central Park', 'Manhattan', 'Coney Island', 'Brooklyn']
        location_table = [
            ['1) Bronx', '2) Ghetto', '3) Central Park'],
            ['4) Manhattan', '5) Coney Island', '6) Brooklyn']
        ]
        print(SingleTable(location_table, title="Where you gonna go? Current Location: " + p.current_area).table)
        try:
            loc = int(input("\n> ")) - 1
            if loc > 5 or loc < 0:
                clear()
                print(SingleTable([["Choose a number between 1 and 6!"]]).table)
            else:
                if loc_index[loc] == p.current_area:
                    clear()
                else:
                    loc += 1
                    if loc == 1:
                        p.current_area = "Bronx"
                    if loc == 2:
                        p.current_area = "Ghetto"
                    if loc == 3:
                        p.current_area = "Central Park"
                    if loc == 4:
                        p.current_area = "Manhattan"
                    if loc == 5:
                        p.current_area = "Coney Island"
                    if loc == 6:
                        p.current_area = "Brooklyn"
                    p.days += 1
                    break
        except ValueError:
            clear()
            print(SingleTable([["That isn't a number!"]]).table)

def difficulty_screen():
    """Select the game's difficulty level."""

    clear()
    while True:
        diff_table = [
            ["(E)asy", "(N)ormal", "(H)ard"],
        ]
        print(SingleTable(diff_table, "Difficulty Level").table)
        print("What level of difficulty would you like to play at?")
        diff = input("\n> ")
        if diff.lower() == "e":
            return 0
        elif diff.lower() == "n":
            return 1
        elif diff.lower() == "h":
            return 2
        else:
            clear()
            print(SingleTable([["Options Are: E, N, or H!!"]]).table)
            
    
def days_screen():
    """Ask how many in-game days to play."""

    clear()
    while True:
        day_table = [
            ["(A) 30 Days", "(B) 60 Days", "(C) 90 Days"]
        ]
        print(SingleTable(day_table, "Number of Days").table)
        print("How many days would you like to play?")
        test = input("\n> ")
        if test.lower() == 'a':
            return 30
        elif test.lower() == 'b':
            return 60
        elif test.lower() == 'c':
            return 90
        else:
            clear()
            print(SingleTable([["Options Are: A, B, or C."]]).table)


def main_screen(p):
    """Main game loop handling actions for the current day."""

    prices = CompanyPrices(p)
    if p.days == p.days_end:
        you_win(p)
    if not p.is_first_round:
        achoice = choice([lambda p: cops_chase(p), lambda p: buy_gun(p), lambda p: get_mugged(p), lambda p: find_companies(p), lambda p: upgrade_coat(p)])
        achoice(p)
    if prices.action != None and not p.is_first_round:
        print(SingleTable([[prices.action]]).table)
        input("Press ENTER to Continue")
    current_area = p.current_area
    if not p.is_first_round and current_area == "Bronx":
        clear()
        ask_loan_shark(p)
        ask_bank(p)
        ask_stash(p)
    while True:
        clear()
        inventory_table = lambda : [
            ['Inventory', 'Days Left: ' + str(p.days_end - p.days)],
            ['Company A: ' + str(round_down(p.company_a)), 'Company B: ' + str(round_down(p.company_b))],
            ['Company C: ' + str(round_down(p.company_c)), 'Company D: ' + str(round_down(p.company_d))],
            ['Company E: ' + str(round_down(p.company_e)), 'Company F: ' + str(round_down(p.company_f))],
        ]
        pricing_table = lambda : [
            ['Current Area: ' + p.current_area, 'Coat Space: ' + str(p.coat_space()) + " / " + str(p.max_trench)],
            ['Company A: ' + str(round_down(prices.company_a)), 'Company B: ' + str(round_down(prices.company_b))],
            ['Company C: ' + str(round_down(prices.company_c)), 'Company D: ' + str(round_down(prices.company_d))],
            ['Company E: ' + str(round_down(prices.company_e)), 'Company F: ' + str(round_down(prices.company_f))]
        ]
        money_table = lambda : [
            ['Debt: ' + str(int(round_down(p.shark.balance))) ,'Guns: ' + str(p.guns), 'Bank: ' + str(int(round_down(p.bank.balance))), 'Wallet: ' + str(int(round_down(p.money)))]
        ]
        print(SingleTable(inventory_table()).table)
        print(SingleTable(pricing_table(), title="Prices").table)
        print(SingleTable(money_table(), title="Money").table)
        print(SingleTable([["Are you going to (B)uy, (S)ell, or (J)et?"]]).table)
        ans = input("\n> ")
        anout = check_ans_bsj(ans)
        clear()
        if anout == 1:
            buy_menu(prices, inventory_table, pricing_table, money_table, p)
        elif anout == 2:
            sell_menu(prices, inventory_table, pricing_table, money_table, p)
        elif anout == 3:
            location_menu(p)
        else:
            clear()
            print(SingleTable([["That isn't an option. Choose B, S, or J"]]).table)
        if p.current_area != current_area:
            break
    p.is_first_round = False
    p.bank.interest()
    p.shark.interest()
    main_screen(p)

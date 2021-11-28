import money


def get_bet():
    while True:
        try:
            balance = money.readFile()
            bet = float(input('\nBet amount:\t'))
        except ValueError:
            print("Enter a valid number ")
            continue
        if bet < 5:
            print("Enter a positive number greater than or equals 5$")
        elif bet > balance:
            print("You don't have enough Balance")
            bet_to_balance(bet)
        elif bet >= 1000:
            print("Maximum bet is 1000$")

        else:
            return bet


def check_balance():
    while True:
        try:
            balance = money.readFile()
            if balance < 5:
                print("You don't have enough balance to start the game")
                choice = input("would you like to buy more chips . enter (yes) to buy")
                while choice.lower() == "yes":
                    AddBalance = float(input("How much money would you like to add:"))
                    balance += AddBalance
                    money.writeFile(balance)
                    choice = input("Do you want to add again (yes / no)")
                continue
        except ValueError:
            print("Enter a valid number ")
            continue
        else:
            return balance


def bet_to_balance(bet):
    start_balance = money.readFile()
    while True:
        try:
            if bet > start_balance:
                print("Your Bet is greater than your Balance")
                choice = input("would you like to buy more chips . enter (yes) to buy")
                while choice.lower() == "yes":
                    AddBalance = float(input("How much money would you like to add:"))
                    start_balance += AddBalance
                    money.writeFile(start_balance)
                    choice = input("Do you want to add again (yes / no)")

        except ValueError:
            print("Enter a valid number ")
            continue
        else:
            return start_balance

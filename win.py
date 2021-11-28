import money
import game


def bet_Win_or_lose(player, house, BetAmount):
    StartingBalance = money.readFile()
    if game.total_cards_value(house) < game.total_cards_value(player) <= 21 or game.total_cards_value(house) > 21:
        Earnings = float(BetAmount) * 1.5
        Earnings = round(Earnings, 2)
        print("Congratulations! You won the Game\n")
        print("you have earned:\t", Earnings)
        Balance = StartingBalance + Earnings
    elif game.total_cards_value(player) < game.total_cards_value(house) <= 21 or game.total_cards_value(player) > 21:
        print("Sorry! House won the Game\n")
        print("you have lost:\t", BetAmount)
        Balance = int(StartingBalance) - float(BetAmount)
        Balance = round(Balance, 2)
    else:
        print("It's a Tie!\n")
        Balance = StartingBalance
    print("Your Balance:\t\t", round(Balance, 2))
    money.writeFile(Balance)


def black_jack(house, player):
    if game.total_cards_value(player) == 21:
        print('\nBlack Jack! You are the winner!')
    elif game.total_cards_value(house) == 21:
        print("\nDealer got a black Jack . sorry you lost")

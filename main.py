import money
import win
import menu
import balance
import game


def main():
    house = []
    player = []
    menu.menu()
    start_balance = money.readFile()
    print(f'money: {start_balance} $')
    start_balance = balance.check_balance()

    if start_balance >= 5:
        play = str(input("\nDo you like to start the game (y/n)"))
        while play.lower() == "y":
            house.clear()
            player.clear()
            BetAmount = balance.get_bet()
            deck = game.shuffle_deck()
            game.game_start(deck, house, player)
            game.hit(deck, player)
            game.stand(deck, house, player)
            win.black_jack(house, player)
            game.display_total_points(house, player)
            win.bet_Win_or_lose(player, house, BetAmount)
            balance.check_balance()

            play = str(input("\nDo you like to play again (y/n)"))
        print("\nBye!")


if __name__ == "__main__":
    main()

import random
import win

suits = ['\u2660', '\u2661', '\u2662', '\u2663']
ranks = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]


# create a function to shuffle the deck
def shuffle_deck():
    try:
        deck = []
        for suit in suits:
            for rank in ranks:
                deck.append(rank + suit)
        random.shuffle(deck)
        if len(deck) <= 26:
            deck.clear()
            for suit in suits:
                for rank in ranks:
                    deck.append(rank + suit)
            random.shuffle(deck)
            return deck
        return deck
    except KeyError as e:
        print(10, "has this issue", e)
    except OSError as e:
        print(e)
    except Exception as e:
        print(type(e), e)


def deal_the_cards(deck, hand):
    card = deck.pop()
    hand.append(card)
    return card


def print_cards(hand):
    s = ""
    for card in hand:
        s = s + "\t _______ "
    print(s)

    s = ""
    for card in hand:
        if card[:2] == '10':
            s = s + "\t|{}     |".format(card[:2])
        else:
            s = s + "\t| {}     |".format(card[0][0])
    print(s)

    s = ""
    for card in hand:
        if card[:2] == '10':
            s = s + "\t|   {}   |".format(card[2:3])
        else:
            s = s + "\t|   {}   |".format(card[1])
    print(s)

    s = ""
    for card in hand:
        if card[:2] == '10':
            s = s + "\t|     {}|".format(card[:2])
        else:
            s = s + "\t|     {} |".format(card[0])
    print(s)

    s = ""
    for card in hand:
        s = s + "\t'-------'"
    print(s)

    print()


def un_shown_card(hand):
    # for i in range(len(hand)):
    s = ""
    s = s + "\t _______\t _______ "
    print(s)

    s = ""
    for card in hand:
        if card[:2] == '10':
            s = s + "\t|{}     |\t| ??    |".format(card[:2])
        else:
            s = s + "\t| {}     |\t| ??    |".format(card[0][0])
    print(s)

    s = ""
    for card in hand:
        if card[:2] == '10':
            s = s + "\t|   {}   |\t|   ??  |".format(card[2:3])
        else:
            s = s + "\t|   {}   |\t|   ??  |".format(card[1])
    print(s)

    s = ""
    for card in hand:
        if card[:2] == '10':
            s = s + "\t|     {}|\t|     ??|".format(card[:2])
        else:
            s = s + "\t|     {} |\t|     ??|".format(card[0])
    print(s)

    s = ""
    s = s + "\t'-------'\t'-------'"
    print(s)
    print()


def display_player_cards(player):
    print("Your Cards:")
    print_cards(player)


def display_dealer_cards(house):
    print("Dealer Cards:")
    print_cards(house)


def total_cards_value(hand):
    try:
        cards_values = {"A": 11, "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7,
                        "8": 8, "9": 9, "1": 10, "J": 10, "Q": 10, "K": 10}
        result = 0
        aces_count = 0
        for card in hand:
            result += cards_values[card[0]]
            if card[0] == 'A':
                aces_count += 1

                while result > 21 and aces_count > 0:
                    result -= 10
                    aces_count -= 1
        return result
    except KeyError as e:
        print(e)
    except OSError as e:
        print(e)
    except Exception as e:
        print(type(e), e)


def display_total_points(house, player):
    display_dealer_cards(house)
    print('YOUR POINTS:\t', total_cards_value(player))
    print('DEALER POINTS:\t', total_cards_value(house), "\n")


def hit(deck, player):
    if total_cards_value(player) < 21:
        choice = input('Hit or Stand? (hit/stand):')
        print()
        while choice.lower() == "hit":
            deal_the_cards(deck, player)
            display_player_cards(player)
            if total_cards_value(player) >= 21:
                return
            choice = input('Hit or Stand? (hit/stand):')
            print()


def stand(deck, house, player):
    while total_cards_value(house) < 17 and total_cards_value(player) < 21:
        deal_the_cards(deck, house)


def game_start(deck, house, player):
    deal_the_cards(deck, house)
    for i in range(2):
        deal_the_cards(deck, player)
    if total_cards_value(player) < 21 and total_cards_value(house) < 21:
        un_shown_card(house)
        deal_the_cards(deck, house)
        display_player_cards(player)
    else:
        display_dealer_cards(house)
        deal_the_cards(deck, house)
        display_player_cards(player)
        win.black_jack(house, player)

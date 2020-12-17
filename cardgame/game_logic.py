from random import randint
import json
import os


class GameOverException(Exception):

    def __init__(self, message):
        super().__init__(message)


def create_deck():
    deck = []

    for colour in "red black yellow".split():

        for number in range(1, 11):
            deck.append([colour, number])

    return deck


def shuffle_deck(deck):
    for index in range(100):
        for index in range(len(deck)):
            random_num = randint(0, len(deck) - 1)
            deck[index], deck[random_num] = deck[random_num], deck[index]

    return deck


def remove_cards_from_deck(deck, player_1_card, player_2_card, player_1_cards, player_2_cards):
    for card in [player_1_card, player_2_card]:
        deck.remove(card)

    player_1_cards.append(player_1_card)
    player_2_cards.append(player_2_card)

    return deck, player_1_cards, player_2_cards


def store_data(data):
    with open("game_data.json", "w+") as f:
        json.dump(data, f)


def player_1_wins_round(cards):
    return "1"


def player_2_wins_round(cards):
    return "2"


def colour_draw(cards):
    numbers = (cards[0][1], cards[1][1])

    if cards[0] == cards[1]:
        return "It's a draw!"

    return str(numbers.index(max(numbers)) + 1)


def draw_cards(deck):
    return (deck[0], deck[1])


def determine_winner(cards):
    colours = (cards[0][0], cards[1][0])
    colour_hierarchy = {('red', 'black'): player_1_wins_round, ('red', 'yellow'): player_2_wins_round,
                        ('red', 'red'): colour_draw, ('yellow', 'red'): player_1_wins_round,
                        ('yellow', 'black'): player_2_wins_round, ('yellow', 'yellow'): colour_draw,
                        ('black', 'red'): player_2_wins_round, ('black', 'black'): colour_draw,
                        ('black', 'yellow'): player_1_wins_round}

    winner = colour_hierarchy[colours](cards)

    return winner


def stringify_cards(p1_cards, p2_cards):
    p1_cards = [str(index) for index in p1_cards]
    p2_cards = [str(index) for index in p2_cards]

    return [p1_cards, p2_cards]


def load_data():
    print(os.getcwd())

    with open("game_data.json", "r+") as f:
        data = json.load(f)

    return data


def set_game():
    data = {
        "cycle": 0, "deck": shuffle_deck(create_deck()), "player_1_cards": [], "player_2_cards": [],
        "player_1_score": 0, "player_2_score": 0}

    store_data(data)


def set_round():
    data = load_data()

    return data


def is_game_over(deck):
    if len(deck) < 1:
        raise GameOverException("Game Finished") from None


def play_round(data):
    cycle, deck, player_1_cards, player_2_cards, player_1_score, player_2_score = list(data.values())

    try:
        is_game_over(deck)
    except GameOverException:

        if player_1_score > player_2_score:
            game_winner = "Player 1"

        else:
            game_winner = "Player 2"

        return [{"cycle": 0, "winner": 0, "player_1_score": player_1_score, "player_2_score": player_2_score,
                 "player_1_card": 0, "player_2_card": 0, "game_winner": game_winner}, True]

    cycle += 1

    player_1_card, player_2_card = draw_cards(deck)

    updated_deck, player_1_cards, player_2_cards = remove_cards_from_deck(deck, player_1_card, player_2_card,
                                                                          player_1_cards, player_2_cards)

    winner = determine_winner((player_1_card, player_2_card))

    player_1_card, player_2_card = stringify_cards(player_1_card, player_2_card)

    if winner == "1":
        player_1_score += 1

    elif winner == "2":
        player_2_score += 1

    data = {
        "cycle": cycle, "deck": deck, "player_1_cards": player_1_cards, "player_2_cards": player_2_cards,
        "player_1_score": player_1_score, "player_2_score": player_2_score}

    store_data(data)

    show_data = {"cycle": cycle, "winner": f"Player {winner}", "player_1_score": player_1_score,
                 "player_2_score": player_2_score, "player_1_card": player_1_card, "player_2_card": player_2_card,
                 "game_winner": ""}

    return [show_data, False]


def play():
    data = set_round()

    return play_round(data)


if __name__ == "__main__":
    play()

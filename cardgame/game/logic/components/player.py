from cardgame.game.logic.components.adts import Stack


class Player:

    def __init__(self, name, deck):
        self.name = name
        self.cards = Stack(base_stack=[])

    def __str__(self):
        return self.name

    def draw_card(self, deck):
        self.active_card = deck.take_card()

    def update_state(self, state, cards):
        if state == 1:
            self.winner(cards)

    def winner(self, cards):
        for index in range(2):
            self.cards.push(cards[index])
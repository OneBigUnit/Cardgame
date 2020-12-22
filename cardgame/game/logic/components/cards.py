from cardgame.game.logic.components.adts import Stack
from cardgame.game.logic.components.exceptions import DeckDepleted


class Cards:

    def __init__(self):
        cards = Cards.generate_cards()
        self.cards = cards.stack_shuffle()

    @staticmethod
    def generate_cards(colours=["red", "black", "yellow"], numbers=[num for num in range(1, 11)]):

        cards = Stack()

        for colour in colours:
            for number in numbers:
                cards.push([colour, number])

        return cards

    def take_card(self):
        try:
            return self.cards.stack_pop()
        except IndexError:
            raise DeckDepleted() from None

    def rank(self, cards):
        colour_hierarchy = {('red', 'black'): (1, 2), ('red', 'yellow'): (2, 1), ('red', 'red'): (1, 1),
                            ('yellow', 'red'): (1, 2), ('yellow', 'black'): (2, 1), ('yellow', 'yellow'): (1, 1),
                            ('black', 'red'): (2, 1), ('black', 'black'): (1, 1), ('black', 'yellow'): (1, 2)}
        colours = (cards[0][0], cards[1][0])
        ranking = colour_hierarchy[colours]
        if ranking == (1, 1):
            ranking = self.rank_by_nums(cards)
        return ranking

    def rank_by_nums(self, cards):
        nums = [cards[0][1], cards[1][1]]

        if nums[0] > nums[1]:
            return (1, 2)
        elif nums[0] < nums[1]:
            return (2, 1)
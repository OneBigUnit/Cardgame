from flask_login import current_user

from cardgame import db
from cardgame.game.logic.components.adts import Stack


class Player:

    def __init__(self, name):
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

    def update_user_info(self, game_winner):
        if str(self) == "Player 1":
            current_user.p1_rounds_won += self.cards.size() // 2
            current_user.p1_rounds_lost += (15 - self.cards.size() // 2)

            if str(self) == str(game_winner):
                current_user.p1_wins += 1
            else:
                current_user.p1_losses += 1
            if self.cards.size() // 2 > current_user.p1_record_points:
                current_user.p1_record_points = self.cards.size() // 2

        else:
            current_user.p2_rounds_won += self.cards.size() // 2
            current_user.p2_rounds_lost += (15 - self.cards.size() // 2)

            if str(self) == str(game_winner):
                current_user.p2_wins += 1
            else:
                current_user.p2_losses += 1
            if self.cards.size() // 2 > current_user.p2_record_points:
                current_user.p2_record_points = self.cards.size() // 2

        db.session.commit()

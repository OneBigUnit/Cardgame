import json

from cardgame.game.logic.components.adts import Queue
from cardgame.game.logic.components.cards import Cards
from cardgame.game.logic.components.context_managers import OpenMyPath
from cardgame.game.logic.components.exceptions import DeckDepleted
from cardgame.game.logic.components.player import Player


class Game:

    def __new__(self):
        self.round_counter = 0
        self.deck = Cards()
        self.players = self.create_players(self)

        return self.round_manager(self)

    def round_manager(self):
        while True:
            try:
                yield self.play_round(self)
            except DeckDepleted:
                break

        self.determine_game_winner(self)

        for player in self.players:
            player.update_user_info(self.game_winner)

        yield self.display_game_winner(self)

    def play_round(self):

        self.increment_round_counter(self)

        self.draw_cards(self)

        self.determine_round_winner(self)

        self.update_players(self)

        return self.display_round_information(self)

    def draw_cards(self):
        for player in self.players:
            player.draw_card(self.deck)

        self.current_cards = [self.players[0].active_card, self.players[1].active_card]

    def determine_round_winner(self):
        self.ranking = Cards.rank(self.deck, self.current_cards)
        self.round_result = Game.decode_ranking(self.players, self.ranking)

    def create_players(self, number=2):
        players = []
        for i in range(1, number + 1):
            players.append(Player(f"Player {i}"))
        return players

    def increment_round_counter(self):
        self.round_counter += 1

    def update_players(self):
        for player, state in zip(self.players, self.ranking):
            player.update_state(state, self.current_cards)

    def display_round_information(self):
        return [True, self.round_counter, str(self.round_result), str(self.players[0]), str(self.players[1]),
                " ".join([str(part) for part in self.current_cards[0]]).title(),
                " ".join([str(part) for part in self.current_cards[1]]).title(),
                self.players[0].cards.size() // 2, self.players[1].cards.size() // 2]

    def determine_game_winner(self):
        if self.players[0].cards.size() > self.players[1].cards.size():
            self.game_winner = self.players[0]
        elif self.players[0].cards.size() < self.players[1].cards.size():
            self.game_winner = self.players[1]

    def display_game_winner(self):
        return [False, str(self.game_winner), str(self.players[0]), str(self.players[1]),
                self.players[0].cards.size() // 2, self.players[1].cards.size() // 2]

    @staticmethod
    def decode_ranking(players, ranking):
        if ranking[1] > ranking[0]:
            return players[0]
        elif ranking[0] > ranking[1]:
            return players[1]

    @staticmethod
    def store_game(results):
        with OpenMyPath("cardgame/game/logic/components"):
            with open("game.json", "w+") as f:
                json.dump({"game": results.reveal()}, f)

    @staticmethod
    def get_game():
        with OpenMyPath("cardgame/game/logic/components"):
            with open("game.json", "r+") as f:
                return Queue(start=json.load(f)["game"])

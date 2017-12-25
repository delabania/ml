from tic_tac_toe import State
from collections import defaultdict
from itertools import izip
from copy import deepcopy
import random

class Player(object):
    def __init__(self, symbol):
        self.symbol = symbol
        # self.policy = {state: {move : number_of_not_loses}}
        self.policy = defaultdict(lambda: defaultdict(int))
        self.game_history = []

    def make_move(self, board):
        # self.policy[board][move]
        possible_moves = board.possible_moves()
        choice = random.choice(list(possible_moves))
        self.game_history.append((deepcopy(board), choice))
        return choice

    def clear_game_history():
        self.game_history = []

    def analyze_game_history(game_result):
        if game_result in ['draw', 'win']:
            pass
        else: # 'loose'
            pass

def play(players):
    board = State()
    step = 0
    while not board.winner() and not board.game_over():
        pos = players[step % 2].make_move(board)
        board.insert(pos, 'o' if step % 2 == 0 else 'x')
        step += 1

    winner = board.winner()
    print board
    for player in players:
        player.analyze_game_history()
        player.clear_game_history()


def learn(reps):
    players = Player('o'), Player('x')
    for rep in range(reps):
        play(players)


learn(1)
from collections import defaultdict
from copy import deepcopy
import gzip
import cPickle as pickle
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
            for state, choice in self.game_history:
                # add perspective of 'x' or 'o' player
                policy[state][choice] += 1
        else:
            # maybe do: policy[state][choice] -= 1
            pass

    def save_policy(self, filename):
        with gzip.open(filename, 'wb') as file_:
            pickle.dump(self.policy, file_)
        
    def load_policy():
        pass

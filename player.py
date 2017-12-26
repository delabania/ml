from collections import defaultdict
from copy import deepcopy
import gzip
import cPickle as pickle
import random
import operator

class Player(object):
    def __init__(self, symbol):
        self.symbol = symbol
        # self.policy = {state: {move : number_of_not_loses}}
        self.game_history = []
        self.reset_policy()

    def reset_policy(self):
        self.policy = defaultdict(lambda: defaultdict(int))

    def make_move(self, board, strategy):
        if strategy == 'random':
            choice = self.make_random_move(board)
        elif strategy == 'best':
            choice = self.make_best_move(board)
        return choice

    def make_random_move(self, board):
        possible_moves = board.possible_moves()
        choice = random.choice(list(possible_moves))
        self.game_history.append((deepcopy(board), choice))
        return choice

    def make_best_move(self, board):
        possible_moves = board.possible_moves()
        possible_moves_rate = {
            choice : self.policy[board][choice] for choice in possible_moves
        }
        best_move = max(possible_moves_rate.iteritems(), key=operator.itemgetter(1)[0])
        return best_move

    def clear_game_history(self):
        self.game_history = []

    def analyze_game_history(self, game_result):
        if game_result in ['draw', 'win']:
            for state, choice in self.game_history:
                self.policy[state][choice] += 1
        else:
            # maybe do: policy[state][choice] -= 1
            pass

    def save_policy(self, filename):
        with gzip.open(filename, 'wb') as file_:
            policy = {
                state : dict(state_decisions)
                for state, state_decisions in self.policy.iteritems()
            }
            pickle.dump(policy, file_)

        
    def load_policy(self, filename):
        with gzip.open(filename, 'r') as file_:
            policy = pickle.load(file_)
            #???? update policy, maybe not overwrite
            self.reset_policy()
            for state, decisions in policy.iteritems():
                for choice, value in decisions.iteritems():
                    self.policy[state][choice] = value

from tic_tac_toe import State
from player import Player

def play(players):
    board = State()
    step = 0
    while not board.winner() and not board.game_over():
        pos = players[step % 2].make_move(board, 'random')
        board.insert(pos, 'o' if step % 2 == 0 else 'x')
        step += 1

    winner = board.winner()
    for player in players:
        if not winner:
            game_result = 'draw'
        elif player.symbol == winner:
            game_result = 'win'
        else:
            game_result = 'loose'
        player.analyze_game_history(game_result)
        player.clear_game_history()


def learn(reps):
    players = Player('o'), Player('x')

    for rep in range(reps):
        play(players)

    for player in players:
        filename = '/tmp/policy_{}.gz'.format(player.symbol)
        #player.save_policy(filename)
        #player.load_policy(filename)

if __name__ == '__main__':
    learn(10**4)
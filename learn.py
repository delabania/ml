from tic_tac_toe import State

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
        #pass 'win', 'draw' to analyze_game_history
        player.analyze_game_history()
        player.clear_game_history()


def learn(reps):
    players = Player('o'), Player('x')

    for rep in range(reps):
        play(players)

    for player in players:
        filename = 'policy_{}.gz'.format(player.symbol)
        player.save_policy(filename)


learn(1)
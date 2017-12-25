class State(object):
    VERTICAL_LINE = [(0, 0), (0, 1), (0, 2)]
    HORIZONTAL_LINE = [(0, 0), (1, 0), (2, 0)]
    CROSS_LINE = [(0,0), (1,1), (2,2)]

    @staticmethod
    def get_winning_lines():
        for i in range(3):
            yield map(lambda pos: (pos[0] + i, pos[1]), State.VERTICAL_LINE) 
        for i in range(3):
            yield map(lambda pos: (pos[0], pos[1] + i), State.HORIZONTAL_LINE)
        yield State.CROSS_LINE
        yield list(reversed(State.CROSS_LINE))

    def __init__(self):
        #board = 'xox--x--o'
        self.board = [['-' for _ in range(3)] for _ in range(3)]

    def __str__(self):
        return '\n'.join(' '.join(row) for row in self.board)

    def __eq__(self, other):
        return self.board == other.board

    def __ne__(self, other):
        return self.board != other.board

    def insert(self, pos, symbol):
        assert symbol in ['x', 'o']
        x, y = pos
        assert 0 <= x < 3 and 0 <= y < 3
        assert self.board[x][y] == '-'
        self.board[x][y] = symbol

    def possible_moves(self):
        for row_num, row in enumerate(self.board):
            for column_num, symbol in enumerate(row):
                if symbol == '-':
                    yield row_num, column_num
    
    def game_over(self):
        return len(list(self.possible_moves())) == 0

    def winner(self):
        for line in State.get_winning_lines():
            symbols_in_line = set(map(lambda pos: self.board[pos[0]][pos[1]], line))
            if '-' in symbols_in_line or len(symbols_in_line) > 1:
                continue
            # only one symbol, different from empty '-', in whole line
            return tuple(symbols_in_line)[0] 
        return None



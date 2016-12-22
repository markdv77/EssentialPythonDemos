class Game:
    def __init__(self):
        self.empty = 0
        self.board = self.create_empty_board()

        self.x = 1
        self.o = -1
        self.current_player = self.x

    def create_empty_board(self):
        e = self.empty
        return [
            [e, e, e],
            [e, e, e],
            [e, e, e]
        ]

    def switch_players(self):
        self.current_player *= -1

    def play_cell(self, row, cell):
        self.board[row][cell] = self.current_player

    def get_cell(self, row, cell):
        return self.board[row][cell]

    @property
    def has_won(self):
        return self.find_winner() is not None

    def find_winner(self):
        b = self.board
        possible_wins = [
            # rows
            [b[0][0], b[0][1], b[0][2]],
            [b[1][0], b[1][1], b[1][2]],
            [b[2][0], b[2][1], b[2][2]],

            # cols
            [b[0][0], b[1][0], b[2][0]],
            [b[0][1], b[1][1], b[2][1]],
            [b[0][2], b[1][2], b[2][2]],

            # diags
            [b[0][0], b[1][1], b[2][2]],
            [b[0][2], b[1][1], b[2][0]],
        ]

        for w in possible_wins:
            s = sum(w)
            if s == 3:
                return self.x
            #elif s == -2:  # explicit error
            elif s == -3:
                return self.o

        return None

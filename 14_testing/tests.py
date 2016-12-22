import os
import unittest

from game import Game


class GameTests(unittest.TestCase):
    def test_can_create_empty_board(self):
        # Arrange
        g = Game()

        # Act

        # Assert
        for row in g.board:
            for cell in row:
                self.assertEqual(g.empty, cell)

    def test_players_can_swap_between_current_one(self):
        # Arrange
        g = Game()

        # Act
        first = g.current_player
        g.switch_players()
        second = g.current_player

        # Assert
        self.assertNotEqual(first, second)

    #def test_game_can_be_won(self):
    #    # Arrange
    #    g = Game()

    #    # Act
    #    g.play_cell(0, 0)
    #    g.switch_players()
    #    g.play_cell(0,1)
    #    g.switch_players()
    #    g.play_cell(1,1)
    #    g.switch_players()
    #    g.play_cell(0,2)
    #    g.switch_players()
    #    g.play_cell(2,2)
    #    g.switch_players()

        # Assert
        #self.assertTrue(g.has_won)

    @unittest.skip('We dont want to run this one right now')
    def test_game_can_be_won(self):
        # Arrange
        moves_text = self.get_text_from_file("moves.csv")
        actual_moves = moves_text[1:]
        # example line:
        # 0,0|2,0|0,1|1,1|2,2|0,2|-1

        for line in actual_moves:
            g = Game()
            #print("Playing line: " + line)
            entries = line.split('|')
            winner = int(entries[-1])
            moves = entries[0:-1]
            for m in moves:
                if m and len(m.strip()) > 0:
                    parts = m.split(',')
                    #print("Playing " + m)
                    r = int(parts[0])
                    c = int(parts[1])
                    g.play_cell(r, c)
                g.switch_players()
            if winner:
                self.assertEqual(winner, g.find_winner())
            else:
                self.assertFalse(g.has_won)


    def get_text_from_file(self, filename):
        folder = os.path.dirname(__file__)
        file = os.path.join(folder, 'moves', filename)
        with open(file, 'r') as fin:
            return fin.readlines()

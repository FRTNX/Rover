import unittest
from rover import move_forward, shift

class TestRoverMethods(unittest.TestCase):

    def test_move_east(self):
        self.assertEqual(move_forward((1, 2), 'E', (8, 10)), (2, 2))

    def test_move_west(self):
        self.assertEqual(move_forward((1, 2), 'W', (8, 10)), (0, 2)) 

    def test_move_north(self):
        self.assertEqual(move_forward((1, 2), 'N', (8, 10)), (1, 3))

    def test_move_south(self):
        self.assertEqual(move_forward((1, 2), 'S', (8, 10)), (1, 1))

    def test_move_out_of_bounds_x(self):
        self.assertEqual(move_forward((8, 2), 'E', (8, 10)), 'Out of bounds')
    
    def test_move_out_of_bounds_y(self):
        self.assertEqual(move_forward((3, 10), 'N', (8, 10)), 'Out of bounds')

    def test_move_out_of_bounds_x2(self):
        self.assertEqual(move_forward((0, 5), 'W', (8, 10)), 'Out of bounds')

    def test_move_out_of_bounds_y2(self):
        self.assertEqual(move_forward((4, 0), 'S', (8, 10)), 'Out of bounds')

    def test_shift_NL(self):
        self.assertEqual(shift("NL"), "W")

    def test_shift_NR(self):
        self.assertEqual(shift("NR"), "E")

    def test_shift_SL(self):
        self.assertEqual(shift("SL"), "E")

    def test_shift_SR(self):
        self.assertEqual(shift("SR"), "W")

    def test_shift_EL(self):
        self.assertEqual(shift("EL"), "N")

    def test_shift_ER(self):
        self.assertEqual(shift("ER"), "S")

    def test_shift_WL(self):
        self.assertEqual(shift("WL"), "S")

    def test_shift_WR(self):
        self.assertEqual(shift("WR"), "N")

if __name__ == '__main__':
    unittest.main()
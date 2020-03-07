import unittest
from unittest.mock import patch

from io import StringIO

from draw_box import draw_box, get_code
from box_constants import *

class TestBoxDraw(unittest.TestCase):

    @patch('sys.stdout', new_callable=StringIO)
    def test_box_correct(self, mock_out):
        expected_out = (
            "┌-┐\n"
            "| |\n"
            "| |\n"
            "| |\n"
            "└-┘\n"
        )
        draw_box(3, 5)
        self.assertEqual(mock_out.getvalue(), expected_out)

    def test_rejects_nonints(self):
        self.assertRaises(TypeError, draw_box, w="non-int", h="non-int")
        self.assertRaises(TypeError, draw_box, w=2, h="non-int")
        self.assertRaises(TypeError, draw_box, w="non-int", h=2)

    def test_min_box_size(self): 
        self.assertRaises(ValueError, draw_box, w=1, h=1)
        self.assertRaises(ValueError, draw_box, w=1, h=2)
        self.assertRaises(ValueError, draw_box, w=2, h=1)
    
    def test_corner_codes(self):
        width = 5
        height = 5

        self.assertEqual(TOP_LEFT, get_code(0, 0, height, width))
        self.assertEqual(TOP_RIGHT, get_code(0, width-1, height, width))
        self.assertEqual(BOTTOM_LEFT, get_code(height-1, 0, height, width))
        self.assertEqual(BOTTOM_RIGHT, get_code(height-1, width-1, height, width))
    
    def test_horizontal_edge_code(self):
        width = 5
        height = 5

        self.assertEqual(H_EDGE, get_code(0, 1, height, width))
        self.assertEqual(H_EDGE, get_code(height-1, 1, height, width))

    def test_vertical_edge_code(self): 
        width = 5
        height = 5

        self.assertEqual(V_EDGE, get_code(1, 0, height, width))
        self.assertEqual(V_EDGE, get_code(1, width-1, height, width))

    def test_inner_space_code(self):
        width = 5
        height = 5
        
        self.assertEqual(SPACE, get_code(3, 3, height, width))

    
if __name__ == "__main__":
    unittest.main()
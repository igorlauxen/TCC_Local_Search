import unittest

from TCCSA import getPlaceToSwap, swap

class FieldTest(unittest.TestCase):

    def test_placeToSwap(self):
        array = [0,1,2,3,4]
        self.assertTrue(getPlaceToSwap(array, 5, True) == 0, 'Review the entry. Should be 0 for Right')
        self.assertTrue(getPlaceToSwap(array, 0, False) == 4, 'Review the entry. Should be 5 for Left')
        self.assertTrue(getPlaceToSwap(array, 4, True) == 4, 'Review the entry. Should be 5 for Right')

    def test_swapItself(self):
        array = [0,1,2,3,4]
        self.assertTrue(swap(array, 5, True) == [4,1,2,3,0], 'Review the entry. Should be [4,1,2,3,0] for Right')
        self.assertTrue(swap(array, 3, True) == [0, 1, 2, 4, 3], 'Review the entry. Should be [0, 1, 2, 4, 3] for Right')
        self.assertTrue(swap(array, 0, False) == [4, 1, 2, 3, 0], 'Review the entry. Should be [4,1,2,3,0] for Left')

if __name__ == "__main__":
    unittest.main()

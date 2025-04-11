import unittest
from bots.pycamp_2025.bad_bot import my_structure

class Terrain:
    def __init__(self, owner, structure):
        self.owner = owner
        self.structure = structure

class TestMyStructure(unittest.TestCase):
    def setUp(self):
        self.world = {
            "castle_position1": Terrain("mine", "castle"),
            "castle_position2": Terrain("mine", "castle"),
            "farm_position": Terrain("mine", "farm"),
            "fort_position": Terrain("mine", "fort"),
        }

    def test_my_castles(self):
        """
        Expected Behavior: return a list of positions that have the structure type "castle"
        Assertion: Checks that the returned list is ["castle_position1", "castle_position2"]
        Result: PASSED
        """
        result = my_structure(self.world, "castle")
        expected = ["castle_position1", "castle_position2"]
        self.assertEqual(result, expected)

    def test_my_farms(self):
        """
        Expected Behavior: return a list of positions that have the structure type "farm"
        Assertion: Checks that the returned list is ["farm_position""]
        Result: PASSED
        """
        result = my_structure(self.world, "farm")
        expected = ["farm_position"]
        self.assertEqual(result, expected)

    def test_my_forts(self):
        """
        Expected Behavior: return a list of positions that have the structure type "fort"
        Assertion: Checks that the returned list is ["fort_position"]
        Result: PASSED
        """
        result = my_structure(self.world, "fort")
        expected = ["fort_position"]
        self.assertEqual(result, expected)

if __name__ == '__main__':
    unittest.main()

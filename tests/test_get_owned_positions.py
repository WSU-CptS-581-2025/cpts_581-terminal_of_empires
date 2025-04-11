import unittest
from src.main.bots.pycamp_2025.angry_farmer import get_owned_positions

class Terrain:
    def __init__(self, owner, structure):
        self.owner = owner
        self.structure = structure

class TestGetOwnedPositions(unittest.TestCase):
    def setUp(self):
        self.world = {
            "castle_position": Terrain("mine", "castle"),
            "farm_position": Terrain("mine", "farm"),
            "farm_position2": Terrain("mine", None),
            "fort_position": Terrain("mine", "fort"),
            "land_position": Terrain("mine", "land"),
        }

    def test_filter_by_owner(self):
        """
        Expected Behavior: return a list of positions ONLY by the owner name, in this case "mine"
        Assertion: Checks that the returned list is ["castle_position", "farm_position", "fort_position", "land_position"] as these are the only positions where the owner is "mine"
        Result: PASSED
        """
        result = get_owned_positions(self.world, "mine")
        expected = ["castle_position", "farm_position", "farm_position2","fort_position", "land_position"]
        self.assertEqual(result, expected)

    def test_filter_by_owner_structure(self):
        """
        Expected Behavior: return a list of positions by the owner name, in this case "mine" AND the structure type
        Assertion: Checks that the returned list is ["farm_position"] as it matches the criteria of the owner name and structure type
        Result: PASSED
        """
        result = get_owned_positions(self.world, "mine", "farm")
        expected = ["farm_position"]
        self.assertEqual(result, expected)

    def test_no_matching_owner(self):
        """
        Expected Behavior: return an empty list since there is no positions with a specficed owner "enemy"
        Assertion: Checks that the list returned is empty
        Result: PASSED
        """
        result = get_owned_positions(self.world, "enemy")
        expected = []
        self.assertEqual(result, expected)

if __name__ == "__main__":
    unittest.main()

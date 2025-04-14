import unittest

from src.GameLogic.game_manager import Terrain, Position, ToE, Player
from src.helper_functions import world_actions


class getAdjacentTilesTest(unittest.TestCase):
    def setUp(self):
        self.world = {
            Position(1,1): Terrain("land","None"),
            Position(5,5): Terrain("sofi", "castle"),
            Position(4,5): Terrain("land","None"),
            Position(5, 4): Terrain("land","None"),
            Position(6, 5): Terrain("land","None"),
            Position(5, 6): Terrain("land","None"),
        }


    def test_DetectAdjacentTiles(self):

        world = {
            Position(1, 1): Terrain("land", "None"),
            Position(5, 5): Terrain("castle", "sofi"),
            Position(4, 5): Terrain("land", "None"),
            Position(5, 4): Terrain("land", "None"),
            Position(6, 5): Terrain("land", "None"),
            Position(5, 6): Terrain("land", "None"),
        }
        expected = {
            Position(5, 5): Terrain("castle", "mine"),
            Position(4, 5): Terrain("land", "None"),
            Position(6, 5): Terrain("land", "None"),
            Position(5, 4): Terrain("land", "None"),
            Position(5, 6): Terrain("land", "None"),
        }
        result = world_actions.copy_world_for_player(world, player=Player("sofi", "pacifist", resources=0, debug=self.debug))
        self.assertEqual(result, expected)


if __name__ == "__main__":
    unittest.main()
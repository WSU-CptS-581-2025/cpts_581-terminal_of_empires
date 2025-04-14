import random

from src.helper_functions.bot_actions import is_adjacent

class BotLogic:
    """
    Bot logic for the Aggressive bot.
    """
    def turn(self, map_size, my_resources, world):
        """
        Aggressive bot always tries to conquer terrain, and never builds any structures.
        It prioritizes conquering enemy terrain over neutral land.
        It tries to keep its resources high, so it can deal with any kind of enemy defenses.
        """
        # try to find enemy terrain that we can conquer

        conquerable_enemy_terrain = [
            position
            for position, terrain in world.items()
            if terrain.owner not in ("mine", None)
        ]

        if conquerable_enemy_terrain:
            # keep the resources high so we can conquer anything we want
            if my_resources < 100:
                return "harvest", None
            else:
                return "conquer", random.choice(conquerable_enemy_terrain)

        # if no enemy terrain, then try to conquer neutral terrain
        conquerable_neutral_terrain = [
            position
            for position, terrain in world.items()
            if terrain.owner is None
        ]

        if conquerable_neutral_terrain:
            if my_resources < 1:
                return "harvest", None
            else:
                return "conquer", random.choice(conquerable_neutral_terrain)

        # finally, if nothing could be done, harvest
        return "harvest", None

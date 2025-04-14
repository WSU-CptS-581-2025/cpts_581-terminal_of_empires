from collections import namedtuple

Position = namedtuple("Position", "x y")
Terrain = namedtuple("Terrain", "structure owner")

def adjacent_positions(world, position):
    """
    Return the valid positions adjacent to the given position, considering the map size.
    """
    x, y = position
    candidates = [
        Position(x - 1, y),
        Position(x + 1, y),
        Position(x, y - 1),
        Position(x, y + 1),
    ]
    return [
        candidate
        for candidate in candidates
        if candidate in world
    ]

def copy_world_for_player(world, player):
    """
    Return a copy of the world to pass to the player (for safety), also modifying the world so
    their terrain positions have "mine" as owner.
    """

    visible_world = {
    }
    for position, terrain in world.items():
        if terrain.owner == player.name:
            visible_world[position] = Terrain(
                terrain.structure,
                "mine"
            )
            for adjacentTile in adjacent_positions(world, position):
                if adjacentTile in visible_world:
                    continue
                adjacent_tile_terrain = world[adjacentTile]
                visible_world[adjacentTile] = Terrain(
                    adjacent_tile_terrain.structure,
                    terrain.owner if adjacent_tile_terrain.owner == player.name else adjacent_tile_terrain.owner
                )
    return visible_world
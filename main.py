import utils
import os
import config as cfg
from pprint import pprint
from maze import Maze


def build_maze():
    map = utils.load_json(os.path.join(cfg.MAPS, map_filename))
    rooms = map['rooms']
    maze = Maze()
    for room in rooms:
        maze.add_room(id=room['id'],
                      name=room['name'],
                      objects=room['objects'])

    for room in rooms:

        if 'north' in room:
            maze.add_link(id1=room['id'], id2=room['north'])
        if 'east' in room:
            maze.add_link(id1=room['id'], id2=room['east'])
        if 'south' in room:
            maze.add_link(id1=room['id'], id2=room['south'])
        if 'west' in room:
            maze.add_link(id1=room['id'], id2=room['west'])
    return maze


if __name__ == '__main__':
    test = utils.load_json(cfg.TEST)
    map_filename = test['map']

    maze = build_maze()

    start = test['start room ID']
    objects = test['objects']

    moves = maze.collect_objects(source=start, objects=objects, verbose=False)
    number_of_moves = len(moves) - 1

    utils.print_output(moves)
    utils.save_json(
        data={
            "test": cfg.TEST_NAME,
            "number of moves": number_of_moves,
            "moves": moves,
        },
        filepath=cfg.RESULT)

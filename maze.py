import utils
import os
import config as cfg
from pprint import pprint
import networkx as nx


class Maze:
    class Room:
        def __init__(self, id, name, objects=[]):
            self._set_id(id=id)
            self._set_name(name=name)
            self._set_objects(objects=objects)

        def _set_id(self, id):
            self._id = id

        def _set_name(self, name):
            self._name = name

        def _set_objects(self, objects):
            self._objects = objects

        def get_id(self):
            return self._id

        def get_name(self):
            return self._name

        def get_objects(self):
            return self._objects

        def __hash__(self):
            return hash(self.get_id())

        def __str__(self):
            return str(
                f"'id': {self.get_id()},\n"
                f"'name': {self.get_name()},\n"
                f"'objects': {self.get_objects()}"
            )

    def __init__(self):
        self._rooms = {}
        self._graph = nx.Graph()

    def add_room(self, id, name, objects=[]):
        self._rooms[id] = Maze.Room(id=id, name=name, objects=objects)
        self._graph.add_node(id)

    def add_link(self, id1, id2):
        self._graph.add_edge(id1, id2)

    def find_objects(self, objects):
        objects_locations = {}
        for node in self._graph.nodes():
            room = self._rooms[node]
            room_objects = room.get_objects()
            objects_found = utils.list_intersection(objects, room_objects)
            if len(objects_found) > 0:
                if node not in objects_locations:
                    objects_locations[node] = []
                for object_found in objects_found:
                    objects_locations[node].append(object_found['name'])
        return objects_locations

    def collect_objects(self, source, objects, verbose=False):
        objects_locations = self.find_objects(objects=objects)
        if verbose:
            print("objects locations: ", objects_locations)
        best_path = self._compute_best_sequence_path(source=source, rooms=list(objects_locations.keys()), verbose=verbose)
        consecutive_pairs = utils.get_consecutive_pairs(best_path)
        shortest_path_among_steps = []
        for pair in consecutive_pairs:
            shortest_path_among_steps.append(nx.shortest_path(G=self._graph, source=pair[0], target=pair[1]))
        if verbose:
            print("steps path ", shortest_path_among_steps)

        moves = [{
            "ID": source,
            "Room": self._rooms[source].get_name(),
            "Objects collected": objects_locations[source] if source in objects_locations else None
        }]
        for shortest_path in shortest_path_among_steps:
            steps = shortest_path[1:]
            for step in steps:
                move = {
                    "ID": step,
                    "Room": str(self._rooms[step].get_name()),
                    "Objects collected": objects_locations[step] if step in objects_locations else None
                }
                moves.append(move)
        return moves

    def _compute_best_sequence_path(self, source, rooms, verbose=False):
        min_cost = None
        min_path = None
        possible_sequences = utils.get_permutations(rooms)
        possible_paths = [[source] + list(sequence) for sequence in possible_sequences]
        if verbose:
            print(f"possibile paths: {str(list(possible_paths))}")
        for path in possible_paths:
            cost = 0
            consecutive_pairs = utils.get_consecutive_pairs(path)
            for consecutive_pair in consecutive_pairs:
                cost += len(nx.shortest_path(G=self._graph, source=consecutive_pair[0], target=consecutive_pair[1]))
            if min_path is None or min_cost < cost:
                min_path = path
                min_cost = cost
        return min_path

    def __str__(self):
        return str(self._graph.edges)

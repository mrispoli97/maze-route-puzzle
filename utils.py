import json
import itertools


def load_json(filepath):
    with open(filepath) as f:
        data = json.load(f)
        return data


def save_json(data, filepath):
    with open(filepath, 'w') as f:
        json.dump(data, f, indent=4)


def list_intersection(lst1, lst2):
    interception = [value for value in lst1 if value in lst2]
    return interception


def get_permutations(values):
    return itertools.permutations(values)


def get_consecutive_pairs(values):
    pairs = []
    for first, second in zip(values, values[1:]):
        pairs.append((first, second))
    return pairs


def print_output(result):
    print("{:<4} {:<20} {:<100}".format('ID', 'Room', 'Objects collected'))
    print("-------------------------------------------")
    for item in result:
        id = item['ID']
        room = item['Room']
        objects_collected = item['Objects collected']
        objects_collected_string = ""
        if objects_collected:
            for object_collected in objects_collected:
                objects_collected_string += object_collected + ", "
            objects_collected_string = objects_collected_string[:-2]
        else:
            objects_collected_string = 'None'
        print("{:<4} {:<20} {:<100}".format(id, room, objects_collected_string))

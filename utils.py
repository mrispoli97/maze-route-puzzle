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

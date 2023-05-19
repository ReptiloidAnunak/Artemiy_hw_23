
from typing import Iterable


def filter_query(value: str, data: Iterable[str]):
    return filter(lambda x: value in x, data)

def map_query(value: int or str, data: Iterable[str]):
    return map(lambda x: x.split(" ")[value], data)

def unique_query(data):
    return set(data)

def sort_query(data, order: str):
    if order == "asc":
        return sorted(data, reverse=False)
    elif order == "desc":
        return sorted(data, reverse=True)
    else:
        raise ValueError

def limit_query(data: Iterable[str], limit):
    with open(data) as f:
        counter = 0
        result = []
        limit = int(limit)
        while True:
            try:
                line = next(f)
            except StopIteration:
                break
            result.append(line)
            counter += 1
            if counter == limit:
                break
        return result


import re
from typing import Generator, TextIO, Iterable, Set, List


def filter_query(value: str, data: Iterable[str]) -> filter:
    return filter(lambda x: value in x, data)


def map_query(value: int, data: Iterable[str]) -> Iterable:
    return map(lambda x: x.split(" ")[value], data)


def unique_query(data: Iterable[str]) -> Set[str]:
    return set(data)


def sort_query(data: Iterable[str], order: str) -> Iterable:
    if order == "asc":
        return sorted(data, reverse=False)
    elif order == "desc":
        return sorted(data, reverse=True)
    else:
        raise ValueError


def limit_query(data: str, limit: int) -> List[str]:
    limit = int(limit)
    with open(data) as f:
        counter = 0
        result = []
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


def apply_regex(regex: str, file: TextIO) -> Generator:
    query = re.compile(regex)
    for line in file:
        if re.search(query, line) is not None:
            yield line
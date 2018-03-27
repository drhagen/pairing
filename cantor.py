from typing import Iterable
from math import floor, sqrt


def cantor_product(stream1: Iterable, stream2: Iterable):
    start_index = 0
    sequence1 = stream1
    while True:
        index1 = start_index
        index2 = 0  # Not used, but included for reference
        for element2 in stream2:
            element1 = sequence1[index1]  # Gets the ith element of the sequence
            yield [element1, element2]
            if index1 == 0:
                break
            else:
                index1 = index1 - 1
                index2 = index2 + 1
        start_index = start_index + 1


def cantor_pairing(index1: int, index2: int):
    return floor((index1 + index2) * (index1 + index2 + 1) / 2) + index2


def cantor_unpairing(index: int):
    w = int((sqrt(8 * index + 1) - 1) / 2)
    t = int((w ** 2 + w) / 2)
    index2 = index - t
    index1 = w - index2
    return [index1, index2]


def cantor_plot():
    from general import pairing_function_plot

    points = [cantor_unpairing(i) for i in range(25)]
    arrows = [
        [0, 0, 1, 0],
        [1, 0, 0, 1],
        [0, 1, 2, 0],
        [2, 0, 1, 1],
        [1, 1, 0, 2],
        [0, 2, 3, 0],
        [3, 0, 2, 1],
        [2, 1, 1, 2],
        [1, 2, 0, 3],
        [4, 0, 3, 1],
        [3, 1, 2, 2],
        [2, 2, 1, 3],
        [1, 3, 0, 4],
        [4, 1, 3, 2],
        [3, 2, 2, 3],
        [2, 3, 1, 4],
        [4, 2, 3, 3],
        [3, 3, 2, 4],
    ]

    return pairing_function_plot(points, arrows)


if __name__ == '__main__':
    from general import assert_consistancy

    cantor_plot().show()
    assert_consistancy(cantor_product, cantor_pairing, cantor_unpairing)

from typing import Iterable
from math import floor, sqrt


def peter_product(stream1: Iterable, stream2: Iterable):
    shell = 0
    max_element1 = next(iter(stream1))
    max_element2 = next(iter(stream2))

    while True:
        index1 = 0  # Not used, just for reference
        index2 = 0
        leg1 = iter(stream1)
        leg2 = iter(stream2)

        while True:
            yield [max_element1, next(leg2)]
            index2 = index2 + 1

            if index2 > shell:
                next(leg1)
                max_element1 = next(leg1)
                max_element2 = next(leg2)
                break

            yield [next(leg1), max_element2]
            index1 = index1 + 1

        shell = shell + 1


def peter_pairing(index1: int, index2: int):
    shell = max(index1, index2)
    step = min(index1, index2)
    if step == index2:
        flag = 0
    else:
        flag = 1
    return shell ** 2 + step * 2 + flag


def peter_unpairing(index: int):
    shell = floor(sqrt(index))
    remainder = index - shell ** 2
    step = floor(remainder / 2)
    if remainder % 2 == 0:  # remainder is even
        return [shell, step]
    else:
        return [step, shell]


def peter_plot():
    from general import pairing_function_plot

    points = [peter_unpairing(i) for i in range(16)]
    arrows = [
        [0, 0, 1, 0],
        [1, 0, 0, 1],
        [0, 1, 1, 1],
        [1, 1, 2, 0],
        [2, 0, 0, 2, {'connectionstyle': 'arc3,rad=-0.1'}],
        [0, 2, 2, 1],
        [2, 1, 1, 2],
        [1, 2, 2, 2],
        [2, 2, 3, 0],
        [3, 0, 0, 3, {'connectionstyle': 'arc3,rad=-0.1'}],
        [0, 3, 3, 1],
        [3, 1, 1, 3, {'connectionstyle': 'arc3,rad=-0.1'}],
        [1, 3, 3, 2],
        [3, 2, 2, 3],
        [2, 3, 3, 3],
    ]

    return pairing_function_plot(points, arrows)


if __name__ == '__main__':
    from general import assert_consistancy

    peter_plot().show()
    assert_consistancy(peter_product, peter_pairing, peter_unpairing)

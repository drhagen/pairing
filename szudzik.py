from typing import Iterable
from math import floor, sqrt


def szudzik_product(stream1: Iterable, stream2: Iterable):
    shell = 0
    while True:
        index2 = 0
        for element2 in stream2:
            if index2 == shell:
                max_element2 = element2
                break
            yield [max_element1, element2]
            index2 = index2 + 1

        index1 = 0
        for element1 in stream1:
            if index1 > shell:
                max_element1 = element1
                break
            yield [element1, max_element2]
            index1 = index1 + 1

        shell = shell + 1


def szudzik_pairing(index1: int, index2: int):
    if index1 > index2:
        return index1 ** 2 + index2
    else:
        return index2 ** 2 + index2 + index1


def szudzik_unpairing(index: int):
    shell = floor(sqrt(index))
    if index - shell ** 2 < shell:
        return [shell, index - shell ** 2]
    else:
        return [index - shell ** 2 - shell, shell]


def szudzik_plot():
    from general import pairing_function_plot

    points = [szudzik_unpairing(i) for i in range(16)]
    arrows = [
        [0, 0, 1, 0],
        [1, 0, 0, 1],
        [0, 1, 1, 1],
        [1, 1, 2, 0],
        [2, 0, 2, 1],
        [2, 1, 0, 2],
        [0, 2, 1, 2],
        [1, 2, 2, 2],
        [2, 2, 3, 0],
        [3, 0, 3, 1],
        [3, 1, 3, 2],
        [3, 2, 0, 3],
        [0, 3, 1, 3],
        [1, 3, 2, 3],
        [2, 3, 3, 3],
    ]

    return pairing_function_plot(points, arrows)


if __name__ == '__main__':
    from general import assert_consistancy

    szudzik_plot().show()
    assert_consistancy(szudzik_product, szudzik_pairing, szudzik_unpairing)

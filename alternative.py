from typing import Iterable
from math import floor, sqrt


def alternative_product(stream1: Iterable, stream2: Iterable):
    shell = 0
    flag = True
    max_element1 = next(iter(stream1))
    max_element2 = next(iter(stream2))

    while True:
        index1 = 0
        index2 = 0
        leg1 = iter(stream1)
        leg2 = iter(stream2)

        while True:
            flag = not flag

            if flag:
                yield [max_element1, next(leg2)]
                index2 = index2 + 1
                if index2 > shell:
                    next(leg1)
                    max_element1 = next(leg1)
                    max_element2 = next(leg2)
                    break
            else:
                yield [next(leg1), max_element2]
                index1 = index1 + 1
                if index1 > shell:
                    next(leg2)
                    max_element2 = next(leg2)
                    max_element1 = next(leg1)
                    break

        shell = shell + 1


def alternative_pairing(index1: int, index2: int):
    shell = max(index1, index2)
    step = min(index1, index2)
    if shell % 2 == 0 and step == index1 or shell % 2 == 1 and step == index2:
        flag = 0
    else:
        flag = 1
    return shell ** 2 + step * 2 + flag


def alternative_unpairing(index: int):
    shell = floor(sqrt(index))
    step = (index - shell ** 2) // 2
    if index % 2 == 0:  # index is even
        return [step, shell]
    else:
        return [shell, step]


def alternative_plot():
    from general import pairing_function_plot

    points = [alternative_unpairing(i) for i in range(16)]
    arrows = [
        [0, 0, 1, 0],
        [1, 0, 0, 1],
        [0, 1, 1, 1],
        [1, 1, 0, 2],
        [0, 2, 2, 0, {'connectionstyle': 'arc3,rad=0.1'}],
        [2, 0, 1, 2],
        [1, 2, 2, 1],
        [2, 1, 2, 2],
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

    alternative_plot().show()
    assert_consistancy(alternative_product, alternative_pairing, alternative_unpairing)

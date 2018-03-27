from typing import Iterable
from math import floor


def box_product(stream1: Iterable, stream2: Iterable):
    for element2 in stream2:
        for element1 in stream1:
            yield [element1, element2]


def box_pairing(length1: int, length2: int, index1: int, index2: int):
    return index1 + index2 * length1


def box_unpairing(length1: int, length2: int, index: int):
    index1 = index % length1  # modulo operation
    index2 = floor(index / length1)  # integer division
    return [index1, index2]


def box_plot():
    from general import pairing_function_plot

    points = [box_unpairing(3, 2, i) for i in range(6)]
    arrows = [
        [0, 0, 1, 0],
        [1, 0, 2, 0],
        [2, 0, 0, 1],
        [0, 1, 1, 1],
        [1, 1, 2, 1],
    ]

    return pairing_function_plot(points, arrows)


def bad_plot():
    from general import pairing_function_plot

    points = [[0, 0], [1, 0], [2, 0], [3, 0]]
    arrows = [
        [0, 0, 1, 0],
        [1, 0, 2, 0],
        [2, 0, 3, 0],
        [3, 0, 4, 0],
    ]

    fig = pairing_function_plot(points, arrows)

    ax = fig.axes[0]

    extra_points = [[x, y + 1] for x in range(4) for y in range(3)]
    ax.scatter(*zip(*extra_points), linestyle="None", marker='o', color='yellow')

    return fig


if __name__ == '__main__':
    box_plot().show()
    bad_plot().show()

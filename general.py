from itertools import count

from matplotlib import pyplot as plt
from matplotlib.patches import FancyArrowPatch

from typing import Iterable


class Count(Iterable):
    def __init__(self, start: int = 0, step: int = 1):
        self.start = start
        self.step = step

    def __iter__(self):
        return count(self.start, self.step)

    def __getitem__(self, key):
        if isinstance(key, int):
            return self.start + key
        elif isinstance(key, slice):
            # Bounded, use range
            if key.start is None:
                start = self.start
            else:
                start = self.start + self.step * key.start

            if key.stop is None:
                stop = None
            else:
                stop = self.start + self.step * key.stop

            if key.step is None:
                step = self.step
            else:
                step = self.step * key.step

            if stop is None:
                # Unbounded, use Count
                return Count(start, step)
            else:
                return range(start, stop, step)
        else:
            raise TypeError(f'Count indexes must be int or slice, not {type(key).__name__}')


def pairing_function_plot(points, arrows):
    n = 4

    fig, ax = plt.subplots(figsize=(3, 3))
    fig.tight_layout()
    fig.patch.set_color('black')

    x_ticks = list(range(n))
    y_ticks = list(range(n))

    ax.scatter(*zip(*points), linestyle="None", marker='o', color='yellow')

    for i, (x, y) in enumerate(points):
        offset = 0.06
        ax.annotate(i, (x + offset, y + offset), color='white')

    for i, arrow in enumerate(arrows):
        x1 = arrow[0]
        y1 = arrow[1]
        x2 = arrow[2]
        y2 = arrow[3]

        additional = arrow[4] if len(arrow) >= 5 else {}

        ax.add_patch(FancyArrowPatch((x1, y1), (x2, y2), **additional, shrinkA=7, shrinkB=7, color='white',
                                     arrowstyle='simple,head_width=4,head_length=8'))

    ax.set_aspect('equal')
    ax.patch.set_alpha(0)
    ax.xaxis.set_ticks(x_ticks)
    ax.yaxis.set_ticks(y_ticks)
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.xaxis.label.set_color('white')
    ax.yaxis.label.set_color('white')
    ax.spines['bottom'].set_color('white')
    ax.spines['top'].set_color('white')
    ax.spines['right'].set_color('white')
    ax.spines['left'].set_color('white')
    ax.tick_params(axis='x', colors='white')
    ax.tick_params(axis='y', colors='white')

    margin = 0.25
    ax.axis([-margin, n - 1 + margin + 0.2, -margin, n - 1 + margin + 0.1])

    return fig


def assert_consistancy(product, pairing, unpairing):
    for i, (x, y) in zip(range(100), product(Count(), Count())):
        print(f'{i} == {pairing(x, y)}, {[x,y]} == {unpairing(i)}')
        assert i == pairing(x, y)
        assert [x, y] == unpairing(i)

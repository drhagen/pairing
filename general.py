from functools import reduce
from itertools import count
from operator import mul
from typing import Iterable

from matplotlib import pyplot as plt
from matplotlib.patches import FancyArrowPatch
from mpl_toolkits.mplot3d import proj3d


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


def prod(iterable):
    return reduce(mul, iterable, 1)


def floored_root(x, n):
    """Integer component of nth root of x.

    Uses binary search to find the integer y such that y ** n <= x < (y + 1) ** n.

    Adapted from https://stackoverflow.com/a/356206/1485877
    """
    high = 1
    while high ** n <= x:
        high *= 2
    low = high // 2
    while low < high:
        mid = (low + high) // 2
        if low < mid and mid ** n < x:
            low = mid
        elif high > mid and mid ** n > x:
            high = mid
        else:
            return mid
    return mid + 1


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


def three_dimensional_plot(points, arrows):
    from mpl_toolkits.mplot3d import Axes3D
    from matplotlib import pyplot as plt

    n = 3

    fig = plt.figure(figsize=(5, 5))
    ax = Axes3D(fig)
    ax.view_init(25, 30)
    ax.grid(False)
    fig.patch.set_color('black')

    x_ticks = list(range(n))
    y_ticks = list(range(n))
    z_ticks = list(range(n))

    ax.scatter(*zip(*points), linestyle='None', marker='o', color='yellow')

    for i, (x, y, z) in enumerate(points):
        offset = 0.1
        ax.text(x + offset, y + offset, z + offset, i, color='white')

    for i, arrow in enumerate(arrows):
        x1 = arrow[0]
        y1 = arrow[1]
        z1 = arrow[2]
        x2 = arrow[3]
        y2 = arrow[4]
        z2 = arrow[5]

        additional = arrow[6] if len(arrow) >= 7 else {}

        ax.add_artist(Arrow3D((x1, x2), (y1, y2), (z1, z2), **additional, shrinkA=7, shrinkB=7, color='white',
                              arrowstyle='simple,head_width=4,head_length=8'))

    ax.patch.set_alpha(0)
    ax.xaxis.set_ticks(x_ticks)
    ax.yaxis.set_ticks(y_ticks)
    ax.zaxis.set_ticks(z_ticks)
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.set_zlabel('z')
    ax.w_xaxis.line.set_color('white')
    ax.w_yaxis.line.set_color('white')
    ax.w_zaxis.line.set_color('white')
    ax.w_zaxis.line.set_color('white')
    ax.xaxis.label.set_color('white')
    ax.yaxis.label.set_color('white')
    ax.zaxis.label.set_color('white')
    ax.xaxis.pane.fill = False
    ax.yaxis.pane.fill = False
    ax.zaxis.pane.fill = False
    ax.xaxis.pane.set_edgecolor('w')
    ax.yaxis.pane.set_edgecolor('w')
    ax.zaxis.pane.set_edgecolor('w')
    ax.xaxis._axinfo['tick']['color'] = 'w'
    ax.yaxis._axinfo['tick']['color'] = 'w'
    ax.zaxis._axinfo['tick']['color'] = 'w'
    ax.tick_params(axis='x', colors='white')
    ax.tick_params(axis='y', colors='white')
    ax.tick_params(axis='z', colors='white')

    return fig


def assert_consistency(product, pairing, unpairing):
    for i, (x, y) in zip(range(100), product(Count(), Count())):
        print(f'{i} == {pairing(x, y)}, {[x, y]} == {unpairing(i)}')
        assert i == pairing(x, y)
        assert [x, y] == unpairing(i)


def assert_multidimensional_consistency(product, pairing, unpairing):
    dims = 4
    for dim in range(1, dims+1):
        iterables = [Count()] * dim
        for i, elements in zip(range(100), product(*iterables)):
            paired = pairing(*elements)
            unpaired = unpairing(dim, i)
            print(f'{i} == {paired}, {elements} == {unpaired}')
            assert i == paired
            assert elements == unpaired


class Arrow3D(FancyArrowPatch):
    def __init__(self, xs, ys, zs, *args, **kwargs):
        FancyArrowPatch.__init__(self, (0, 0), (0, 0), *args, **kwargs)
        self._verts3d = xs, ys, zs

    def draw(self, renderer):
        xs3d, ys3d, zs3d = self._verts3d
        xs, ys, zs = proj3d.proj_transform(xs3d, ys3d, zs3d, renderer.M)
        self.set_positions((xs[0], ys[0]), (xs[1], ys[1]))
        FancyArrowPatch.draw(self, renderer)

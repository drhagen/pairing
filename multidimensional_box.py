from typing import List, Iterable

from general import three_dimensional_plot


def multidimensional_box_product(*streams: Iterable) -> List:
    n = len(streams)

    def recursive_product(i_stream) -> List:
        for element in streams[i_stream]:
            if i_stream == n - 1:
                # On final dimension, yield each element
                yield [element]
            else:
                # On other dimension, yield each element followed by each
                # possible combination of elements in the remaining dimensions
                for remaining_elements in recursive_product(i_stream + 1):
                    yield [element] + remaining_elements

    yield from recursive_product(0)


def multidimensional_box_pairing(lengths: List[int], indexes: List[int]) -> int:
    # Should probably assert that all indexes are less than corresponding lengths
    n = len(lengths)
    index = 0
    dimension_product = 1
    # Compute indexes from last to first because that is the order the product is grown
    for dimension in reversed(range(n)):
        index += indexes[dimension] * dimension_product
        dimension_product *= lengths[dimension]

    return index


def multidimensional_box_unpairing(lengths: List[int], index: int) -> List[int]:
    # Should probably assert that index is less than the product of lengths
    n = len(lengths)
    indexes = [0] * n  # Preallocate list
    dimension_product = 1
    # Compute indexes from last to first because that is the order the product is grown
    for dimension in reversed(range(n)):
        indexes[dimension] = index // dimension_product % lengths[dimension]
        dimension_product *= lengths[dimension]

    return indexes


def multidimensional_box_plot():
    points = [
        [0, 0, 0],
        [0, 0, 1],
        [0, 0, 2],
        [0, 1, 0],
        [0, 1, 1],
        [0, 1, 2],
        [1, 0, 0],
        [1, 0, 1],
        [1, 0, 2],
        [1, 1, 0],
        [1, 1, 1],
        [1, 1, 2],
    ]

    arrows = [
        [0, 0, 0, 0, 0, 1],
        [0, 0, 1, 0, 0, 2],
        [0, 0, 2, 0, 1, 0],
        [0, 1, 0, 0, 1, 1],
        [0, 1, 1, 0, 1, 2],
        [1, 0, 0, 1, 0, 1],
        [1, 0, 1, 1, 0, 2],
        [1, 0, 2, 1, 1, 0],
        [1, 1, 0, 1, 1, 1],
        [1, 1, 1, 1, 1, 2],
    ]

    return three_dimensional_plot(points, arrows)


if __name__ == '__main__':
    lengths = [2, 3, 4]
    for i, (x, y, z) in enumerate(multidimensional_box_product(*[list(range(length)) for length in lengths])):
        paired = multidimensional_box_pairing(lengths, [x, y, z])
        unpaired = multidimensional_box_unpairing(lengths, i)
        print(f'{i} == {paired}, {[x, y, z]} == {unpaired}')
        assert i == paired
        assert [x, y, z] == unpaired

    multidimensional_box_plot().show()

from typing import List, Iterable

from general import floored_root, three_dimensional_plot
from multidimensional_box import multidimensional_box_unpairing, multidimensional_box_pairing


def multidimensional_szudzik_product(*streams: Iterable):
    n = len(streams)

    if n == 0:
        # The Cartesian product of no streams is a single empty item
        yield []
        return

    # In the recursive function, it must possible to get the shell element of the final stream. This iterator is stepped
    # through at each shell to produce the final_shell_element.
    final_shell_iterator = iter(streams[-1])

    def recursive_product(i_stream, shell_used) -> list:
        if i_stream == n - 1:
            if shell_used:
                # A shell element was emitted earlier in the item
                for i_element, element in zip(range(shell + 1), streams[i_stream]):
                    yield [element]
            else:
                # No shell element has been emitted for this item yet and the recursive function is at the last
                # stream, so a shell element only must be emitted or else this item will not be on the shell.
                yield [final_shell_element]
        else:
            for i_element, element in zip(range(shell + 1), streams[i_stream]):
                next_shell_used = shell_used or i_element == shell

                for remaining_elements in recursive_product(i_stream + 1, next_shell_used):
                    yield [element] + remaining_elements

    shell = 0
    while True:
        final_shell_element = next(final_shell_iterator)

        yield from recursive_product(0, False)

        shell += 1


def multidimensional_szudzik_pairing(*indexes: int) -> int:
    n = len(indexes)

    if n == 0:
        # The only one element of a Cartesian product of zero streams and this is it
        return 0

    shell = max(indexes)

    def recursive_index(dim: int):
        # Number of dimensions of a slice perpendicular to the current axis
        slice_dims = n - dim - 1

        # Number of elements in a slice (only those on the current shell)
        subshell_count = (shell + 1) ** slice_dims - shell ** slice_dims

        index_i = indexes[dim]
        if index_i == shell:
            # Once an index on the shell is encountered, the remaining indexes follow
            # multidimensional box pairing
            return subshell_count * shell + multidimensional_box_pairing([shell + 1] * slice_dims,
                                                                         indexes[dim + 1:])
        else:
            # Compute the contribution from the next index the same way
            # by recursing to the next dimension
            return subshell_count * index_i + recursive_index(dim + 1)

    # Start with the number of elements from before this shell and recursively
    # find the contribution from each index to the linear index
    return shell ** n + recursive_index(0)


def multidimensional_szudzik_unpairing(n: int, index: int) -> List[int]:
    shell = floored_root(index, n)

    def recursive_indexes(dim: int, remaining: int):
        if dim == n - 1:
            # If this is reached, that means that no index so far has been on the shell. By construction, this
            # final index must be on the shell or else the point itself will not be on the shell.
            return [shell]
        else:
            # Number of dimensions of a slice perpendicular to the current axis
            slice_dims = n - dim - 1

            # Number of elements in a slice (only those on the current shell)
            subshell_count = (shell + 1) ** slice_dims - shell ** slice_dims

            index_i = min(remaining // subshell_count, shell)
            if index_i == shell:
                # Once an index on the shell is encountered, the remaining indexes follow
                # multidimensional box unpairing
                return [shell] + multidimensional_box_unpairing([shell + 1] * slice_dims,
                                                                remaining - subshell_count * shell)
            else:
                # Compute the next index the same way by
                # recursing to the next dimension
                return [index_i] + recursive_indexes(dim + 1, remaining - subshell_count * index_i)

    # Subtract out the elements from before this shell and recursively
    # find the index at each dimension from what remains
    return recursive_indexes(0, index - shell ** n)


def multidimensional_recursive_szudzik_plot():
    # Plot third shell only
    points = [
        [0, 0, 2],
        [0, 1, 2],
        [1, 0, 2],
        [1, 1, 2],

        [0, 2, 0],
        [0, 2, 1],
        [1, 2, 0],
        [1, 2, 1],
        [0, 2, 2],
        [1, 2, 2],

        [2, 0, 0],
        [2, 0, 1],
        [2, 1, 0],
        [2, 1, 1],
        [2, 0, 2],
        [2, 1, 2],
        [2, 2, 0],
        [2, 2, 1],
        [2, 2, 2],
    ]

    arrows = [
        [0, 0, 2, 0, 1, 2],
        [0, 1, 2, 1, 0, 2],
        [1, 0, 2, 1, 1, 2],
        [0, 2, 0, 0, 2, 1],
        [0, 2, 1, 1, 2, 0],
        [1, 2, 0, 1, 2, 1],
        [1, 2, 1, 0, 2, 2],
        [0, 2, 2, 1, 2, 2],
        [2, 0, 0, 2, 0, 1],
        [2, 0, 1, 2, 1, 0],
        [2, 1, 0, 2, 1, 1],
        [2, 1, 1, 2, 0, 2],
        [2, 0, 2, 2, 1, 2],
        [2, 1, 2, 2, 2, 0],
        [2, 2, 0, 2, 2, 1],
        [2, 2, 1, 2, 2, 2],
    ]

    return three_dimensional_plot(points, arrows)


def multidimensional_sorted_szudzik_plot():
    # Plot third shell only
    points = [
        [0, 0, 2],
        [0, 1, 2],
        [0, 2, 0],
        [0, 2, 1],
        [0, 2, 2],
        [1, 0, 2],
        [1, 1, 2],
        [1, 2, 0],
        [1, 2, 1],
        [1, 2, 2],
        [2, 0, 0],
        [2, 0, 1],
        [2, 0, 2],
        [2, 1, 0],
        [2, 1, 1],
        [2, 1, 2],
        [2, 2, 0],
        [2, 2, 1],
        [2, 2, 2],
    ]

    arrows = [
        [0, 0, 2, 0, 1, 2],
        [0, 1, 2, 0, 2, 0],
        [0, 2, 0, 0, 2, 1],
        [0, 2, 1, 0, 2, 2],
        [1, 0, 2, 1, 1, 2],
        [1, 1, 2, 1, 2, 0],
        [1, 2, 0, 1, 2, 1],
        [1, 2, 1, 1, 2, 2],
        [2, 0, 0, 2, 0, 1],
        [2, 0, 1, 2, 0, 2],
        [2, 0, 2, 2, 1, 0],
        [2, 1, 0, 2, 1, 1],
        [2, 1, 1, 2, 1, 2],
        [2, 1, 2, 2, 2, 0],
        [2, 2, 0, 2, 2, 1],
        [2, 2, 1, 2, 2, 2],
    ]

    return three_dimensional_plot(points, arrows)


if __name__ == '__main__':
    from general import assert_multidimensional_consistency

    multidimensional_recursive_szudzik_plot().show()
    multidimensional_sorted_szudzik_plot().show()
    assert_multidimensional_consistency(multidimensional_szudzik_product, multidimensional_szudzik_pairing,
                                        multidimensional_szudzik_unpairing)

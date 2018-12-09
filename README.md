# Superior Pairing Function

This is the code behind a [blog post](https://drhagen.com/blog/superior-pairing-function/) on pairing functions and a follow-up [blog post](https://drhagen.com/blog/multidimensional-pairing-functions/) on n-dimensional pairing functions. A pairing function returns the Cartesian product (all possible combinations) of two infinite streams. As explained in the post, the naive approaches to the Cartesian product do not work on infinite streams and existing pairing functions have some undesirable properties for programmatic purposes, for which I discuss solutions.

## Dependencies

* [matplotlib](https://github.com/matplotlib/matplotlib)

## Structure

There are five methods described in the first post, each of which is coded up in a separate file:

* `box.py`: Not an actual pairing function as it only works on finite lists not infinite streams
* `cantor.py`: The [original pairing function](https://en.wikipedia.org/wiki/Pairing_function) by George Cantor
* `szudzik.py`: The [elegant pairing function](http://szudzik.com/ElegantPairing.pdf) by Matthew Szudzik
* `peter.py`: The superior pairing function by Rozsa Peter
* `alternative.py`: The alternative pairing function by me

There are two methods described in the second post, each of which is also coded up in a separate file:

* `multidimensional_box.py`: Not an actual pairing function as it only works on a list of finite streams
* `multidimensional_szudzik.py`: An implementation of the n-dimensional generalization suggested in the elegant pairing function

Each method has three functions associated with it:

* **Pairing** function `(Index, Index) -> Index` which takes two indexes into streams and returns the index into the Cartesian product stream
* **Unpairing** function `(Index) -> [Index, Index]` which takes an index into the Cartesian product stream and produces two indexes into the individual streams
* **Cartesian product** function `(Iterable[A], Iterable[B]) -> Iterable[[A, B]]` which takes two streams and produces a stream of all possible combinations

## Usage

Run any of the four pairing function scripts to cause a matplotlib figure illustrating that method to be displayed and the first 100 indexes of each method to be printed and validated. Run `save_figures.py` to recreate all the SVG versions of all the figures in the blog posts.

## License

All code is made available under the MIT license. See `license.txt`.

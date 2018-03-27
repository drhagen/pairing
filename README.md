# Superior Pairing Function

This is the code behind a [blog post](http://drhagen.com/blog/superior-pairing-function/) introducing the superior pairing function. A pairing function returns the Cartesian product (all possible combinations) of two infinite streams. As explained in the post, the naive approaches to the Cartesian product do not work on infinite streams and existing pairing functions have some undesirable properties for programmatic purposes, which I rectify in my version.

## Dependencies

* [matplotlib](http://github.com/matplotlib/matplotlib)

## Structure

There are four methods described in the post, each of which is coded up in a separate file:

* `cantor.py`: The [original pairing function](https://en.wikipedia.org/wiki/Pairing_function) by George Cantor
* `szudzik.py`: The [elegant pairing function](http://szudzik.com/ElegantPairing.pdf) by Matthew Szudzik
* `hagen.py`: The superior pairing function by me
* `alternative.py`: The alternative pairing function, also by me

Each method has three functions associated with it:

* **Pairing** function `(Index, Index) -> Index` which takes two indexes into streams and returns the index into the Cartesian product stream
* **Unpairing** function `(Index) -> [Index, Index]` which takes an index into the Cartesian product stream and produces two indexes into the individual streams
* **Cartesian product** function `(Iterable[A], Iterable[B]) -> Iterable[[A, B]]` which takes two streams and produces a stream of all possible combinations

## Usage

Run any of the four pairing function scripts to cause a matplotlib figure illustrating that method to be displayed. Run `save_figures.py` to recreate all the SVG versions of all the figures in the blog post.

## License

All code is made available under the MIT license. See `license.txt`.

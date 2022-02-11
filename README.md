# mcl-python

`mcl-python` is a Python library that creates bindings for [mcl](https://github.com/herumi/mcl) library by 光成滋生 MITSUNARI Shigeo(herumi@nifty.com).

## Supported curves

For now the only supported curve is `BLS12_384` (named in library `BN384_256`)

## Installation

Please clone this repository and set the `DIR_FOR_LINKER` varriable in `hook.py` in mcl folder to the compiled and installed mcl library.

## Usage

```python
import sys
sys.path.insert(1, '<path to cloned repo>')

from mcl import Fr

# create new random fr
fr = Fr.rnd()
```

For more examples, please check [tests](tests/).

## Tests

Tests are written in `unittest`.

```
python3 -m unittest discover tests/
```

## Jlib

There is a small library `jlib.py` contains functions, that stores and loads the results of mcl into json in order to provide capability of exchanging the information in a consistent format.

```python
import sys
sys.path.insert(1, '<path to cloned repo>')

from mcl import Fr
from mcl import G1

a = Fr.rnd()
x = Fr.rnd()
Q = G1.hashAndMapTo(b'abc')
A = Q * a
X = Q * x

# creaing a json message
message = jstore({'A': A, 'X': X})

# unpacking json message
A_, X_ = jload({'A': G1, 'X': G1}, message)
```

## Patches

The library needed some bugfixes and implementation of some missing features in order to solve laboratory lists.

- Patched `serialize` function, which cut the buffer after first null. Now the function takes into account the length of the buffer returned from otiginal mcl
- Implemented missing power operation for `GT`
- Implemented `setHashOf` function for creating hash of `Fr` values

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
[MIT](https://choosealicense.com/licenses/mit/)

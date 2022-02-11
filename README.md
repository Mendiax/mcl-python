# mcl-python

`mcl-python` is a Python library that creates bindings for [mcl](https://github.com/herumi/mcl) library by 光成滋生 MITSUNARI Shigeo(herumi@nifty.com).

## Supported curves

For now the only supported curve is `BLS12_384` (named in library `BN384_256`)

## Installation

Please clone this repository and setup path for the installed mcl library in `hook.py` in mcl folder.

## Usage

```python
import mcl

fr = new mcl.Fr()
fr.setByCSPRNG()
```

For more examples, please check [tests](tests/).

## Tests

Tests are written in `unittest`.

```
python3 -m unittest discover tests/
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

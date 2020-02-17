# h5cv

[![PyPI version](https://badge.fury.io/py/h5cv.svg)](https://badge.fury.io/py/h5cv)
[![Build Status](https://secure.travis-ci.org/toyama0919/h5cv.png?branch=master)](http://travis-ci.org/toyama0919/h5cv)

show hdf5 file in image file.


## h5cv command

#### list keys

```bash
$ h5cv -H test.h5 ls [images]
```

#### show dataset in hdf5.

```bash
$ h5cv -H test.h5 show /some_group/test.jpg.np
```

#### imgcat in hdf5.

```bash
$ h5cv -H test.h5 show /some_group/test.jpg.np
```

#### write in hdf5.

```bash
$ h5cv -H test.h5 [--store [numpy|binary]] write -g 'images/*.jpg'
```

## custom generator

```
from h5cv.core import Core
from PIL import Image


class MyGenerator:
    def __init__(self):
        pass

    def __call__(self, path):
        print(f"custom generate {path}")
        return Image.open(path)

Core(
    hdf5="test.h5",
    generator=MyGenerator()
).write("evaluation/*.jpg")
```


## Installation

```sh
pip install h5cv
```

### Installation from github

```sh
pip install git+https://github.com/toyama0919/h5cv
```

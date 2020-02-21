# h5cv

[![PyPI version](https://badge.fury.io/py/h5cv.svg)](https://badge.fury.io/py/h5cv)
[![Build Status](https://secure.travis-ci.org/toyama0919/h5cv.png?branch=master)](http://travis-ci.org/toyama0919/h5cv)

show hdf5 file in image file.


## h5cv command

#### list keys

```bash
$ h5cv -H test.h5 ls [-r] [key]
```

#### show dataset in hdf5.

```bash
$ h5cv -H test.h5 show /some_group/test.jpg.np
```

#### imgcat in hdf5.

```bash
$ h5cv -H test.h5 imgcat /some_group/test.jpg
```

#### write in hdf5.

```bash
$ h5cv -H test.h5 [--store [numpy|binary]] write -g 'images/*.jpg' [--compression gzip] [--append]
```

## custom generator

```
from h5cv.core import Core
from h5cv.generator import Generator
from PIL import Image


class MyGenerator(Generator):
    def __getitem__(self, path):
        print(f"custom generate {path}")
        return Image.open(path)

Core(
    hdf5="test.h5"
).write(
    "evaluation/*.jpg",
    generator=MyGenerator(),
    compression="gzip"
)
```


## Installation

```sh
pip install h5cv
```

### Installation from github

```sh
pip install git+https://github.com/toyama0919/h5cv
```

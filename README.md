# h5cv

[![PyPI version](https://badge.fury.io/py/h5cv.svg)](https://badge.fury.io/py/h5cv)
[![Build Status](https://secure.travis-ci.org/toyama0919/h5cv.png?branch=master)](http://travis-ci.org/toyama0919/h5cv)

show hdf5 file in image file.


## get start

```bash
$ ls -lh evaluation/
total 2936
-rw-r--r--@ 1 hiroshi.toyama  1522739515    37K  7  3  2019 car1.jpg
-rw-r--r--@ 1 hiroshi.toyama  1522739515   188K  7  3  2019 cat1.jpg
-rw-r--r--  1 hiroshi.toyama  1522739515   137K  7  3  2019 dog1.jpg
-rw-r--r--  1 hiroshi.toyama  1522739515    51K  7  3  2019 dog2.jpg
-rw-r--r--  1 hiroshi.toyama  1522739515    77K  7  3  2019 dog3.jpg
-rw-r--r--  1 hiroshi.toyama  1522739515   8.8K  7  3  2019 dog4.jpg
-rw-r--r--@ 1 hiroshi.toyama  1522739515    42K  7  3  2019 monitor1.jpg
-rw-r--r--  1 hiroshi.toyama  1522739515   267K  7  3  2019 person1.jpg
-rw-r--r--  1 hiroshi.toyama  1522739515   170K  7  3  2019 person2.jpg
-rw-r--r--  1 hiroshi.toyama  1522739515   467K  7  3  2019 room1.jpg

$ h5cv -H test.h5 --store numpy write -g 'evaluation/*.jpg' -a
2020-03-06 19:13:35,972 INFO - compression => None
2020-03-06 19:13:35,973 INFO - generate numpy: evaluation/dog4.jpg => test.h5:evaluation/dog4.jpg
2020-03-06 19:13:35,977 INFO - generate numpy: evaluation/car1.jpg => test.h5:evaluation/car1.jpg
2020-03-06 19:13:35,978 INFO - generate numpy: evaluation/dog3.jpg => test.h5:evaluation/dog3.jpg
2020-03-06 19:13:35,980 INFO - generate numpy: evaluation/monitor1.jpg => test.h5:evaluation/monitor1.jpg
2020-03-06 19:13:35,982 INFO - generate numpy: evaluation/dog2.jpg => test.h5:evaluation/dog2.jpg
2020-03-06 19:13:35,983 INFO - generate numpy: evaluation/dog1.jpg => test.h5:evaluation/dog1.jpg
2020-03-06 19:13:35,985 INFO - generate numpy: evaluation/cat1.jpg => test.h5:evaluation/cat1.jpg
2020-03-06 19:13:35,987 INFO - generate numpy: evaluation/person1.jpg => test.h5:evaluation/person1.jpg
2020-03-06 19:13:35,989 INFO - generate numpy: evaluation/person2.jpg => test.h5:evaluation/person2.jpg
2020-03-06 19:13:35,991 INFO - generate numpy: evaluation/room1.jpg => test.h5:evaluation/room1.jpg

$ h5cv -H test.h5 ls -r
evaluation
evaluation/car1.jpg
evaluation/cat1.jpg
evaluation/dog1.jpg
evaluation/dog2.jpg
evaluation/dog3.jpg
evaluation/dog4.jpg
evaluation/monitor1.jpg
evaluation/person1.jpg
evaluation/person2.jpg
evaluation/room1.jpg
```

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
$ h5cv -H test.h5 \
  [--store [numpy|binary]] \
  write \
  -g 'images/*.jpg' \
  [--output-group mygroup] \
  [--compression gzip] \
  [--append]
```

#### delete dataset or group in hdf5.

```bash
$ h5cv -H test.h5 delete /some_group/test.jpg
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

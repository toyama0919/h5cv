# h5cv

[![PyPI version](https://badge.fury.io/py/h5cv.svg)](https://badge.fury.io/py/h5cv)
[![Build Status](https://secure.travis-ci.org/toyama0919/h5cv.png?branch=master)](http://travis-ci.org/toyama0919/h5cv)

show hdf5 file in image file.


## Examples

#### list keys

```bash
$ h5cv -H test.h5 ls /

```

#### imgcat in hdf5.

```bash
$ h5cv -H test.h5 imgcat /some_group/test.jpg.np
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
$ h5cv -H test.h5 write -g 'images/*.jpg'
```

## Installation

```sh
pip install h5cv
```

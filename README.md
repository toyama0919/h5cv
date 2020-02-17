# h5cv

[![PyPI version](https://badge.fury.io/py/h5cv.svg)](https://badge.fury.io/py/h5cv)
[![Build Status](https://secure.travis-ci.org/toyama0919/h5cv.png?branch=master)](http://travis-ci.org/toyama0919/h5cv)

Command Line utility for Amazon Aurora.

Support python3 only. (use boto3)

## Settings

```sh
export AWS_ACCESS_KEY_ID=XXXXXXXXXXXXXXXXXXXX
export AWS_SECRET_ACCESS_KEY=XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
export AWS_DEFAULT_REGION=xx-xxxxxxx-x
```

* support environment variables and iam role.

## Examples

#### list instance and cluster

```bash
$ h5cv list

[instances]
db01 mysql available db.m3.xlarge  ap-northeast-1c None
db02 mysql available db.m3.xlarge  ap-northeast-1c None
db03 mysql available db.m3.large ap-northeast-1c None
db04 mysql available db.m3.large ap-northeast-1c None
db05 aurora available db.t2.medium  ap-northeast-1c aurora-cluster
db06 aurora available db.t2.medium  ap-northeast-1c aurora-cluster

[clusters]
aurora-cluster available aurora  ['db05', 'db06']
...
```

## Installation

```sh
pip install h5cv
```

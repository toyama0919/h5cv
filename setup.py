from setuptools import setup, find_packages
import os
import re

here = os.path.abspath(os.path.dirname(__file__))


def read_version():
    version_match = re.search(
        r"^VERSION = ['\"]([^'\"]*)['\"]",
        open(os.path.join("src", "h5cv", "__init__.py")).read(),
        re.M,
    )
    if version_match:
        return version_match.group(1)
    raise RuntimeError("Unable to find version string.")


install_requires = [
    "h5py",
    "click",
    "PyYAML",
    "imgcat",
]
extras_require = {"test": ["tox", "twine", "wheel"]}

setup(
    name="h5cv",
    scripts=["bin/h5cv"],
    version=read_version(),
    description="Command Line utility for cost of aws.",
    long_description=open(os.path.join(here, "README.md")).read(),
    long_description_content_type="text/markdown",
    classifiers=[
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
    ],
    keywords="h5cv hdf5 Python3 cv",
    author="Hiroshi Toyama",
    author_email="toyama0919@gmail.com",
    url="https://github.com/toyama0919/h5cv",
    license="MIT",
    packages=find_packages("src", exclude=["tests"]),
    package_dir={"": "src"},
    include_package_data=True,
    zip_safe=False,
    install_requires=install_requires,
    extras_require=extras_require,
    tests_require=extras_require["test"],
    entry_points={"console_scripts": ["h5cv=h5cv.commands:main"]},
)

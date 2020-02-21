import os
import yaml
import h5py
import glob
from imgcat import imgcat
from .logger import get_logger
from .generator import Generator
from . import constants


class Core:
    def __init__(
        self, config=None, profile=None, hdf5=None, store=None, debug=None,
    ):
        profile = self._read_profile(config, profile)
        self.hdf5 = hdf5 or profile.get("hdf5")
        self.store = store or profile.get("store") or constants.DEFAULT_STORE
        self.debug = debug
        self.logger = get_logger(debug)

    def list(self, key, recursive=False):
        with h5py.File(self.hdf5, "r") as root:
            result = root.get(key) if key else root
            if (
                result.__class__ == h5py._hl.group.Group
                or result.__class__ == h5py._hl.files.File
            ):
                if recursive:
                    result.visit(self._print_all)
                else:
                    for key in result.keys():
                        print(key)
            elif result.__class__ == h5py._hl.dataset.Dataset:
                print(result.name)

    def write(self, glob_string, append=False, generator=None, **settings):
        generator = generator or Generator(store=self.store, debug=self.debug)
        mode = "a" if append else "w"
        paths = glob.glob(glob_string, recursive=True)
        with h5py.File(self.hdf5, mode) as root:
            generator(root, paths, settings=settings)

    def imgcat(self, key):
        with h5py.File(self.hdf5, "r") as root:
            image_numpy = root[key][()]
            imgcat(image_numpy.tostring())

    def show(self, key):
        with h5py.File(self.hdf5, "r") as root:
            dataset = root[key][()]
            print(dataset)

    def _read_profile(self, config, profile_name):
        config = config or constants.DEFAULT_CONFIG
        profile_name = profile_name or constants.DEFAULT_PROFILE
        if config and os.path.exists(config):
            profile = yaml.load(open(config, encoding="UTF-8").read()).get(profile_name)
            if profile is None:
                profile = {}
        else:
            profile = {}
        return profile

    def _print_all(self, name):
        print(name)

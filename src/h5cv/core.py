import os
import yaml
import h5py
import numpy
import glob
import cv2
from imgcat import imgcat
from .logger import get_logger
from .generator import Generator
from . import constants


class Core:
    def __init__(
        self,
        config=None,
        profile=None,
        hdf5=None,
        store=None,
        debug=None
    ):
        profile = self._read_profile(config, profile)
        self.hdf5 = hdf5 or profile.get("hdf5")
        self.store = store or profile.get("store") or constants.DEFAULT_STORE
        self.logger = get_logger(debug)
        self.generator = Generator(store=self.store)

    def list(self, key):
        with h5py.File(self.hdf5, "r") as root:
            result = root.get(key) if key else root
            if (
                result.__class__ == h5py._hl.group.Group
                or result.__class__ == h5py._hl.files.File
            ):
                for key in result.keys():
                    print(key)
            elif result.__class__ == h5py._hl.dataset.Dataset:
                print(result.name)

    def add_files(self, globs, compression=None):
        with h5py.File(self.hdf5, "a") as root:
            for glob_string in globs:
                img_paths = glob.glob(glob_string, recursive=True)
                for i, path in enumerate(img_paths):
                    if os.path.isfile(path):
                        if root.get(path):
                            self.logger.debug(f"already exist => {path}")
                        else:
                            data = self.generator(path)
                            self.logger.debug(f"data => {data}")
                            root.create_dataset(path, data=data, compression=compression)

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

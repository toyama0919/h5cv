import numpy
import os
from .logger import get_logger


class Generator:
    def __init__(self, store="binary", debug=False):
        self.store = store
        self.logger = get_logger(debug)

    def __call__(self, root, paths, settings={}):
        compression = settings.get("compression")
        self.logger.info(f"compression => {compression}")
        for i, path in enumerate(paths):
            if os.path.isfile(path):
                if root.get(path):
                    self.logger.debug(f"already exist => {path}")
                else:
                    data = self.__getitem__(path)
                    root.create_dataset(path, data=data, compression=compression)

    def __getitem__(self, path):
        self.logger.info(f"generate {self.store} => {path}")
        with open(path, "rb") as f:
            if self.store == "binary":
                data = numpy.void(f.read())
            elif self.store == "numpy":
                data = numpy.frombuffer(f.read(), dtype="uint8")
        self.logger.debug(f"data => {data}")
        return data

import numpy
import os
from .logger import get_logger


class Generator:
    def __init__(self, store="binary", debug=False):
        self.store = store
        self.logger = get_logger(debug)

    def __call__(self, root, paths, settings={}):
        compression = settings.get("compression")
        output_group = settings.get("output_group")
        self.logger.info(f"compression => {compression}")
        for i, path in enumerate(paths):
            if not os.path.isfile(path):
                continue
            dataset_path = self._get_dataset_path(output_group, path)
            if root.get(dataset_path):
                self.logger.info(f"already exist => {dataset_path}")
            else:
                self.logger.info(
                    f"generate {self.store}: {path} => {root.filename}:{dataset_path}"
                )
                data = self.__getitem__(path)
                root.create_dataset(dataset_path, data=data, compression=compression)

    def __getitem__(self, path):
        with open(path, "rb") as f:
            if self.store == "binary":
                data = numpy.void(f.read())
            elif self.store == "numpy":
                data = numpy.frombuffer(f.read(), dtype="uint8")
        self.logger.debug(f"data => {data}")
        return data

    def _get_dataset_path(self, output_group, path):
        if output_group is None:
            return path
        basename = os.path.basename(path)
        return os.path.join(output_group, basename)

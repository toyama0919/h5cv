import numpy


class Generator:
    def __init__(self, store="binary", settings={}):
        self.store = store
        self.settings = settings

    def __call__(self, path):
        print(f"generate {self.store} => {path}")
        if self.store == "binary":
            return self._binary(path, self.settings)
        elif self.store == "numpy":
            return self._numpy(path, self.settings)

    def _binary(self, path, settings):
        with open(path, "rb") as f:
            data = numpy.void(f.read())
        return data

    def _numpy(self, path, settings):
        with open(path, "rb") as f:
            data = numpy.fromstring(f.read(), dtype="uint8")
        return data

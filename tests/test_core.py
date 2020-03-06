from h5cv.core import Core


class TestCore(object):
    def setup_method(self, method):
        self.core = Core(hdf5="tmp/test.h5")

    def teardown_method(self, method):
        pass

    def test_write(self):
        self.core.write("tests/data/*.jpg")

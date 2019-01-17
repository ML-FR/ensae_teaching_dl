"""
@brief      test log(time=25s)
"""

import sys
import os
import unittest
import warnings
from pyquickhelper.loghelper.flog import fLOG


try:
    import src
except ImportError:
    path = os.path.normpath(
        os.path.abspath(
            os.path.join(
                os.path.split(__file__)[0],
                "..",
                "..")))
    if path not in sys.path:
        sys.path.append(path)
    import src


class TestSkipExampleKerasMNIST(unittest.TestCase):

    def test_keras_logreg(self):
        fLOG(
            __file__,
            self._testMethodName,
            OutputPrint=__name__ == "__main__")

        try:
            from src.ensae_teaching_dl.examples.keras_mnist import keras_mnist_data, keras_build_mnist_model, keras_fit, keras_predict
        except SyntaxError as e:
            if sys.version_info[:2] == (3, 7):
                warnings.warn(
                    "Tensorflow still not available on python 3.7: {0}".format(e))
                return
            else:
                raise
        fLOG("data")
        (X_train, Y_train), (X_test, Y_test) = keras_mnist_data()
        fLOG("model", Y_train.shape)
        model = keras_build_mnist_model(Y_train.shape[1], fLOG=fLOG)
        fLOG("fit")
        if False and __name__ == "__main__":
            keras_fit(model, X_train, Y_train, X_test, Y_test, batch_size=1,  # 128 for a better accuracy
                      nb_classes=None, nb_epoch=1, fLOG=fLOG)
        else:
            # We make it shortest when run in unit test
            fLOG("quicker")
            N = 10
            X_train = X_train[:N, :]
            Y_train = Y_train[:N, :]
            X_test = X_test[:N, :]
            Y_test = Y_test[:N, :]
            keras_fit(model, X_train, Y_train, X_test, Y_test, batch_size=1,  # 128 for a better accuracy
                      nb_classes=None, nb_epoch=1, fLOG=fLOG)
        score = keras_predict(model, X_test, Y_test)
        r = score[:5]
        fLOG(r)


if __name__ == "__main__":
    unittest.main()

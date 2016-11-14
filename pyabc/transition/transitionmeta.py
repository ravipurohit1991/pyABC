from abc import ABCMeta

import numpy as np
import pandas as pd


def fit_wrap(self, X, w):
    if len(X.columns) == 0:
        self.no_parameters = True
        return
    self.no_parameters = False
    if w.size > 0:
        assert np.isclose(w.sum(), 1)
    self.fit_old(X, w)


def pdf_wrap(self, x):
    if self.no_parameters:
        return 1
    return self.pdf_old(x)


def rvs_wrap(self):
    if self.no_parameters:
        return pd.Series()
    return self.rvs_old()


class TransitionMeta(ABCMeta):
    """
    This metaclass handles the special case of no parameters.
    Transition classes do not have to check for it anymore
    """
    def __init__(cls, name, bases, attrs):
        ABCMeta.__init__(cls, name, bases, attrs)
        cls.fit_old = cls.fit
        cls.fit = fit_wrap

        cls.pdf_old = cls.pdf
        cls.pdf = pdf_wrap

        cls.rvs_old = cls.rvs
        cls.rvs = rvs_wrap
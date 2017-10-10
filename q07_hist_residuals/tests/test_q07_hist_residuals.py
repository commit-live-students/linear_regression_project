from unittest import TestCase
from ..build import hist_residuals
from unittest import TestCase
from inspect import getargspec


class TestHistResiduals(TestCase):
    def test_plot_residuals(self):

        # Input parameters tests
        args = getargspec(hist_residuals)
        self.assertEqual(len(args[0]), 2, "Expected argument(s) %d, Given %d" % (2, len(args[0])))
        self.assertEqual(args[3], (60,), "Expected default values do not match given default values")

        # Return type tests
        # Nothing to check here

        # Return value tests
        # Nothing to check here

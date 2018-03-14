from unittest import TestCase
from ..build import hist_residuals
from unittest import TestCase
from inspect import getfullargspec


class TestHistResiduals(TestCase):
    def test_hist_residuals_arguements(self):

        # Input parameters tests
        args = getfullargspec(hist_residuals)
        self.assertEqual(len(args[0]), 2, "Expected argument(s) %d, Given %d" % (2, len(args[0])))

    def test_hist_residuals_defaults(self):
        args = getfullargspec(hist_residuals)
        self.assertEqual(args[3], (60,), "Expected default values do not match given default values")

        # Return type tests
        # Nothing to check here

        # Return value tests
        # Nothing to check here

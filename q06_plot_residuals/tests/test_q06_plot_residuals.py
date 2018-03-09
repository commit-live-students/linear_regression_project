from ..build import plot_residuals
from unittest import TestCase
from inspect import getfullargspec
from unittest import TestCase

class TestPlotResiduals(TestCase):
    def test_plot_residuals_arguements(self):

        # Input parameters tests
        args = getfullargspec(plot_residuals)
        self.assertEqual(len(args[0]), 2, "Expected argument(s) %d, Given %d" % (2, len(args[0])))
    def test_plot_residuals_defaults(self):
        args = getfullargspec(plot_residuals)
        self.assertEqual(args[3], (None), "Expected default values do not match given default values")

        # Return type tests
        # Nothing to check here

        # Return value tests
        # Nothing to check here


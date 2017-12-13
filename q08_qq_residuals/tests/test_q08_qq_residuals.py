from unittest import TestCase
from ..build import qq_residuals
from unittest import TestCase
from inspect import getargspec


class TestQqResiduals(TestCase):
    def test_qq_residuals_arguements(self):

        # Input parameters tests
        args = getargspec(qq_residuals)
        self.assertEqual(len(args[0]), 1, "Expected argument(s) %d, Given %d" % (1, len(args[0])))
    def test_qq_residuals_defaults(self):
    	args = getargspec(qq_residuals)
        self.assertEqual(args[3], None, "Expected default values do not match given default values")

        # Return type tests
        # Nothing to check here

        # Return value tests
        # Nothing to check here

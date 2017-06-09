#!/usr/bin/python

"""Unit tests for the getuval function"""

#  standard library imports
import unittest


class GetUvalTest(object):
    """Test getuval and the output of functions called by it."""
    def getuval(self, argument):
        """Return a function named after given string."""
        function = 'do_{0}'.format(argument)
        function = getattr(self, function)
        return function()

    @staticmethod
    def do_hello():
        """Return 'hello world'"""
        return 'hello world'


class TestOutput(unittest.TestCase):
    """Test the output is equal to the expected output."""
    def test_hello(self):
        """Test the output of the do_hello function."""
        result = GetUvalTest().getuval('hello')
        self.assertEqual(result, 'hello world')


if __name__ == '__main__':
    unittest.main()

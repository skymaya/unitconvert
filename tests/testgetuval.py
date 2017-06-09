#!/usr/bin/python

class dummy(object):
    def getuval(self, argument):
        """Return a function to calculate the unit's value"""
        function = 'test_{0}'.format(argument)
        function = getattr(self, function)
        return function()

    def test_blah(self):
        return 'hello world'

print dummy().getuval('blah')

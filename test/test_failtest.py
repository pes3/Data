#Trigger a fail
import unittest
from unittest import TestCase

from code import add_numbers, sub_numbers

#passing in TestCast is what triggers the unit test loader
class failTest(TestCase):
    #has to start with test per unittest package
    def testfail(self):
        self.assertEqual(add_numbers(1,2), 7)
        #as we can see above, 1 plut 2 is not seven so it will fail


class SubtractNumbersTest(TestCase):
    def testSimple(self):
        self.assertEqual(sub_numbers(3, 2), 1)
        # as we can see above 3 subtract 2 is 1 so it will pass

if __name__ == "__main__":
    print("Run 'python -m unittest' to run these tests!")


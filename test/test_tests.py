
import unittest # built in 
from unittest import TestCase

from code import add_numbers, sub_numbers
#comes from my own code base

class AddNumbersTest(TestCase):
# unittest module works via class where you extend TestCase then create methods than actually test

    def setUp(self) -> None:
        print("I run at the beginning of every test for this AddNumbersTest class!")
#use it show an event was initilized , could also be used to make a fresh DB connection or other circumstances
#addl, a tear down method could be used as the end
#overiting setUp(TestCase had), but it did nothing prior 
    def testSimple(self):
        self.assertEqual(add_numbers(1, 2), 3)
#need test at beginning of method name
#if these two arguments are not the same, this test is failed
#self.assertEqual is critical to testcase class, it tests first and second are equal (takes two things to compare)
#assertEqual tells you values, gives more detail in error
#https://docs.python.org/3/library/unittest.html#basic-example
    def testLessSimple(self):
        self.assertEqual(add_numbers(1, add_numbers(2, 3)), 6)

# 1 plus 2 plus 3 should equal 6
class SubtractNumbersTest(TestCase):
    def testSimple(self):
        self.assertEqual(sub_numbers(3, 2), 1)

if __name__ == "__main__":
    print("Run 'python -m unittest' to run these tests!")
# reminder if you run file directly, do what is in the if statement, but if for example if you imported this it would not execute if statemen


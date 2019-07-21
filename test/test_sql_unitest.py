import unittest # built in 
from unittest import TestCase

from sqlunit import *

class AddNumbersTest(TestCase):

    def setUp(self) -> None:
        c = sqlite3.connect('test.db')
        #not needed for this script because connetion is already done
        #(cont..) placed for a reminder
    def test_row_count(self):#making sure inerting rows does what it should
        x = count_rows()
        insert_table('add','new','values')
        y = count_rows() # now count rows again after adding
        self.assertEquals(x,(y - 1))
        # make sure the difference is 1, if not the test will fail       
if __name__ == "__main__":
    print("Run 'python -m unittest' to run these tests!")

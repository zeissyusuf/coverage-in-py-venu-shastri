import string_calculator
import unittest
import typewise_alert

class TypeWiseTest(unittest.TestCase):
  def GivenEmptyStringZeroIsExpected(self):
    self.assertTrue(string_calculator.Add_Numbers("") == 0)
    
if __name__=='__main__':
  unittest.main()

import string_calculator
import unittest

class String_Calculator_Test(unittest.TestCase):
  def GivenEmptyStringZeroIsExpected(self):
    self.assertTrue(string_calculator.Add_Numbers("") == 0)
    
if __name__=='__main__':
  unittest.main()

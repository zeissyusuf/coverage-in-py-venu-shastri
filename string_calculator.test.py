import string_calculator
import unittest

def Add(strimg):
  pass



class String_Calculator_Test(unittest.TestCase):
  def GivenEmptyStringZeroIsExpected(self):
    self.assertTrue(string_calculator.Add("") == 0)
 
if __name__=='__main__':
  unittest.main()

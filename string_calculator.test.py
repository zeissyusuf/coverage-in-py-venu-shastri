import string_calculator
import typewise_alert

class TypeWiseTest(unittest.TestCase):
  def GivenEmptyStringZeroIsExpected(self):
    self.assertTrue(typewise_alert.Add_Numbers("") == 0)
    
if __name__=='__main__':
  unittest.main()

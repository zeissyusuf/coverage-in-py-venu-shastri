import string_calculator
import typewise_alert

class TypeWiseTest(unittest.TestCase):
  def GivenEmptyStringZeroIsExpected(self):
    self.assert(typewise_alert.Add("") == 0)
    
if __name__=='__main__':
  unittest.main()

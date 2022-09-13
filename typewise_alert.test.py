import unittest
import typewise_alert


class TypewiseTest(unittest.TestCase):
  def test_infers_breach_as_per_limits(self):
    self.assertTrue(typewise_alert.infer_breach(20, 50, 100) == 'TOO_LOW')
  def test_infers_breach_high(self):
     self.assertTrue(typewise_alert.infer_breach(120, 50, 100) == 'TOO_HIGH')
  def test_infers_breach_Normal(self):
    self.assertTrue(typewise_alert.infer_breach(60, 50, 100) == 'NORMAL')
  def test_check_and_aleart(self):
    typewise_alert.infer_breach(50, 50, 50)
  def test_check_and_aleart(self):
    typewise_alert.infer_breach(30, 30, 30)
  def test_check_temp(self):
    self.assertTrue(typewise_alert.classify_temperature_breach("PASSIVE_COOLING", 30)=="NORMAL")


if __name__ == '__main__':
  unittest.main()

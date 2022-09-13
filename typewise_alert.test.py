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
  def test_check_temp_Normal(self):
    self.assertTrue(typewise_alert.classify_temperature_breach("PASSIVE_COOLING", 30)=="NORMAL")
  def test_check_temp_Normal_High_1(self):
    self.assertTrue(typewise_alert.classify_temperature_breach("PASSIVE_COOLING", 40)=="TOO_HIGH")
  def test_check_temp_Normal_High_2(self):
    self.assertTrue(typewise_alert.classify_temperature_breach("PASSIVE_COOLING", -1)=="TOO_LOW")
  def test_check_temp_Normal_2(self):
    self.assertTrue(typewise_alert.classify_temperature_breach("HI_ACTIVE_COOLING", 30)=="NORMAL")
  def test_check_temp_Normal_High_3(self):
    self.assertTrue(typewise_alert.classify_temperature_breach("HI_ACTIVE_COOLING", 50)=="TOO_HIGH")
  def test_check_temp_Normal_High_4(self):
    self.assertTrue(typewise_alert.classify_temperature_breach("HI_ACTIVE_COOLING", -30)=="TOO_LOW")
  def test_check_temp_Normal_5(self):
    self.assertTrue(typewise_alert.classify_temperature_breach("MED_ACTIVE_COOLING", 40)=="NORMAL")
  def test_check_temp_Normal_High_6(self):
    self.assertTrue(typewise_alert.classify_temperature_breach("MED_ACTIVE_COOLING", 47)=="TOO_HIGH")
  def test_check_temp_Normal_High_7(self):
    self.assertTrue(typewise_alert.classify_temperature_breach("MED_ACTIVE_COOLING", -40)=="TOO_LOW")
  def test_check_temp_Normal_High_8(self):
    self.assertTrue(typewise_alert.check_and_alert(alertTarget, "PASSIVE_COOLING", 30)=="")


    

if __name__ == '__main__':
  unittest.main()

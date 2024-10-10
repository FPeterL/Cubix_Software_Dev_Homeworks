import unittest
from BMILib import calc

class TestBMICalc(unittest.TestCase):

    def test_bmi_int_magassággal(self):
        eredmény = calc(súly = 70, magasság = 170)
        self.assertAlmostEqual(24.22,eredmény , places=2)

    def test_bmi_with_float_magassággal(self):
        eredmény = calc(súly = 70, magasság=1.7)
        self.assertAlmostEqual(24.22, eredmény,places=2)

    def test_bmi_with_float_súllyal(self):
        eredmény = calc(súly=65.7, magasság=170)
        self.assertAlmostEqual(22.73, eredmény,places=2)
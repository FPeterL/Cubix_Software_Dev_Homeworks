import unittest
from BMILib import calc
import pytest

class TestBMICalc(unittest.TestCase):

    def test_bmi_int_magassággal(self):
        result = calc(weight = 70, height = 170)
        self.assertAlmostEqual(24.22,result , places=2)

    def test_bmi_with_float_magassággal(self):
        result = calc(weight = 70, height=1.7)
        self.assertAlmostEqual(24.22, result,places=2)

    def test_bmi_with_float_súllyal(self):
        result = calc(weight=65.7, height=170)
        self.assertAlmostEqual(22.73, result,places=2)
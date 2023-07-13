import unittest
import physics


class TestPhysics(unittest.TestCase):
    def test_bouyancy(self):
        self.assertEquals(physics.calculate_bouyancy(1, 1000), 9810)
        self.assertNotEquals(physics.calculate_bouyancy(1, 20), 5.9812)
        self.assertRaises(ValueError, lambda: physics.calculate_bouyancy(-1, -1))

    def test_float(self):
        self.assertEquals(physics.will_it_float(2, 1000), True)
        self.assertNotEquals(physics.will_it_float(3, 5), False)
        self.assertRaises(ValueError, lambda: physics.will_it_float(-1, 1))

    def test_pressure(self):
        self.assertEquals(physics.calculate_pressure(1000), 9810000)
        self.assertNotEquals(physics.calculate_pressure(9810), 5)

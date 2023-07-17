import math
import unittest

import numpy
import physics


class TestPhysics(unittest.TestCase):
    def test_bouyancy(self):
        self.assertEquals(physics.calculate_bouyancy(1, 1000), 9810)
        self.assertNotEquals(physics.calculate_bouyancy(1, 20), 5.9812)
        self.assertRaises(ValueError, lambda: physics.calculate_bouyancy(-1, -1))

    def test_float(self):
        self.assertEquals(physics.will_it_float(2, 1000), True)
        self.assertNotEquals(physics.will_it_float(3, 5), False)
        self.assertEquals(physics.will_it_float(1, 1000), None)
        self.assertRaises(ValueError, lambda: physics.will_it_float(-1, 1))

    def test_pressure(self):
        self.assertEquals(physics.calculate_pressure(1000), 9810000 + 101.325)
        self.assertNotEquals(physics.calculate_pressure(9810), 5)

    def test_calculate_acceleration(self):
        self.assertEquals(physics.calculate_acceleration(10, 5), 2)
        self.assertNotEquals(physics.calculate_acceleration(5, 3), 4)

    def test_calculate_angular_acceleration(self):
        self.assertEquals(physics.calculate_angular_acceleration(4, 4), 1)
        self.assertNotEquals(physics.calculate_angular_acceleration(3, 2), 4)

    def test_calculate_torque(self):
        self.assertEquals(physics.calculate_torque(5, 0, 5), 0)
        self.assertNotEquals(physics.calculate_torque(4, 30, 5), 4)

    def test_calculate_moment_of_inertia(self):
        self.assertEquals(physics.calculate_moment_of_inertia(2, 2), 8)
        self.assertNotEquals(physics.calculate_moment_of_inertia(3, 2), 3)

    def test_calculate_auv_acceleration(self):
        numpy.testing.assert_array_equal(
            physics.calculate_auv_acceleration(0, math.pi / 4),
            numpy.array([[0.0], [0.0]]),
        )

    def test_calculate_auv_angular_acceleration(self):
        self.assertAlmostEquals(physics.calculate_auv_angular_acceleration(100, 30), 25)
        self.assertNotEquals(physics.calculate_auv_angular_acceleration(100, 30), 5)

    def test_calculate_auv2_acceleration(self):
        numpy.testing.assert_array_equal(
            physics.calculate_auv2_acceleration(
                numpy.array([0, 0, 0, 0]), math.pi / 6, math.pi / 4
            ),
            numpy.array([[0.0], [0.0]]),
        )

    def test_calculate_auv2_angular_acceleration(self):
        self.assertAlmostEquals(
            physics.calculate_auv2_angular_acceleration(
                numpy.array([100, 100, 0, 0]), 0, 3, 4
            ),
            0,
        )
        self.assertNotEquals(
            physics.calculate_auv2_angular_acceleration(
                numpy.array([100, 100, 100, 0]), 0, 3, 4
            ),
            5,
        )

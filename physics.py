import math
import numpy


d_water = 1000  # density of water -> 1 m^3 = 1000kg
g = 9.81  # acceleration due to gravity (m/s^2)
pressure_at_surface = 101.325  # 1atm // 101.325 KPa


def calculate_bouyancy(v, density_fluid):
    """
    calculates the bouyancy of an object in any given fluid density
    units: newtons"""
    if v <= 0 or density_fluid <= 0:
        raise ValueError("Volume and fluid density must both be positive!")
    return density_fluid * g * v


def will_it_float(v, mass):
    """calculates if an object with a given volume and mass will float or not in water
    true/false"""
    if v <= 0 or mass <= 0:
        raise ValueError("Volume and mass must both be positive!")
    if (calculate_bouyancy(v, d_water) - (g * mass)) == 0:
        return None
    return (calculate_bouyancy(v, d_water) - (g * mass)) > 0


def calculate_pressure(depth):
    """
    calculates the pressure at any given depth in water.
    units: pascals"""
    depth = abs(depth)
    return depth * g * d_water + pressure_at_surface


def calculate_acceleration(F, m):
    "calculates the acceleration of an object given the force applied on it and its mass"
    return F / m


def calculate_angular_acceleration(tau, i):
    "calcualtes the angular acceleration of an object gfiven the force applied on it and its mass"
    return tau / i


def calculate_torque(F_magnitude, F_direction, r):
    # calculates torque given the force vector and r
    return r * (F_magnitude * math.sin(F_direction * math.pi / 180))


def calculate_moment_of_inertia(m, r):
    # calculate the moment of intertia given the distance to CoM and the mass of the object
    return m * math.pow(r, 2)


def rotation_arr(theta):
    arr = numpy.array(
        [
            [(math.cos(theta), -math.sin(theta))],
            [(math.sin(theta), math.cos(theta))],
        ]
    )
    return arr


def rov_arr(theta):
    arr = numpy.array(
        [
            [
                math.cos(theta),
                math.cos(theta),
                -math.cos(theta),
                -math.cos(theta),
            ],
            [
                math.sin(theta),
                -math.sin(theta),
                -math.sin(theta),
                math.sin(theta),
            ],
        ]
    )

    return arr


def calculate_auv_acceleration(
    F_magnitude, F_angle, thruster_distance=0.5, mass=100, volume=0.1
):
    thrusters = numpy.array(
        [[F_magnitude], [F_magnitude], [F_magnitude], [F_magnitude]]
    )
    rov_rot_arr = rov_arr(F_angle)
    forcearr = numpy.dot(rov_rot_arr, thrusters)
    accl = numpy.array([forcearr[0] / mass, forcearr[1] / mass])
    print(thrusters)
    print(rov_rot_arr)
    print(forcearr)
    print(accl)


calculate_auv_acceleration(1000, (math.pi / 6))

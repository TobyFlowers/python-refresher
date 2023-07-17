import math
import numpy


d_water = 1000  # density of water -> 1 m^3 = 1000kg
g = 9.81  # acceleration due to gravity (m/s^2)
pressure_at_surface = 101.325  # 1atm // 101.325 KPa


def rotation_arr(theta):
    # return array for global rotation array
    arr = numpy.array(
        [
            [(math.cos(theta), -math.sin(theta))],
            [(math.sin(theta), math.cos(theta))],
        ]
    )
    return arr


def rov_arr(theta):
    # return array for ROV-centric rotation array
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
    """calcualtes the angular acceleration of an object gfiven the force applied on it and its mass"""
    return tau / i


def calculate_torque(F_magnitude, F_direction, r):
    """calculates torque given the force vector and r"""
    return r * (F_magnitude * math.sin(F_direction * math.pi / 180))


def calculate_moment_of_inertia(m, r):
    """calculate the moment of intertia given the distance to CoM and the mass of the object"""
    return m * math.pow(r, 2)


def calculate_auv_acceleration(
    F_magnitude, F_angle, thruster_distance=0.5, mass=100, volume=0.1
):
    """calc the acceleration of a one-thruster robot in robot-centric space"""
    thrusters = numpy.array([[-F_magnitude]])
    rov_rot_arr = numpy.array([[math.cos(F_angle)], [math.sin(F_angle)]])
    forcearr = numpy.matmul(rov_rot_arr, thrusters)
    accl = numpy.array([forcearr[0] / mass, forcearr[1] / mass])
    return accl


def calculate_auv_angular_acceleration(
    F_magnitude, F_angle, intertia=1, thruster_distance=0.5
):
    """calc the acceleration of a one-thruster robot"""
    return calculate_torque(F_magnitude, F_angle, thruster_distance) / intertia


def calculate_auv2_acceleration(T, alpha, theta, mass=100):
    """calc the acceleration of a 4-thruster robot"""

    rov_rot_arr = rov_arr(alpha)
    forcearr = numpy.matmul(rov_rot_arr, T)
    accl = numpy.array([forcearr[0] / mass, forcearr[1] / mass])
    return numpy.matmul(rotation_arr(theta), accl)


def calculate_auv2_angular_acceleration(T, alpha, L, l, inertia=100):
    """calc the  ang acceleration of a 4-thruster robot"""
    beta = numpy.arctan(l / L)
    rov_rot_arr = rov_arr(alpha + beta)
    forcearr = numpy.matmul(rov_rot_arr, T)
    accl = numpy.array([forcearr[0] / inertia, forcearr[1] / inertia])
    r = math.sqrt(math.pow(L, 2) + math.pow(l, 2))
    magnitude = math.sqrt(accl[0] * accl[0] * accl[1] + accl[1])
    return calculate_torque(magnitude, alpha, r) / inertia


def simulate_auv2_motion(
    T, alpha, L, l, inertia=100, dt=0.1, t_final=10, x0=0, y0=0, theta0=0, mass=100
):
    # numpy.zeros(shape=(len(time), 2))
    time = numpy.arange(0, t_final, dt)
    linearAcceleration = numpy.zeros(shape=(len(time), 2))
    angularAcceleration = numpy.zeros_like(time)
    linearVelocity = numpy.zeros(shape=(len(time), 2))
    angularVelocity = numpy.zeros_like(time)
    linearDisplacementX = numpy.zeros_like(time)
    linearDisplacementY = numpy.zeros_like(time)
    angularDisplacement = numpy.zeros_like(time)
    theta = theta0
    l_velocity = numpy.zeros(shape=(len(time), 2))
    a_velocity = 0
    angularDisplacement[0] = theta0
    linearDisplacementX[0] = x0
    linearDisplacementY[0] = y0
    theta = theta0

    for i in range(1, len(time)):
        # CALCULATING ACCELERATION MATRICIES
        laccel = calculate_auv2_acceleration(T, alpha, theta, mass)
        aaccel = calculate_auv2_angular_acceleration(T, alpha, L, l, inertia)
        linearAcceleration[i] = laccel.T
        angularAcceleration[i] = aaccel

        # CALCULATING VELOCITY MATRICES

        l_velocity = numpy.array(
            [
                [linearAcceleration[i - 1][0] + linearAcceleration[i][0] * dt],
                [linearAcceleration[i - 1][0] + linearAcceleration[i][1] * dt],
            ]
        )
        a_velocity = a_velocity + (angularAcceleration[i]) * dt

        linearVelocity[i] = l_velocity.T
        angularVelocity[i] = a_velocity

        # CALCULATING POSITION MATRICIES
        linearDisplacementX[i] = (
            0.5 * laccel[0] * math.pow(dt, 2) + linearDisplacementX[i - 1] * time[i]
        )
        linearDisplacementY[i] = (
            0.5 * laccel[1] * math.pow(dt, 2) + linearDisplacementY[i - 1] * time[i]
        )
        angularDisplacement[i] = (
            0.5 * aaccel * math.pow(dt, 2) + angularDisplacement[i - 1] * time[i]
        )

    return (
        time,
        linearDisplacementX,
        linearDisplacementY,
        angularDisplacement,
        linearVelocity,
        angularVelocity,
        linearAcceleration,
    )


print(simulate_auv2_motion(numpy.array([0, 0, 0, 0]), math.pi / 4, 3, 4))

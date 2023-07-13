d_water = 1000  # density of water -> 1 m^3 = 1000kg
g = 9.81  # acceleration due to gravity (m/s^2)


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
    return depth * g * d_water

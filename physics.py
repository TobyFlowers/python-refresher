d_water = 1000
g = 9.81


# calculates the bouyancy of an object in any given fluid density
# units: newtons
def calculate_bouyancy(v, density_fluid):
    if v <= 0 or density_fluid <= 0:
        raise ValueError("Volume and fluid density must both be positive!")
    return density_fluid * g * v


# calculates if an object with a given volume and mass will float or not in water
# true/false
def will_it_float(v, mass):
    if v <= 0 or mass <= 0:
        raise ValueError("Volume and mass must both be positive!")
    return (calculate_bouyancy(v, d_water) - (g * mass)) >= 0


# calculates the pressure at any given depth in water.
# units: pascals
def calculate_pressure(depth):
    depth = abs(depth)
    return depth * g * d_water

# calculates the bouyancy of an object in any given fluid
def calculate_bouyancy(v, density_fluid):
    return density_fluid * 9.81 * v


# calculates if an object with a given volume and mass will float or not in water
def will_it_float(v, mass):
    return (calculate_bouyancy(v, 1000) - (9.81 * mass)) > 0


# calculates the pressure at any given depth in water.
def calculate_pressure(depth):
    return depth * 9.81 * 1000

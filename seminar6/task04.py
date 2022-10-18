def find_farthest_orbit(orbits):
    return  max(orbits, key=lambda x: 3.14 * x[0] * x[1] if (x[0] != x[1]) else False)

orbits = [(1, 7), (2.5, 111), (7, 4), (5, 6), (7, 3)]
print(find_farthest_orbit(orbits))
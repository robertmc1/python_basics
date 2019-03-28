from space.planet import Planet
from space.calc import planet_mass, planet_vol

nabboo = Planet('Nabboo', 3300000, 8, 'Nabboo system')

nabboo_mass = planet_mass(nabboo.gravity, nabboo.radius)
nabboo_vol = planet_vol(nabboo.radius)

print(f'{nabboo.name} has a mass of {nabboo_mass} and a volume of {nabboo_vol}')







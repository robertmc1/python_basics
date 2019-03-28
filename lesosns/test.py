from clasees import Planet

#hoth = Planet('Hoth', 200000, 5.5, 'Hoth System')
#print(f'Name is: {hoth.name}')
#print(f'Radius is: {hoth.radius}')
#print(f'The gravity is: {hoth.gravity}')
#print(hoth.orbit())

nabboo = Planet('Nabboo', 3300000, 8, 'Nabboo system')
print(f'Name: {nabboo.name}')
print(f'Radius: {nabboo.radius}')
print(f'Gravity: {nabboo.gravity}')
print(nabboo.orbit())
print(Planet.shape)
print(nabboo.shape)

#Este no funciona
#print(Planet.orbit())

#Este funciona porque es el @
#print(Planet.commons())

#Este funciona y ademas modifica el string
print(Planet.spin('a vary high speed'))
def ninja_intro(dictionary):
    for key, val in dictionary.items():
        print(f'I am {key} and I am a {val} belt.')

ninja_belts = {}

while True:
    ninja_name = input('Enter a ninja name:')
    ninja_belt = input('Enter a belt color')
    ninja_belts[ninja_name] = ninja_belt

    another = input('add another? (y/n)')
    if another == 'y':
        continue
    else:   
        break

ninja_intro(ninja_belts)







#--------------Diccionarios---------
#ninjas_belt = {"Cristal":"red", "Pepe": "Black"}
#
#Para saber si esta una en concreto
#	python
#	"Robert" in ninjas_belt
#
#para ver todas als palabras
#	python
#	ninjas_belt.keys()
#
#para pasarlo a una lista
#	python
#	list(ninjas_belt.Keys())
#
#para los VALORES
#	python	
#	ninjas_belt.valuers()
#
#para pasarlo a una lsita
#	python
#	vals = list(ninjas_belt.values())
#
#CONTAR cuantas veces esta un valor
#	python
#	vals.count('blavk')
#
#Insertar uno nuevo
#	py
#	ninjas_belt['yoshi']= "brown"
#
#crear objeto
#	py
#	person = dict('name': "Robert", 'age': 23, 'height': 1.83)
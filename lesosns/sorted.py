def belt_count(dictionary):
    belts = list(dictionary.values())
    for belt in set(belts):
        num = belts.count(belt)
        print(f'There are {num} {belt} belts.')

ninja_belts = {}

while True:
    ninja_name = input('Enter a ninja name: ')
    ninja_belt = input('Enter a belt color: ')
    ninja_belts[ninja_name] = ninja_belt

    another = input('add another? (y/n)')
    if another == 'y':
        continue
    else:   
        break

belt_count(ninja_belts)


#------------Ordenar listas SHEET----------------
#
#nums = [1,3,2,8,5,6,4,9,7,2,1]
#names = ["Robert", "Ramona", "Peter","Ana"]
#
#para ordenar: 
#	sorted(nums)
#	sorted(names) (Si hay mayusculas y minusculas primero ordena de A-Z y despues las 
#	minusculas de a-z)
#
#para ordenr sin repetir
#	set(nums)
#
#--------con objetos-----
#ninjas = {"Robert": black, "Pedro": "white"}
#
#imprimir valores
#	ninjas.values()
#imprimir valores sin repetir
#	set(ninjas.values())


grades = ['A', 'B', 'F','C','F','A']

def remove_f(grade):
    return grade != 'F'

#-------1º Forma-----------------------
#filter(testing_funcition, grades)

print(list(filter(remove_f, grades)))

#------filter con FOR-------------------
filtered_grades = []

for grade in grades:
    if grade != 'F':
        filtered_grades.append(grade)
print(filtered_grades)

#-------Filter Comprenhension------------

print([grade for grade in grades if grade != 'F'])





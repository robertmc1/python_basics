my_name = 'Robert'

def print_name():
    global my_name
    my_name='Tom'
    print('The name inside the funcrion is', my_name)

print_name()

print('Outside the function the name is', my_name)
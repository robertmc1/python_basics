
def ehem_decorator(func):

    def func_wrapper():
        #code before function
        print('*ehem*')
        #fire the function
        func()
        #code after function
        print('*ejem*')

    return func_wrapper

@ehem_decorator
def question():
    print('Podías traerme la cuenta?')
question()

@ehem_decorator
def answer():
    print('Enseguida caballero')
answer()

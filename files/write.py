with open ('write.txt','w') as write_file:
    write_file.write('Hola Robert. Buen Trabajo!')
    write_file.write('\nI love you so much!')

#a es amend (adjuntar) y w es para Write
with open ('write.txt','a') as write_file:
    write_file.write('\nCould it be?')

quotes =[
    '\nI love you so much!',
    '\nCouse',
    '\nYou are awsome!'
]

with open ('write.txt','a') as write_file:
    write_file.writelines(quotes)
    
with open ('write.txt','a') as write_file:
    write_file.write(input('How are you?'))
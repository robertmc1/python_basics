from random import randint

ninja_words = [
    'Aiki', 'Buyu', 'Chimonjutsu', 'Cho sen', 'Dojo', 'Gakusei', 'Haiboku',
    'Jin', 'Kenshi', 'Obake ken', 'Rakusha', 'Sanmaru', 'Tekkon', 'Yoko'
]

def ninjarize(word):
    random_pos = randint(0, len(ninja_words) - 1)
    return f'{word} {ninja_words[random_pos]}'

paragraphs = int(input('How many paragraphs of robert_ipum do you wont?'))


with open ('ipsum.txt') as ipsum_original:
    items = ipsum_original.read().split()    

    for n in range(paragraphs):
        ninja_text = list(map(ninjarize, items))
        with open ('robert_ipsum.txt','a') as robert_ipsum:
            robert_ipsum.write(''.join(ninja_text)+ '\n\n')
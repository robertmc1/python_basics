
from random import shuffle

def jumble(word):
    anagram = list(word) 
    shuffle(anagram)
    return ''.join(anagram) 

words = ['potatoes', 'tomatoes', 'bananas']
anagrams = []

#for word in words:
#    anagrams.append(jumble(word))
#print(anagrams)

#print(list(map(jumble, words)))

#Hecho con comprenhension

print([jumble(word) for word in words])


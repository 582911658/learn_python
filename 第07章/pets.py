pets = ['dog', 'cat', 'dog', 'goldfish', 'rabbit', 'cat']
print(pets)
while 'cat' in pets:
    pets.remove('cat')
    break
while 'dog' in pets:
    pets.remove('dog')
    break
print(pets)

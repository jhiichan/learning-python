# Dictionaries

# creating dictionaries with curly braces
character = {
    'name': 'Tifa Lockhart',
    'birthdate': 'May 3',
    'weapon': 'Knuckles',
    'home': 'Nibelheim'
}

# accessing items in dictionary
print(character['name'])
print(character.get('home'))

# getting keys
print(character.keys())

# updating values
character['birthdate'] = 'May 3, 1987'

# adding item
character['ultimate'] = 'Final Heaven'

# removing item
del character['weapon']

# nested types
character['weapons'] = [
    {
        'name': 'Knuckles',
        'damage': 100
    },
    {
        'name': 'Premium Heart',
        'damage': 1000
    }
]
print(character)
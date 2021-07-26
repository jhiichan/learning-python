from typing import List


my_shows = {
    0: {
        'title': 'The Avengers',
        'director': 'Joss Whedon',
        'cast': ['Robert Downey Jr.', 'Chris Evans', 'Chris Hemsworth'],
        'type': 'movie'
    },
    1: {
        'title': 'Rurouni Kenshin Part I: Origins',
        'director': 'Keishi Ohtomo',
        'cast': ['Takeru Satoh', 'Emi Takei'],
        'type': 'movie'
    },
    2: {
        'title': 'Modern Family',
        'director': '',
        'cast': ['Ed O\'Neill', 'Sofía Vergara', 'Julie Bowen' ,'Ty Burrell'],
        'type': 'series'
    }
}

# print(my_shows)
keyword ='Julie Bowen'
result = {}
for key, value in my_shows.items():
    show = list(value.values())
    if keyword in show:
        result[key] = my_shows[key]
    elif keyword in value['cast']:
        result[key] = my_shows[key]

print(result)
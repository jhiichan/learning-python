from flask import (
    Blueprint
)

bp = Blueprint('show', __name__, url_prefix='/show')

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

@bp.route('/', methods=('GET',))
def index():
    return my_shows

@bp.route('/<int:id>', methods=('GET',))
def get_by_id(id):
    return my_shows[id]

@bp.route('/search/<string:keyword>', methods=('GET',))
def search(keyword):
    result = {}
    for key, value in my_shows.items():
        show = list(value.values())
        if keyword in show:
            result[key] = my_shows[key]

    return result
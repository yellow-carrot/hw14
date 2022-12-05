from utils import *
from flask import Flask, jsonify

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True


@app.route('/movie/<title>')
def page_search_by_title(title):
    return search_by_title(title)


@app.route('/movie/<start_year>/to/<end_year>')
def page_search_by_years(start_year, end_year):
    return jsonify(search_between_years(start_year, end_year))


@app.route('/movie/rating/<rating>')
def page_search_by_rating(rating):
    if rating == 'children':
        result = rating_children()
    elif rating == 'family':
        result = rating_family()
    elif rating == 'adult':
        result = rating_adult()
    else:
        result = None
    return jsonify(result)


@app.route('/genre/<genre>')
def page_search_by_genre(genre):
    return jsonify(search_by_genre(genre))


if __name__ == '__main__':
    app.run()
#
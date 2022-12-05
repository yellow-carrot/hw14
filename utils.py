import sqlite3


def search_by_title(title):
    with sqlite3.connect('netflix.db') as connection:

        cursor = connection.cursor()

        cursor.execute(f"""
                SELECT title, country, release_year, listed_in, description
                FROM netflix
                WHERE title LIKE '%{title}%'
                ORDER BY release_year DESC
                        """)

        data = cursor.fetchone()

        film = {
            'title': data[0],
            'country': data[1],
            'release_year': data[2],
            'genre':data[3],
            'description': data[4]
        }

        return film


def search_between_years(start_year, end_year):
    with sqlite3.connect('netflix.db') as connection:
        cursor = connection.cursor()

        cursor.execute(f"""
                SELECT title, release_year
                FROM netflix
                WHERE release_year BETWEEN {start_year} AND {end_year}
                ORDER BY release_year DESC
                LIMIT 100
        """)

        data = cursor.fetchall()

        films_list = []

        for item in data:

            film = {
                'title': item[0],
                'release_year': item[1]
            }

            films_list.append(film)

        return films_list


def rating_children():
    with sqlite3.connect('netflix.db') as connection:

        cursor = connection.cursor()

        cursor.execute(f"""
                SELECT title, rating, description
                FROM netflix
                WHERE rating = 'G'
                LIMIT 100
        """)

        data = cursor.fetchall()

        films_list = []

        for item in data:
            film = {
                'title': item[0],
                'rating': item[1],
                'description': item[2]
            }

            films_list.append(film)

        return films_list


def rating_family():
    with sqlite3.connect('netflix.db') as connection:

        cursor = connection.cursor()

        cursor.execute( f"""
                SELECT title, rating, description
                FROM netflix
                WHERE rating IN ('G','PG','PG-13')
                LIMIT 100               
        """)

        data = cursor.fetchall()

        films_list = []

        for item in data:
            film = {
                'title': item[0],
                'rating': item[1],
                'description': item[2]
            }

            films_list.append(film)

        return films_list


def rating_adult():
    with sqlite3.connect('netflix.db') as connection:

        cursor = connection.cursor()

        cursor.execute(f"""
                SELECT title, rating, description
                FROM netflix
                WHERE rating IN ('G','PG','PG-13', 'R', NC-17)
                LIMIT 100
        """)

        data = cursor.fetchall()

        films_list = []

        for item in data:
            film = {
                'title': item[0],
                'rating': item[1],
                'description': item[2]
            }

            films_list.append(film)

        return films_list


def search_by_genre(genre):
    with sqlite3.connect('netflix.db') as connection:

        cursor = connection.cursor()

        cursor.execute(f"""
                SELECT title, description
                FROM netflix
                WHERE listed_in LIKE '%{genre}%'
                ORDER BY release_year
                LIMIT 10
        """)

        data = cursor.fetchall()

        films_list = []

        for item in data:
            film = {
                'title': item[0],
                'description': item[1]
            }

            films_list.append(film)

        return films_list


def search_by_actors(actor_1, actor_2):
    with sqlite3.connect('netflix.db') as connection:

        cursor = connection.cursor()


        cursor.execute(f"""
                SELECT count(netflix.cast), netflix.cast
                FROM netflix
                WHERE netflix.cast LIKE '%{actor_1}%' AND netflix.cast LIKE '%{actor_2}%'
                GROUP BY netflix.cast
        """)

        return cursor.fetchall()


def find_movie(type, release_year, genre):
    cursor = connection.cursor()

    cursor.execute(f"""
                SELECT title, description, release_year
                FROM netflix
                WHERE type = 'type' AND release_year = release_year AND listed_in LIKE '%{genre}%'
                GROUP BY netflix.cast
           """)

    return cursor.fetchall()

#
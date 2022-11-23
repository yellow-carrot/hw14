import sqlite3



with sqlite3.connect('netflix.db') as connection:
    cursor = connection.cursor()

    query = """
            SELECT title, country, release_year, listed_in, description
            FROM netflix
            ORDER BY release_year

    """

    cursor.execute(query)
    movies_list = cursor.fetchall()

print(movies_list)

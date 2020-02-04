def create_restaurants_table(db_connection):
    """
    This creates a table to store restaurants in.
    Caution this will delete the existing restaurant table.

    Arguments
    =========
    - db_connection - database connection to an SQLite3 database
    """
    cursor = db_connection.cursor()
    cursor.execute('DROP TABLE IF EXISTS restaurants')
    cursor.execute('''CREATE TABLE restaurants
        (name text, xpos real, ypos real)''')
    db_connection.commit()


def add_restaurant(db_connection, name, xpos, ypos):
    """
    This adds a restaurant to the restaurants table.

    Arguments
    =========
    - db_connection - database connection to an SQLite3 database
    - name - name of the database
    - xpos - position on the x axis
    - ypos - position on the y axis
    """
    cursor = db_connection.cursor()
    cursor.execute('INSERT INTO restaurants VALUES (?,?,?)',
                   name, xpos, ypos)
    db_connection.commit()

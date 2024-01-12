#!/usr/bin/python3
"""Takes the name of a state as an argument and
lists all cities of that state
"""

if __name__ == '__main__':
    import MySQLdb
    from sys import argv

    db = MySQLdb.connect(host='localhost', user=argv[1], passwd=argv[2],
                         db=argv[3], port=3306)
    cur = db.cursor()
    cur.execute("""
                SELECT name
                FROM cities
                WHERE state_id = (
                    SELECT id
                    FROM states
                    WHERE name = %(name_search)s)
                ORDER BY cities.id
                """, {
                    'name_search': argv[4]
                })
    rows = cur.fetchall()
    if rows is not None:
        print(", ".join([row[0] for row in rows]))

    cur.close()
    db.close()

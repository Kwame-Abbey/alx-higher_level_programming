#!/usr/bin/python3
"""Displays all values in the states table where
name matches the argument
"""

if __name__ == '__main__':
    import MySQLdb
    from sys import argv

    name_search = argv[4]

    db = MySQLdb.connect(host='localhost', user=argv[1], passwd=argv[2],
                         db=argv[3], port=3306)

    cur = db.cursor()
    cur.execute("SELECT * FROM states \
                WHERE name LIKE BINARY '{}' \
                ORDER BY states.id ASC".format(name_search))
    rows = cur.fetchall()
    for row in rows:
        print(row)

    cur.close()
    db.close()

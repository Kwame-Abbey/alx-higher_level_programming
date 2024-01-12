#!/usr/bin/python3
"""Displays all values in the states table where
name matches the argument and safe from MySQL injection
"""

if __name__ == '__main__':
    import MySQLdb
    from sys import argv

    name_search = argv[4]

    db = MySQLdb.connect(host='localhost', user=argv[1], passwd=argv[2],
                         db=argv[3], port=3306)

    cur = db.cursor()
    cur.execute("""SELECT * FROM states \
                WHERE name = %(name_search)s \
                ORDER BY states.id ASC
                """, {
                    'name_search': name_search
                })
    rows = cur.fetchall()
    for row in rows:
        print(row)

    cur.close()
    db.close()

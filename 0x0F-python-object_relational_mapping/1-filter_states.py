#!/usr/bin/python3
"""Lists all states with a name starting with upper 'N'"""

if __name__ == '__main__':
    import MySQLdb
    from sys import argv

    db = MySQLdb.connect(host='localhost', user=argv[1], passwd=argv[2],
                         db=argv[3], port=3306)

    cur = db.cursor()
    cur.execute("SELECT id, name FROM states WHERE states.name REGEXP '^N'")
    rows = cur.fetchall()

    for row in rows:
        print(row)

    cur.close()
    db.close()

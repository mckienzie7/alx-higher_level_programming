#!/usr/bin/python3
"""List cities by states"""
import MySQLdb
import sys

if __name__ == "__main__":
    db = MySQLdb.connect(
            user=sys.argv[1],
            passwd=sys.argv[2],
            db=sys.argv[3],
            port=3306
            )
    cur = db.cursor()
    cur.execute(
            """
            SELECT c.id, c.name, s.name
            FROM cities AS c
            INNER JOIN states as s
            ON c.state_id = s.id
            """
            )
    rows = cur.fetchall()
    for row in rows:
        print("{}".format(row))

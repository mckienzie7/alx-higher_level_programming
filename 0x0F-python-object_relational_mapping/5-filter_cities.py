#!/usr/bin/python3
"""State name as argument name cities of the state"""
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
            SELECT c.name
            FROM cities AS c
            INNER JOIN states as s
            ON c.state_id = s.id
            WHERE s.name = %s
            """,
            (sys.argv[4], )
            )
    rows = cur.fetchall()
    city_list = []
    for row in rows:
        if row[0] not in city_list:
            city_list.append(row[0])
    ls = ", ".join(city_list)
    print(ls)

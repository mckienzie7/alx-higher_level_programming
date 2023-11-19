#!/usr/bin/python3
"""List state if name is given using safer way"""
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
    cur.execute("SELECT * FROM states WHERE name = %s", (sys.argv[4], ))
    rows = cur.fetchall()
    for row in rows:
        print("{}".format(row))

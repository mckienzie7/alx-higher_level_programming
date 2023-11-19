#!/usr/bin/python3
"""List all states from database"""
import sys
import MySQLdb

if __name__ == "__main__":
    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    c = db.cursor()
    c.execute("SELECT * FROM `states`")
    for state in c.fetchall():
        print("{}".format(state))

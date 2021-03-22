import sqlite3 as sql

db = sql.connect('dtb.db')
cur = db.cursor()

print("Welcome to our store. You can buy credits there.")

print("""
Prices:
1 credit = 1 ¢

""")

cur.execute("SELECT credit FROM credits")

beforeCredits = cur.fetchall()[0][0]

request = int(input("How many credits you want to buy?"))

cur.execute(f"UPDATE credits SET credit = {beforeCredits+request}")

db.commit()
db.close()
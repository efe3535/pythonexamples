#/usr/bin/python3
#Python roulette game.
#Wrotten by github.com/efe3535

from random import choice as c
import sqlite3 as sql
from time import sleep

db = sql.connect('dtb.db')

crs = db.cursor()

print("""
Python Roulette Game
Options:
Red or Black

Rules:
You have %50 change of winning.

Good Luck!
""")

crs.execute("CREATE TABLE IF NOT EXISTS credits (username,credit)")

crs.execute("SELECT * FROM credits")

rows = crs.fetchall()

possibilities = ["red","black"]

while True:
    bet = input("Enter Your Bet\n\n").lower()

    if bet in possibilities:

        print("Ok, so your bet is ", bet)
        print("Rollin' roulette!")
        
        result = c(possibilities)
        
        sleep(5)

        print(result.capitalize())

        if result == bet:
            print("You win!")
            if rows != []:
                print("Looks like you created your account!")
                crs.execute("SELECT credit FROM credits")
                credit = crs.fetchall()
                credit = credit[0][0]
                crs.execute(f"UPDATE credits SET credit = {credit+1}")
            elif rows == []:
                print("You haven't create an account. Please register !")
                usr = input("Enter your username")
                crs.execute(f"INSERT INTO credits VALUES ('{usr}',0)")
            db.commit()
            break
        elif result != bet:
            print("You lose!") 
            db.commit()
            break
    else:
        print("Check your bet please.\n\n")
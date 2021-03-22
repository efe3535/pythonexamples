#/usr/bin/python3
#Python roulette game.
#Written by github.com/efe3535

#Note that this is just an example.
#No money will be PAID.

from random import choice
import sqlite3 as sql
from time import sleep

db = sql.connect('dtb.db')

crs = db.cursor()

print("""
Python Roulette Game
Options:
Red or Black

Rules:
You have %50 percentage of winning.

Good Luck!
""")

crs.execute("CREATE TABLE IF NOT EXISTS credits (username,credit)")

crs.execute("SELECT * FROM credits")

rows = crs.fetchall()

possibilities = ["red","black"]

crs.execute("SELECT credit FROM credits")

credits=crs.fetchall()[0][0]

result = choice(possibilities)
            
while True:

    if credits > 0:
        print(f"your credits: {credits}")
        bet = input("Enter Your Bet\n\n").lower()

        if bet in possibilities:

            print("Ok, so your bet is ", bet.capitalize())
            print("Rollin' roulette!")
            
            
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
                
                if rows != []:
                    print("Looks like you created your account!")
                    crs.execute("SELECT credit FROM credits")
                    credit = crs.fetchall()
                    credit = credit[0][0]
                    crs.execute(f"UPDATE credits SET credit = {credit-1}")
                elif rows == []:
                    print("You haven't create an account. Please register !")
                    usr = input("Enter your username")
                    crs.execute(f"INSERT INTO credits VALUES ('{usr}',0)")
                db.commit()
                break
                
                db.commit()
                break
        else:
            print("Check your bet please.\n\n")
    else:
        print("You have run out of your credits. You can buy them from our store")
        break
db.close()
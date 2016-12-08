#
# PyDB Login Demo
#
# Do not use this for anything useful, the passwords are unencrypted!
#
# (c) 2016 Matt Gallant
#

import pydb

# Login Variable
tok = 0

# Choose Login or Create
print("PyDB Demo")
mode = input("Login or Create: ")

if mode == "create":
    # Create Database
    pydb.create("login")

    # Add Columns
    pydb.addcolumn("login","usernames")
    pydb.addcolumn("login","passwords")

    # Start Main Code
    username = input("Username: ")
    password = input("Password: ")

    pydb.addrow("login","usernames",username,username)
    pydb.addrow("login","passwords",username,password)

    print("Account " + username + " Created!")

if mode == "login":

    # Create Database
    pydb.create("login")

    # Start Main Code
    print("PyDB Login Script")
    username = input("Username: ")
    password = input("Password: ")

    # Get Data
    user = pydb.read("login","usernames",username)
    passwd = pydb.read("login","passwords",username)

    if user == username:
        tok += 1
    if passwd == password:
        tok += 1
    if tok == 2:
        print("Welcome " + username + "!")
    else:
        print("Incorrect Credentials!")
#
# PyDB API Demo
#
# (c) 2016 Matt Gallant
#

import pydb

# Create Database login
pydb.create("demo")

# Add Column users
pydb.addcolumn("demo","users")

# Add Rows
pydb.addrow("login","users","user1","Matt")

# Read From Each Row
user1 = pydb.read("login","users","user1")

# Print Each Row
print(user1)
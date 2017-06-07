#
# PyDB API Demo
#
# (c) 2017 Matt Gallant
#

import pydb

# Create Database login
pydb.create("login")

# Add Column users
pydb.addcolumn("login","users")

# Add Rows
pydb.addrow("login","users","user1","Matt")

# Read From Each Row
user = pydb.readrow("login","users","user1")

# List Columns
col = pydb.listcolumns("login")

# List Rows
rows = pydb.listrows("login", "users")

# Print Each Row
print(user)
print(col)
print(rows)
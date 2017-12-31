#
# PyDB Demo
# A simple way to store persistent data in Python.
# (c) 2018 Matthew Gallant
# Licensed under the MIT license
#

import PyDB as db

# Store some data
db.set("test", "This is a test!")

# Retrieve some data
data = db.get("test")

# Delete some data
db.unset("test")

# List all data entries
datasets = db.list()

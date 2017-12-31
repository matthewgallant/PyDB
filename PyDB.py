#
# PyDB
# A simple way to store persistent data in Python.
# Version 2.0
# (c) 2018 Matthew Gallant
# Licensed under the MIT license
#

import os

def set(key, data):
    if not os.path.exists(".pydb/"):
        os.makedirs(".pydb/")
    dataStore = open(".pydb/" + key + ".data", "w+")
    dataStore.write(str(data))
    dataStore.close()

def get(key):
    dataStore = open(".pydb/" + key + ".data", "r")
    data = dataStore.read()
    dataStore.close()
    return data

def unset(key):
    os.remove(".pydb/" + key + ".data")

def list():
    entries = []
    for file in os.listdir(".pydb/"):
        if file.endswith(".data"):
            entries.append(file[0:-5])
    return entries

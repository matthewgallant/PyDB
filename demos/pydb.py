#
# PyDB Version 1.0
#
# (c) 2016 Matt Gallant
#

import sys
import os
import string
import shutil

def create(x):
    if not os.path.exists(x):
        os.makedirs(x)

def addcolumn(x,y):
    with open(x + "/" + y + ".db", "a") as add_column:
        add_column.close()

def addrow(x,y,z,w):
    fobj = open(x + "/" + y + ".db")
    text = fobj.read().strip().split()
    if z in text: #string in present in the text file
        fn = x + "/" + y + ".db"
        f = open(fn)
        output = []
        for line in f:
            if not z in line:
                output.append(line)
        f.close()
        f = open(fn, 'w')
        f.writelines(output)
        f.close()
        with open(x + "/" + y + ".db", "a") as add_row:
            add_row.write(z + " " + w + "\n")
            add_row.close()
    else: #string is absent in the text file
        with open(x + "/" + y + ".db", "a") as add_row:
            add_row.write(z + " " + w + "\n")
            add_row.close()

def read(x,y,z):
        parse_file = open(x + "/" + y + ".db")
        parsed_file = parse_file.read()
        for line in parsed_file.splitlines():
            if line.startswith(z):
                len_size = len(z)
                line_var = line[len_size+1:]
                return(line_var)
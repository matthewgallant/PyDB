#
# PyDB Version 1.1
#
# (c) 2017 Matt Gallant
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

def readrow(x,y,z):
        parse_file = open(x + "/" + y + ".db")
        parsed_file = parse_file.read()
        for line in parsed_file.splitlines():
            if line.startswith(z):
                len_size = len(z)
                line_var = line[len_size+1:]
                return(line_var)

def listcolumns(x):
        return(os.listdir(x + "/"))

def listrows(x,y):
        d = []
        parse_file = open(x + "/" + y + ".db")
        parsed_file = parse_file.read()
        for line in parsed_file.splitlines():
            row, data = line.split(" ")
            d.append(row)
        return(d)

def rmrow(x,y,z):
        rm_file = open(x + "/" + y + ".db", "r")
        rm_file_line = rm_file.readlines()
        rm_file.close()
        rm_file = open(x + "/" + y + ".db","w")
        for line in rm_file_line:
            if line!=z+"\n":
                rm_file.write(line)
        rm_file.close()
#
# PyDB Version 1.0
#
# (c) 2016 Matt Gallant
#

import sys
import os
import glob

print("PyDB Version 1.0")
print("(c) 2016 Matt Gallant")

loop = 1

def delete():
	remove_name_file = open("db-names","r")
	remove_name_line = remove_name_file.readlines()
	remove_name_file.close()
	remove_name_file = open("db-names","w")
	for line in remove_name_line:
	    if line!=remove_db+"\n":
	        remove_name_file.write(line)
	remove_name_file.close()
	print("Deleted \"" + remove_db + "\"" + "!")

while loop == 1:
    db_cmd = raw_input(">>> ")

    cmd = db_cmd.split()

    if "create" in cmd:
        create_db = db_cmd[7:]

        print("Creating Database: \"" + create_db + "\"")
        with open("db-names", "a") as db_names:
            db_names.write(create_db + "\n")
        if not os.path.exists(create_db):
            os.makedirs(create_db)
        print("Database \"" + create_db + "\" Created Successfully!")

    if "data" in cmd:
        with open("db-names", 'r') as db_print:
            print(db_print.read())

    if "remove" in cmd:
        remove_db = db_cmd[7:]
        print("Are you sure you want to delete \"" + remove_db + "\"?")
        verify = raw_input()
        if verify == "y":
        	delete()
        if verify == "Y":
        	delete()
        if verify == "yes":
        	delete()
        if verify == "Yes":
        	delete()

    if "edit" in cmd:
        edit_db = db_cmd[5:]
        folder, file_name = edit_db.split()
        edit_loop = 1
        while edit_loop == 1:
            database_edit = raw_input(folder + " / " + file_name + " > ")
            if database_edit == "exit":
                edit_loop = 0
            else:
                with open(folder + "/" + file_name + ".db", "a") as db_file:
                    db_file.write(database_edit + "\n")
                    db_file.close()

    if "read" in cmd:
        read_name = db_cmd[5:]
        folder, file_name = read_name.split()
        file_length = len(file_name)
        parse_file = open(folder + "/" + file_name + ".db")
        parsed_file = parse_file.read()
        print("")
        print("Rows:")
        print("")
        print(parsed_file)

    if "base" in cmd:
        base_name = db_cmd[5:]
        path = base_name + "/*.db"   
        files = glob.glob(path)   
        for file in files:     
            f = open(file, 'r')
            print("")  
            sys.stdout.write(f.read())
            f.close() 
        print("")

    if "rmrow" in cmd:
        rmrow = db_cmd[6:]
        folder, file_name, rm_line = rmrow.split()
        rm_file = open(folder + "/" + file_name + ".db", "r")
        rm_file_line = rm_file.readlines()
        rm_file.close()
        rm_file = open(folder + "/" + file_name + ".db","w")
        for line in rm_file_line:
            if line!=rm_line+"\n":
                rm_file.write(line)
        rm_file.close()
                
    if "help" in cmd:
        print("Commands available:")
        print("create, delete, data, edit, read, base, help, exit")
        print("CREATE: Makes a new database")
        print("Ex. create test")
        print("REMOVE: Deletes a database from the PyDB index")
        print("Ex. remove test user")
        print("DATA: Lists all available databases")
        print("Ex. data")
        print("EDIT: Edit a database column")
        print("Ex. edit test user")
        print("READ: Reads data from a column in a database")
        print("Ex. read test user")
        print("BASE: Reads from whole database")
        print("Ex. base test")
        print("HELP: Brings up the help text")
        print("Ex. help")
        print("EXIT: Exits the PyDB shell")
        print("Ex. exit")

    if "exit" in cmd:
        print("Exiting!")
        sys.exit(0)

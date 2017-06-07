# PyDB

A simple way to locally database variables for python programs.

PyDB allows you to save variables that you can call in your code. This is useful because everytime you restart your program, all of your variables are unset, but with PyDB, you can save these forever.

## Getting Started

This will help you get started using PyDB.

### Prerequisites

You will need a system running python2 or python3.

### Installing

Download the version used for importing:

```
curl -O https://raw.githubusercontent.com/ChilliNerd/PyDB/master/demos/pydb.py
```

## Usage

There is up to 4 variables you will need to use in a command: The database name, the column name, the row name and the row data.

First you need to add the pydb.py to the root of your python script's directory, then we need to import it in our code:
```
import pydb
```

Create Database:
```
pydb.create("your database name")
```

Add Column:
```
pydb.addcolumn("your database name","your column name")
```

Add Row:
```
pydb.addrow("your database name","your column name","your row name","your row data")
```

Read Row:
```
pydb.readrow("your database name","your column name","your row name")
```

List Columns:
```
pydb.listcolumns("your database name")
```

List Rows:
```
pydb.listrows("your database name","your column name")
```

## Demos

There is demos avaiable in the demos folder. demo.py prints a variable, login.py is a simple login and create form and gui.py is a tkinter script that saves textfield input.

## Authors

* **Matt Gallant** - *Initial Work* - [Website](http://chillinerd.github.io)

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

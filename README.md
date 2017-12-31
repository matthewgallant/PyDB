# PyDB

A simple way to store persistent data in Python.

PyDB allows you to save variables that you can call in your code. This is useful because everytime you restart your program, all of your variables are unset, but with PyDB, you can save these forever. Plus, it's only 32 lines long (only 20 if you remove comments and spacing)!

## Getting Started

This will help you get started using PyDB.

### Prerequisites

You will need a system running python2 or python3.

### Installing

Download the library:

```
curl -O https://raw.githubusercontent.com/MatthewGallant/PyDB/master/PyDB.py
```

## Usage

First you need to add the PyDB.py to the root of your python script's directory, then we need to import it in our code:
```
import PyDB as db
```

Create Dataset:
```
db.set("test", "This is a test!")
```

Read Dataset:
```
data = db.get("test")
```

Delete Dataset:
```
db.unset("test")
```

List Datasets:
```
datasets = db.list()
```

## Demos

There is a demo showcasing a bit of code in the demo.py file.

## Authors

* **Matt Gallant** - *Initial Work* - [Website](http://matthewgallant.me)

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

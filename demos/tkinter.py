#
# PyDB Tkinter Demo
#
# Shows how to use pydb for application settings.
#
# (c) 2016 Matt Gallant
#
# Click run and exit the program, when you run it again, the label will still be the same until changed!
#

import Tkinter as tk
import pydb

pydb.create("gui")

pydb.addcolumn("gui","labels")

label_text = pydb.readrow("gui","labels","label1")

root = tk.Tk()
root.title("PyDB GUI Demo")
root.geometry("400x300")

def update_btn_text():
    db_text = entry.get()
    pydb.addrow("gui","labels","label1",db_text)
    v.set("Saved label text: " + db_text)

v = tk.StringVar()
v.set(label_text)
label = tk.Label(root, textvariable = v)

entry = tk.Entry(root)

btn = tk.Button(root, command = update_btn_text, text = "Set")

label.pack()
entry.pack()
btn.pack()

root.mainloop()

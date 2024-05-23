from tkinter import *
from tkinter import ttk

app = Tk()
app.geometry("600x400")


def clear():
    combo.set('')


def get_index(*arg):
    Label(app, text="The value at index " + str(combo.current()) +
          " is" + " " + str(var.get()), font=('Helvetica 12')).pack()


months = ('January', 'February', 'March', 'April', 'May', 'June',
          'July', 'August', 'September', 'October', 'November', 'December')

var = StringVar()
combo = ttk.Combobox(app, textvariable=var)
combo['values'] = months
combo['state'] = 'readonly'
combo.pack(padx=5, pady=5)

var.trace('w', get_index)

button = Button(app, text="Clear", command=clear)
button.pack()

app.mainloop()

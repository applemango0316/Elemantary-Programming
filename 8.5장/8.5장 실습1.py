from tkinter import *

# 20244021, 컴퓨터공학과, 김성준
print("20244021, 컴퓨터공학과, 김성준")


def save_data():
    try:
        fileD = open("deliveries.txt", "a")
        fileD.write("Depot:\n")
        fileD.write("%s\n" % depot.get())
        fileD.write("Description:\n")
        fileD.write("%s\n" % description.get())
        fileD.write("Address:\n")
        fileD.write("%s\n" % address.get("1.0", END))
        depot.delete(0, END)
        description.delete(0, END)
        address.delete("1.0", END)
    except Exception as ex:
        app.title("Can't write to the file %s" % ex)


def read_depots(file):
    depots = []
    depots_f = open(file)
    for line in depots_f:
        depots.append(line.rstrip())
    return depots


app = Tk()
app.title("Head-Ex Deliveries")
Label(app, text="Depot:").pack()
depot = StringVar()
depot.set(None)

options = read_depots("depots.txt")
OptionMenu(app, depot, *options).pack()

Label(app, text="Description:").pack()
description = Entry(app)
description.pack()
Label(app, text="Address:").pack()
address = Text(app)
address.pack()

Button(app, text="Save",
       command=save_data).pack()

app.mainloop()

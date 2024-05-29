from tkinter import *

# 20244021, 컴퓨터공학과, 김성준
print("20244021, 컴퓨터공학과, 김성준")


def save_data():
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


app = Tk()
app.title("Head-Ex Deliveries")

Label(app, text="Depot:").pack()
depot = Entry(app)
depot.pack()

Label(app, text="Description:").pack()
description = Entry(app)
description.pack()

Label(app, text="Address:").pack()
address = Text(app)
address.pack()

Button(app, text="Save", command=save_data).pack()

app.mainloop()

from tkinter import *
counter = 0

# 20244021, 컴퓨터공학과, 김성준
print("20244021, 컴퓨터공학과, 김성준")


def counter_label(label):
    def count():
        global counter
        counter += 1
        label.config(text=str(counter))
        label.after(1000, count)
    count()


app = Tk()
app.title("Counting Seconds")
label = Label(app, fg="green")
label.pack()
counter_label(label)
button = Button(app, text='Stop', width=25, command=app.destroy)
button.pack()
app.mainloop()

from tkinter import *
import pygame.mixer
import os

# 20244021, 컴퓨터공학과, 김성준
print("20244021, 컴퓨터공학과, 김성준")

PATH = os.getcwd() + '\\sound'
os.chdir(PATH)

sounds = pygame.mixer
sounds.init()
correct_s = sounds.Sound("correct.wav")
wrong_s = sounds.Sound("wrong.wav")

number_correct = 0
number_wrong = 0


def play_correct_sound():
    global number_correct
    number_correct = number_correct + 1
    correct_s.play()


def play_wrong_sound():
    global number_wrong
    number_wrong = number_wrong + 1
    wrong_s.play()


app = Tk()
app.title("TVN Game Show")
app.geometry('300x110+200+100')

b1 = Button(app, text="correct!", width=10, command=play_correct_sound)
b1.pack(side='left', padx=10, pady=10)

b2 = Button(app, text="wrong!", width=10, command=play_wrong_sound)
b2.pack(side='right', padx=10, pady=10)

app.mainloop()

print(str(number_correct) + " were correctly answered.")
print(str(number_wrong) + " were answered incorrectly.")

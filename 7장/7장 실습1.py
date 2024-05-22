import pygame.mixer
import os


sounds = pygame.mixer
sounds.init()
PATH = os.getcwd() + '\\sound'
os.chdir(PATH)


def wait_finish(channel):
    while channel.get_busy():
        pass


# 20244021, 컴퓨터공학과, 김성준
print("20244021, 컴퓨터공학과, 김성준")

s = sounds.Sound("heartbeat.wav")
wait_finish(s.play())

s2 = sounds.Sound("buzz.wav")
wait_finish(s2.play())

s3 = sounds.Sound("ohno.wav")
wait_finish(s3.play())

s4 = sounds.Sound("carhorn.wav")
wait_finish(s4.play())

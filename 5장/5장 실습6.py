# 20244021, 컴퓨터공학과, 김성준
print("20244021, 컴퓨터공학과, 김성준")


def wCount(word):
    wlist = []
    for wd in text.split():
        wlist.append(wd)
    cnt = wlist.count(word)
    return cnt


f = open("Imagine.txt")
text = f.read()

w = "Imagine"
n = wCount(w)
print(w + ":" + str(n))

wlist = ["Imagine", "people", "dreamer"]
s = {}

for wd in wlist:
    n = wCount(wd)
    s[wd] = n

print(s)

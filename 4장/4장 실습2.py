# 20244021, 컴퓨터공학과, 김성준
print("20244021, 컴퓨터공학과, 김성준")

text = """
Soonchunhyang University
Department of Computer Science and Engineering
"""

f = open("test.txt", "w")
f.write(text)
f.close()

f = open("test.txt")
lines = f.read()
print(lines.upper())

# 20244021, 컴퓨터공학과, 김성준
print("20244021, 컴퓨터공학과, 김성준")

for i in range(5):
    print(i)

print(list(range(5)))

result_f = open("results.txt")
for line in result_f:
    print(line)

list(result_f)
result_f.close()
result_f = open("results.txt")
list(result_f)

result_f.seek(0)

text = result_f.read()
print(text)

print(text.split())

s = "Computer"
print(list(s))

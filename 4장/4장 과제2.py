# 20244021, 컴퓨터공학과, 김성준
print("20244021, 컴퓨터공학과, 김성준")

scores = []
result_f = open("results.txt")

for line in result_f:
    (name, score) = line.split()
    scores.append((float(score)))
result_f.close()

scores.sort()

f = open("scores.txt", "w")
loop = 0
while loop < 3:
    f.write(str(scores[loop]))
    f.write('\n')
    print(scores[loop])
    loop = loop + 1
f.close()

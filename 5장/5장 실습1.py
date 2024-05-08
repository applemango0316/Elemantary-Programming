# 20244021, 컴퓨터공학과, 김성준
print("20244021, 컴퓨터공학과, 김성준")


scores = []
names = []

result_f = open("results.txt")

for line in result_f:
    (name, score) = line.split()
    scores.append((float(score)))
    names.append(name)

result_f.close()

scores.sort()
scores.reverse()

print("The hightest score were:")

print(names[0]+' with'+str(scores[0]))
print(names[1]+' with'+str(scores[1]))
print(names[2]+' with'+str(scores[2]))

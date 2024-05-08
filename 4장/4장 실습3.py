# 20244021, 컴퓨터공학과, 김성준
print("20244021, 컴퓨터공학과, 김성준")

scores = []
result_f = open("results.txt")

for line in result_f:
    (name, score) = line.split()
    scores.append((float(score)))
result_f.close()

scores.sort()
scores.reverse()

print(scores[0])
print(scores[1])
print(scores[2])

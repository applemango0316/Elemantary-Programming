# 20244021, 컴퓨터공학과, 김성준
print("20244021, 컴퓨터공학과, 김성준")

scores = {}
result_f = open("results.txt")

for line in result_f:
    (name, score) = line.split()
    scores[score] = name

result_f.close()

print("The top scores were:")
for each_score in scores.keys():
    print('Surfer ' + scores[each_score] + ' scored ' + each_score)

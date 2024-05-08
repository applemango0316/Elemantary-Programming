# 20244021, 컴퓨터공학과, 김성준
from math import pi
from collections import deque
print("20244021, 컴퓨터공학과, 김성준")

squres = [1, 4, 9, 16, 25]
print(squres)

print(squres[0])
print(squres[-1])
print(squres[-3:])

print(squres + [36, 49, 64, 81, 100])

cubes = [1, 8, 27, 65, 125]
print(cubes)
print(4 ** 3)
cubes[3] = 64
print(cubes)

cubes.append(216)
cubes.append(7 ** 3)
print(cubes)

rgb = ["Red", "Green", "Blue"]
rgba = rgb
id(rgb) == id(rgba)

rgba.append("Alph")
print(rgb)

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
print(letters)

letters[2:5] = ['C', 'D', 'E']
print(letters)

letters[2:5] = []
print(letters)

letters[:] = []
print(letters)

letters = ['a', 'b', 'c', 'd']
len(letters)

a = ['a', 'b', 'c']
n = [1, 2, 3]
x = [a, n]
print(x)

print(x[0])

print(x[0][1])


fruits = ['orange', 'apple', 'pear', 'banana', 'kiwi', 'apple', 'banana']
print(fruits.count('apple'))

print(fruits.count('tangerine'))

print(fruits.index('banana'))

print(fruits.index('banana', 4))

fruits.reverse()
print(fruits)

fruits.append('grape')
print(fruits)

fruits.sort()
print(fruits)

print(fruits.pop())

stack = [3, 4, 5]
stack.append(6)
stack.append(7)
print(stack)

print(stack.pop())

print(stack)

print(stack.pop())

print(stack.pop())

print(stack)

queue = deque(["Eric", "John", "Michael"])
queue.append("Terry")
queue.append("Graham")
print(queue.popleft())

print(queue.popleft())

print(queue)

squares = []
for x in range(10):
    squares.append(x**2)

print(squares)

squares = [x**2 for x in range(10)]
print([(x, y) for x in [1, 2, 3] for y in [3, 1, 4] if x != y])

combs = []
for x in [1, 2, 3]:
    for y in [3, 1, 4]:
        if x != y:
            combs.append((x, y))

print(combs)

vec = [-4, -2, 0, 2, 4]

print([x*2 for x in vec])


print([x for x in vec if x >= 0])

print([abs(x) for x in vec])


freshfruit = ['  banana', '  loganberry ', 'passion fruit  ']
[weapon.strip() for weapon in freshfruit]


print([(x, x**2) for x in range(6)])

vec = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print([num for elem in vec for num in elem])


print([str(round(pi, i)) for i in range(1, 6)])

matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
]
print([[row[i] for row in matrix] for i in range(4)])

transposed = []
for i in range(4):
    transposed.append([row[i] for row in matrix])

print(transposed)

transposed = []
for i in range(4):
    # the following 3 lines implement the nested listcomp
    transposed_row = []
    for row in matrix:
        transposed_row.append(row[i])
    transposed.append(transposed_row)

print(transposed)

list(zip(*matrix))

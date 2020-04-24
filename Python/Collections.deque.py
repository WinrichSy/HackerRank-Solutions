#Collections.deque()
#https://www.hackerrank.com/challenges/py-collections-deque/problem

from collections import deque

num_inputs = int(input())
d = deque()

for i in range(num_inputs):
    command = input().split()
    if command[0] == 'append':
        d.append(int(command[1]))
    elif command[0] == 'appendleft':
        d.appendleft(int(command[1]))
    elif command[0] == 'clear':
        d.clear()
    elif command[0] == 'extend':
        d.extend(command[1])
    elif command[0] == 'extendleft':
        d.extendleft(command[1])
    elif command[0] == 'count':
        d.count(command[1])
    elif command[0] == 'pop':
        d.pop()
    elif command[0] == 'print':
        print(d)
    elif command[0] == 'popleft':
        d.popleft()
    elif command[0] == 'remove':
        d.remove(command[1])
    elif command[0] == 'reverse':
        d.reverse()
    elif command[0] == 'rotate':
        d.rotate(int(command[1]))

ans = ''
for i in d:
    ans += str(i) + ' '

print(ans.strip())

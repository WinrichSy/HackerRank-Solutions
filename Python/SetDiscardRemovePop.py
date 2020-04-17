#Set .discard() .remove() & .pop()
https://www.hackerrank.com/challenges/py-set-discard-remove-pop/problem

n = int(input())
s = set(map(int, input().split()))

i = int(input())
for j in range(i):
    commands = input().split()
    if commands[0] == 'pop':
        if len(s) > 0:
            s.pop()
    elif commands[0] == 'discard':
        s.discard(int(commands[1]))
    elif commands[0] == 'remove':
        try:
            s.remove(int(commands[1]))
        except:
            continue


print(sum(s))

#Exceptions
#https://www.hackerrank.com/challenges/exceptions/problem

times = int(input())
for i in range(times):
    inputs = input().split()
    try:
        a = int(inputs[0])
        b = int(inputs[1])
        print(a//b)
    except ZeroDivisionError as e:
        print('Error Code:', e)
    except ValueError as e:
        print('Error Code:', e)

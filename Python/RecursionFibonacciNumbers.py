#Recursion: Fibonacci Numbers
#https://www.hackerrank.com/challenges/ctci-fibonacci-numbers/problem

def fibonacci(n):
    if n==0:
        return 0
    if n==1:
        return 1
    return(fibonacci(n-1)+fibonacci(n-2))

n = int(input())
print(fibonacci(n))

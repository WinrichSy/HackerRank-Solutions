#collections.Counter()
#https://www.hackerrank.com/challenges/collections-counter/problem

from collections import Counter

num_of_shoes = int(input())
shoe_sizes = Counter([int(i) for i in input().split(' ')])
num_of_customers = int(input())

total = 0
for i in range(num_of_customers):
    size_price = input().split(' ')
    size, price = int(size_price[0]), int(size_price[1])
    if shoe_sizes[size] > 0:
        total += price
        shoe_sizes[size] -= 1

print(total)

#Iterables and Iterators
#https://www.hackerrank.com/challenges/iterables-and-iterators/problem

import itertools
#contains the letter 'a'

num_letters = int(input())
letters = input().split(' ')
tuple_length = int(input())

combos = itertools.combinations(letters, tuple_length)
containing_a = sum([1 if 'a' in i else 0 for i in itertools.combinations(letters, tuple_length)])
total = sum([1 for i in list(combos)])
print(containing_a/total)

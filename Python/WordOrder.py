#Word Order
#https://www.hackerrank.com/challenges/word-order/problem

dictionary = {}

num_of_words = int(input())
for i in range(num_of_words):
    word = input()
    if word not in dictionary:
        dictionary[word]=1
    else:
        dictionary[word] += 1

vals = ''
for i in list(dictionary.values()):
    vals += str(i) + ' '

print(len(dictionary.keys()))
print(vals.strip())

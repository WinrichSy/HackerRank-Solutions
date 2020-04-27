#Collections.OrderedDict()
#https://www.hackerrank.com/challenges/py-collections-ordereddict/problem

from collections import OrderedDict

items = int(input())
ordered_dict = OrderedDict()
for i in range(items):
    item_price = input().split()
    item = ' '.join(item_price[0:-1])
    price = int(item_price[-1])
    if item not in ordered_dict.keys():
        ordered_dict[item] = price
    else:
        ordered_dict[item] += price

for key, val in ordered_dict.items():
    print('{} {}'.format(key, val))

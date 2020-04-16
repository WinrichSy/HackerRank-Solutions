#Nested Lists
https://www.hackerrank.com/challenges/nested-list/problem

some_dict={}
for _ in range(int(raw_input())):
    name = raw_input()
    score = float(raw_input())
    some_dict[name] = score


sorted_list = (sorted(some_dict.items(), key = lambda kv:(kv[1], kv[0])))
lowest_score = sorted_list[0][1]

iterator = 1
while(lowest_score == sorted_list[iterator][1]):
    iterator += 1

second_lowest_score = sorted_list[iterator][1]
second_lowest_name = []
second_lowest_name.append(sorted_list[iterator][0])

if len(sorted_list)>iterator:
    for i in sorted_list[iterator+1:]:
        if second_lowest_score == i[1]:
            second_lowest_name.append(i[0])
        else:
            break

for i in second_lowest_name:
    print(i)

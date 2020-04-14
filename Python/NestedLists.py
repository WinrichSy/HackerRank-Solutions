#Nested Lists
#https://www.hackerrank.com/challenges/nested-list/problem

if __name__ == '__main__':
    d = {}
    score_list = []
    for _ in range(int(raw_input())):
        name = raw_input()
        score = float(raw_input())
        d[name] = score
        score_list.append(score)

    score_list = sorted(score_list)
    lowest = score_list[0]
    for i in score_list:
        if(i>lowest):
            lowest = i
            break

    low_score_name = []
    for name, score in d.items():
        if d[name] == lowest:
            low_score_name.append(name)

    low_score_name.sort()
    for i in low_score_name:
        print(i)

#Find the Runner-Up Score!
#https://www.hackerrank.com/challenges/find-second-maximum-number-in-a-list/problem

if __name__ == '__main__':
    n = int(raw_input())
    arr = map(int, raw_input().split())

    sorted_array = sorted(arr)
    sorted_array = sorted_array[::-1]
    highest_score = sorted_array[0]

    for i in sorted_array:
        if(i<highest_score):
            highest_score = i
            break

    print(highest_score)

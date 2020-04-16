#Find A String
#https://www.hackerrank.com/challenges/find-a-string/problem

def count_substring(string, sub_string):
    counter = 0
    contains = False

    for i in range(len(string)):
        if string[i] != sub_string[0]:
            continue

        else:
            contains = False
            for j in range(len(sub_string)):
                if i+j < len(string):
                    if string[i+j]==sub_string[j]:
                        contains = True
                    else:
                        contains = False
                        break
                elif j < len(sub_string):
                    contains = False


            if contains:
                counter+=1
                contains = False

    return counter

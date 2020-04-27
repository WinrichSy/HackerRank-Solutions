#Merge the Tools!
#https://www.hackerrank.com/challenges/merge-the-tools/problem

def remove_repeat_occurence(lst):
    ans = [lst[0]]
    for i in lst[1:]:
        if i not in ans:
            ans.append(i)
    return ''.join(ans)

def merge_the_tools(string, k):
    subs = [string[i:i+k] for i in range(0,len(string), k)]
    for i in subs:
        print(remove_repeat_occurence(i))

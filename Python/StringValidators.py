#String Validators
#https://www.hackerrank.com/challenges/string-validators/problem

if __name__ == '__main__':
    s = input()
    print(True in [True if i.isalnum() else False for i in s])
    print(True in [True if i.isalpha() else False for i in s])
    print(True in [True if i.isdigit() else False for i in s])
    print(True in [True if i.islower() else False for i in s])
    print(True in [True if i.isupper() else False for i in s])

#String Formatting
#https://www.hackerrank.com/challenges/python-string-formatting/problem

def print_formatted(number):
    width = len(str('{0:b}'.format(number)))
    for i in range(1, number+1):
        spaces1 = " "*(width-len(str(i)))
        spaces2 = " "*(width-len(str(oct(i))[2:])+1)
        spaces3 = " "*(width-len(str(hex(i))[2:])+1)
        spaces4 = " "*(width-len(str("{0:b}".format(i)))+1)
        print(spaces1+str(i) +spaces2+ str(oct(i))[2:] +spaces3+ str(hex(i)).upper()[2:] +spaces4+ str("{0:b}".format(i)))

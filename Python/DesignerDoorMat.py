#Designer Door Mat
#https://www.hackerrank.com/challenges/designer-door-mat/problem

dimensions = input().split(' ')
rows = int(dimensions[0])
columns = int(dimensions[1])
pattern = '.|.'
for i in range(rows):
    if i == rows//2:
        print(('-')*((columns//2)-3) +'WELCOME'+ ('-')*((columns//2)-3))
    elif i<rows//2:
        print(('-')*((columns//2)-(i*3)-1) +(pattern*(2*i)+pattern)+ ('-')*((columns//2)-(i*3)-1))
    elif i>rows//2:
        diff = abs(i-rows)-1
        print(('-')*((columns//2)-(diff*3)-1) +(pattern*(2*diff)+pattern)+ ('-')*((columns//2)-(diff*3)-1))

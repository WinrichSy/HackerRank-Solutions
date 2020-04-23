#Calendar Module
#https://www.hackerrank.com/challenges/calendar-module/problem

import calendar

days = {0:'MONDAY',
        1:'TUESDAY',
        2:'WEDNESDAY',
        3:'THURSDAY',
        4:'FRIDAY',
        5:'SATURDAY',
        6:'SUNDAY'}
date = input().split(' ')
month, day, year = int(date[0]), int(date[1]), int(date[2])

print(days[calendar.weekday(year, month, day)])

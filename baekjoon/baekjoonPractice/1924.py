import sys
input = sys.stdin.readline

x, y = map(int,input().split())

day = ['SUN','MON','TUE','WED','THU','FRI','SAT']

month = [31,28,31,30,31,30,31,31,30,31,30,31]

totalDay = sum(month[:x-1])+y

lastDay = day[totalDay%7]
print(lastDay)
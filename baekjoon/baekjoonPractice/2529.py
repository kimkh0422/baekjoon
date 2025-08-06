import sys
from itertools import permutations
input = sys.stdin.readline

k = int(input())
signs = input().split()
numbers = ['0','1','2','3','4','5','6','7','8','9']
result = []

def check(number):
    for i in range(k):
        if signs[i] == '<' and number[i] >= number[i+1]:
            return False
        if signs[i] == '>' and number[i] <= number[i+1]:
            return False
    return True

for number in permutations(numbers, k+1):
    if check(number):
        result.append("".join(number))

print(max(result))
print(min(result))

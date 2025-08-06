import sys
input = sys.stdin.readline

N = int(input())

numbers = [-1] * (N + 1)

def fib(i):
    if i == 0:
        numbers[i] = 0
        return 0
    if i == 1:
        numbers[i] = 1
        return 1
    if numbers[i] != -1:
        return numbers[i]
    numbers[i] = fib(i - 1) + fib(i - 2)
    return numbers[i]

print(fib(N))

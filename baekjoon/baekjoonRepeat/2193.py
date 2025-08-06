import sys
input = sys.stdin.readline

N = int(input())

numbers = [0]*(N+1)


def fib(number):
    if number == 1:
        return 1
    if number == 2:
        return 1
    if numbers[number] !=0:
        return numbers[number]

    numbers[number] = fib(number-1)+ fib(number-2)
    return numbers[number]

print(fib(N))
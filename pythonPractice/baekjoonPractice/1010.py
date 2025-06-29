import sys
input = sys.stdin.readline

T = int(input())

def fact(a):
    number = 1
    for i in range(1,a+1):
        number = number*i
    return number

def comb(a,b):
    result = fact(a)//(fact(b)*fact(a-b))
    return result




for _ in range(T):
    N, M = map(int,input().split())  
    print(comb(M,N))


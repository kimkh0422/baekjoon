import sys
input = sys.stdin.readline

T = int(input())

def factorial(number):
    result = 1
    for i in range(1,number+1):
        result*=i
    return result

def makeComb(N,M):   #  mCn = m! / (n! * (m-n)!)
    return factorial(M) // (factorial(N)*factorial(M-N))



for _ in range(T):
    N,M = map(int,input().split())
    print(makeComb(N,M))
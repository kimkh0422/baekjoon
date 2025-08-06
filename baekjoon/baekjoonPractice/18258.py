import sys
from collections import deque

queue = deque()
input = sys.stdin.readline
N = int(input())

def push(a):
    queue.append(a)

def pop():
    if not queue:
        return -1
    else:
        return queue.popleft()

def size():
    return len(queue)

def empty():
    if not queue:
        return 1
    else:
        return 0
    
def front():
    if not queue:
        return -1
    else:
        return queue[0]
    
def back():
    if not queue:
        return -1
    else:
        return queue[-1]
        


for i in range(N):
    command = input().strip().split()

    if command[0] == 'push':
        push(command[1])

    elif command[0] == 'pop':
        print(pop())

    elif command[0] == 'size':
        print(size())

    elif command[0] == 'empty':
        print(empty())

    elif command[0] == 'front':
        print(front())

    elif command[0] == 'back':
        print(back())
      


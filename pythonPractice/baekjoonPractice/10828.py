import sys
input = sys.stdin.readline

stack = []

def push(a):
   stack.append(a)

def pop():
    if len(stack)==0:
        print(-1)
    else:
        print(stack.pop())

def size():
    print(len(stack))

def empty():
    if len(stack)==0:
        print(1)
    else:
        print(0)

def top():
    if len(stack)==0:
        print(-1)
    else:
        print(stack[len(stack)-1])

count = int(input())


for i in range(count):
    command = input().split()

    if command[0] == 'push':
        push(int(command[1]))
    elif command[0] == 'pop':
        pop()
    elif command[0] == 'size':
        size()
    elif command[0] == 'empty':
        empty()
    elif command[0] == 'top':
        top()



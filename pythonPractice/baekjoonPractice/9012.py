import sys
input = sys.stdin.readline

T = int(input())

result = []

for i in range(T):
    PS = input()
    stack = []
    is_VPS = True

    for char in PS:
        if char == '(':
            stack.append(char)
        elif char == ')':
            if not stack:
                is_VPS = False
                break
            stack.pop()
    if stack:
        is_VPS = False

    if is_VPS == True:
        result.append('YES')
    else:
        result.append('NO')

print('\n'.join(result))


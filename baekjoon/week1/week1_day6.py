h = int(input("원하는 행의 크기를 입력하세요."))
a = int(input("원하는 열의 크기를 입력하세요."))

doubleArray = [[1 for i in range(a)]for i in range(h)]

for array in doubleArray:
    print(array)
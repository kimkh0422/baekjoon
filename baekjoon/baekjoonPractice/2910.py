from collections import defaultdict


N,C = map(int,input().split())

numbers = list(map(int,input().split()))

freq = defaultdict(int)   #freq라는 딕셔너리를 만듦

for num in numbers:
    freq[num] += 1  #freq라는 딕셔너리에 키랑 벨류 추가. num이 키값이고 freq[num]이 벨류값. 즉 키값 하나 등장할때마다 벨류값에 1씩 추가. 배열에 키값이 총 몇개있는지 알 수 있음음

for key in freq:
    print(f"{key} : {freq[key]}번 등장")
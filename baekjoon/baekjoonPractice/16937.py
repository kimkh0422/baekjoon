import sys
input = sys.stdin.readline

H, W = map(int, input().split())  # 모눈종이 크기
N = int(input())

stickers = []

for _ in range(N):
    R, C = map(int, input().split())
    stickers.append((R, C))  # 각 스티커의 크기 저장

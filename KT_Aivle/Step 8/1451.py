import sys
input = sys.stdin.readline

N, M = map(int, input().split())
square = []

for _ in range(N):
    square.append(int(input()))
    
print(square)
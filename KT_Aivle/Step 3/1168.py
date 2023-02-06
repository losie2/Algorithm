from collections import deque
import sys
input = sys.stdin.readline

N, K = map(int, input().split())

q = [i for i in range(1, N + 1)]
cursor = 0
result = []
for _ in range(N):
    cursor += K - 1
    cursor %= len(q)
    result.append(str(q.pop(cursor)))
    
print("<" + ", ".join(result) + ">")
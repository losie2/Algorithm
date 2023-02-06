from collections import deque
import sys
input = sys.stdin.readline

n, k = map(int, input().split())

q = deque((range(1, n+1)))
answer = []

while len(q) != 1:
    for _ in range(k-1):
        q.append(q.popleft())
    answer.append(q.popleft())
answer.append(q[0])

print(f"<{', '.join(map(str,answer))}>")
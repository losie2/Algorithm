import sys
N = int(sys.stdin.readline())
nums = []

for i in range(N):
    nums.append(list(map(int, sys.stdin.readline().split())))
    
nums.sort(key=lambda x: (x[1], x[0]))

for i in nums:
    print(i[0], i[1])
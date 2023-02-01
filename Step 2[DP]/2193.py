import sys
input = sys.stdin.readline

N = int(input())
# 1 1
# 10 1
# 101 100 2
# 1010 1001 1000 3
# 10101 10010 10100 10000 10001 5
# 101010 100100 101001 100000 101000 100010 100001 100101 8

DP = [0] * 91
DP[1] = 1
DP[2] = 1

for i in range(3, N + 1):
    DP[i] = DP[i - 2] + DP[i - 1]
    
print(DP[N])
import sys
input = sys.stdin.readline

n = int(input())

dp = [[0] + [0 for i in range(10)] + [0] for j in range(101)]

for i in range(1, 10):
    dp[1][i] = 1
    
for i in range(2, n + 1):
    for j in range(10):
        dp[i][j] = dp[i - 1][j - 1] + dp[i - 1][j + 1]
    
print(sum(dp[n]) % 1000000000)
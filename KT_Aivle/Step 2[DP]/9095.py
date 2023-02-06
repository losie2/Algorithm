import sys
read = sys.stdin.readline

dp = [0] * 11

dp[1] = 1
dp[2] = 2
dp[3] = 4 # 1,1,1/ 1,2 / 2, 1/ 3
dp[4] = 7 # 1,1,1,1 / 1,1,2 / 1,2,1 / 2, 1, 1/ 2,2 / 1, 3/ 3, 1
dp[5] = 13 # 1,1,1,1,1 / 1,1,1,2 / 1,1,2,1/ 1,2,1,1 / 2,1,1,1 / 1,2,2 / 2,1,2 / 2,2, 1/ 1,1,3/ 1,3,1/3,1,1/ 2,3/ 3,2

for i in range(5, 11):
    dp[i] = sum(dp[i-3:i])
    
N = int(read())
for _ in range(N):
    print(dp[int(read())])

import sys
input = sys.stdin.readline

N = int(input())

#   0 1 2 3  4  5  6  7  8 9 # 맨 뒤 숫자
# 0 0 0 0 0  0  0  0  0  0 0
# 1 1 1 1 1  1  1  1  1  1 1     10
# 2 1 2 3 4  5  6  7  8  9 10    55
# 3 1 3 6 10 15 21 28 36 45 55   220

DP = [[0 for _ in range(11)] for _ in range(N + 1)]

for i in range(10):
    DP[1][i] = 1
    
for i in range(N + 1):
    DP[i][0] = 1

for i in range(2,N + 1):
    for j in range(1, 10):
        DP[i][j] = (DP[i][j - 1] + DP[i - 1][j])
        
print(sum(DP[N]) % 10007)


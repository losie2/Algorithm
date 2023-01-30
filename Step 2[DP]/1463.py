# 첫 번째 시도(dfs), 시간 초과 실패

# N = int(input())
# answer = []

# def dp(N, cnt):
#     if N == 1:
#         answer.append(cnt)
#         return
#     if N % 3 == 0:
#         dp(N / 3, cnt + 1)
    
#     if N % 2 == 0:
#         dp(N / 2, cnt + 1)
    
#     dp(N - 1, cnt + 1)
    
# dp(N, 0)
# print(min(answer))

# 두 번째 접근(dp)
N = int(input())

dp = [0] * (N + 1)

for i in range(2, N + 1):
    dp[i] = dp[i-1] + 1
    
    if i % 2 == 0:
        dp[i] = min(dp[i], dp[i // 2] + 1)
    if i % 3 == 0:
        dp[i] = min(dp[i], dp[i // 3] + 1)
        
print(dp[N])
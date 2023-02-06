import sys
input = sys.stdin.readline

N = int(input())
nums = {}

for i in range(N):
    card = int(input())
    if card in nums:
        nums[card] += 1
    else:
        nums[card] = 1
result = sorted(nums.items(), key = lambda x : (-x[1], x[0]))
print(result[0][0])
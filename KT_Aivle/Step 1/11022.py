N = int(input())
numbers = []
for i in range(N):
    A, B = input().split(' ')
    numbers.append([int(A), int(B)])
    
cnt = 1
for number in numbers:
    print(f"Case #{cnt}: {number[0]} + {number[1]} = {number[0] + number[1]}")
    cnt += 1
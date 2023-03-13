import sys
input = sys.stdin.readline

E, S, M = map(int, input().split())
a, b, c = 1, 1, 1
year = 0
if E == S and S == M and M == E:
    print(S)
    exit()

while True:
    
    a += 1
    b += 1
    c += 1
    year += 1
    
    if a > 15:
        a = 1
    if b > 28:
        b = 1
    if c > 19:
        c = 1
    
    if a == E and b == S and c == M and year > 14:
        print(year + 1)
        break
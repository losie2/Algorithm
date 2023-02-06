import sys
input = sys.stdin.readline

string = input()
alpha = list('abcdefghijklmnopqrstuvwxyz')

lower = [0] * len(alpha)
for ch in string:
    if ch in alpha:
        lower[alpha.index(ch)]+=1
for low in lower:
    print(low, end = ' ')
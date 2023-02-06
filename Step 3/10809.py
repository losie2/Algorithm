import sys
input = sys.stdin.readline
S = input()
for ch in 'abcdefghijklmnopqrstuvwxyz':
    print(S.find(ch), end = ' ')
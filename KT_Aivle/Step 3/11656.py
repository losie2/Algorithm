import sys
input = sys.stdin.readline

S = input()
S = S[::-1]
tail = []
st = ""
for ch in S:
    if ch != '\n':
        st += ch
        tail.append(st[::-1])

tail.sort()
for t in tail:
    print(t)    

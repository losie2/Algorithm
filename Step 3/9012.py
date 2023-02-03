import sys
input = sys.stdin.readline

N = int(input())

for _ in range(N):
    s = list(input())
   
    stack = []
    VPS = True
    
    for c in s:
        if c == '(':
            stack.append('(')
        if c == ')':
            if stack:
                stack.pop()
            elif not stack:
                VPS = False
                break
    if not stack and VPS:
        print('YES')
    elif stack or not VPS:
        print('NO')
            
        
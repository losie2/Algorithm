import sys
N = int(sys.stdin.readline())
person = []

for i in range(N):
    age, name = map(str, input().split())
    age = int(age)
    person.append((age,name))
    
person.sort(key=lambda x: x[0])

for i in person:
    print(i[0], i[1])
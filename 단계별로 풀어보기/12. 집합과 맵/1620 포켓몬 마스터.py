import sys

n, m = map(int, sys.stdin.readline().split())

name_saver = {}
count_saver = {}
ans = []

for i in range(1, n+1):
    name = sys.stdin.readline().strip()
    name_saver[i] = name
    count_saver[name] = i

for i in range(m):
    test = sys.stdin.readline().strip()
    if test.isdigit():
        ans.append(name_saver[int(test)])
    else:
        ans.append(count_saver[test])

for i in ans:
    print(i)
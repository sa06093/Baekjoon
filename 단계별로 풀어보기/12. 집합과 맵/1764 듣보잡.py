import sys

n, m = map(int, sys.stdin.readline().split())
setn = set()
ans_list = []

for i in range(n):
    name = sys.stdin.readline().strip()
    setn.add(name)

for i in range(m):
    test = sys.stdin.readline().strip()
    if test in setn:
        ans_list.append(test)
ans_list.sort()
print(len(ans_list))
for i in ans_list:
    print(i)
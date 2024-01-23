import sys

a, b = map(int, sys.stdin.readline().split())
set_a = set(map(int, sys.stdin.readline().split()))
set_b = set(map(int, sys.stdin.readline().split()))
count = 0

for i in set_b:
    if i not in set_a:
        count += 1

for i in set_a:
    if i not in set_b:
        count += 1

print(count)
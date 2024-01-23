import sys

a, b = map(int, sys.stdin.readline().split())

for i in range(min(a, b), 0, -1):
    if a % i == 0 and b % i == 0:
        max_val = i
        break

ans = a * b / max_val
print(f'{ans:.0f}')
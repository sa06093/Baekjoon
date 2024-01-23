import sys

a, b = map(int, sys.stdin.readline().split())
c, d = map(int, sys.stdin.readline().split())

top = a * d + b * c
bottom = b * d

def gcd(x, y):
    while y:
        x, y = y, x % y
    return x

max_val = gcd(top, bottom)

ans_top = top // max_val
ans_bottom = bottom // max_val
print(ans_top, end=' ')
print(ans_bottom)
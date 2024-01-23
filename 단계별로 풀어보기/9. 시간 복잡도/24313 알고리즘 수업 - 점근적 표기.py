a1, a0 = map(int, input().split())
c = int(input())
n0 = int(input())


# 초기값도 더 커야하고
# 커져가는 기울기도 더 커야함
if (a1*n0 + a0 <= c*n0) and (a1<=c):
    print(1)
else:
    print(0)
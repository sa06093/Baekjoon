n = int(input())

ans = -1
for i in range(1001):
    for j in range(5):
        if 5 * i + 3 * j == n:
            ans = i + j
print(ans)
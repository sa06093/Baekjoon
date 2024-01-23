# 몬테칼로 적분법 사용

n = int(input())
total_array = [[0]*100 for i in range(100)]

for i in range(n):
    x, y = map(int, input().split())
    for i in range(y, y + 10):
        dir_y = i
        for j in range(x, x + 10):
            dir_x = j
            if total_array[dir_y][dir_x] == 0:
                total_array[dir_y][dir_x] = 1
            else:
                pass
total = 0
for i in range(100):
    total += sum(total_array[i])
print(total)
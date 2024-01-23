n, m = map(int, input().split())
num_list = list(map(int, input().split()))

max  = 1
for i in range(n - 2):
    for j in range(i + 1, n - 1):
        for k in range(j + 1, n):
            if  max < num_list[i] + num_list[j] + num_list[k] <= m:
                max = num_list[i] + num_list[j] + num_list[k]
print(max)
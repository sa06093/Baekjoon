n = int(input())
list1 = []
ans = 0
for i in range(n):
    list1.append(int(input()))

end = n - 1

list1 = sorted(list1)

for i in range(1, n):
    for j in range(1, n):
        if i + j + list1[end-1] == list1[end]:
            ans = list1[end]
        elif i + j + list1[end-1] > list1[end]:
            end -= 1
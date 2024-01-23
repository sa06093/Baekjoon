n, k = map(int, input().split())
list1 = [i for i in range(1, n+1)]
ans = []
index = 0
while len(list1) != 0:
    index += (k-1)
    index = index % len(list1)
    ans.append(list1.pop(index))

print("<",end="")
for i in range(n-1):
    print(ans[i],end=", ")
print(ans[n-1], end = "")
print(">",end="")
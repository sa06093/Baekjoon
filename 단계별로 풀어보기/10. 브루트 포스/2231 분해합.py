n = int(input())
ans = 0
for i in range(n):
    lista = [j for j in str(i)]
    integer_list = list(map(int, lista))
    if i + sum(integer_list) == n:
        ans = i
        break
print(ans)
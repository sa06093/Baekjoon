total_list = []
max_list = []
for i in range(1, 10):
    lista = list(map(int, input().split()))
    max_list.append(max(lista))
    total_list.append(lista)

max_val = max(max_list)
max_x = max_list.index(max_val)
max_y = total_list[max_x].index(max_val)

print(max_val)
print(max_x + 1, end=" ")
print(max_y + 1)
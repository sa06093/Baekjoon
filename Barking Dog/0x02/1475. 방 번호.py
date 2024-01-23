n = str(input())


lista = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
count_list = [0 for i in range(10)]

for i in range(len(n)):  # 0 1 2 3
    place = lista.index(int(n[i]))
    count_list[place] += 1


list_left = count_list[0:6] + count_list[7:9]
max_of_left = max(list_left)

sum_of_69 = count_list[6] + count_list[9]
if sum_of_69 % 2 == 0:
    count_69 = sum_of_69 // 2
else:
    count_69 = sum_of_69 // 2 + 1

ans = max(max_of_left, count_69)

print(ans)
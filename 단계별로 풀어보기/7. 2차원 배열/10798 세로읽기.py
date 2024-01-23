total_list = []
len_list = []
for i in range(5):
    string = input()
    list1 = [i for i in string]
    len_list.append(len(list1))
    total_list.append(list1)

max_len = max(len_list)
for i in total_list:
    if len(i) < max_len:
        for j in range(max_len - len(i)):
            i.append("$")

ans_list = []

for i in range(max_len):
    for j in range(5):
        ans_list.append(total_list[j][i])

ans = ''.join(ans_list)
ans = ans.replace('$', '')
print(ans)
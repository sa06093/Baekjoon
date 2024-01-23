s = input()

total_list = []

for i in range(0, len(s)+1):
    for j in range(i+1, len(s)+1):
        total_list.append(s[i:j])

ans_list = list(set(total_list))
print(len(ans_list))
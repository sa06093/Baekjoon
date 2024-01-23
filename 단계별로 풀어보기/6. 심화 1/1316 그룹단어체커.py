n = int(input())
ans_count = 0

for j in range(n):
    string = input()
    once = set()
    lista = []
    count = 0
    once.add(string[0])
    lista.append(string[0])
    for i in range(len(string)-1):
        # 그룹 단어가 아니라면 1 추가
        if (string[i + 1] in once) and (string[i + 1] != string[i]):
            count += 1
            break
        else:
            once.add(string[i + 1])
            lista.append(string[i + 1])
    # 총 그룹 단어가 아닌것에 개수 더해주기
    ans_count += count
# 전체에서 총 그룹 단어가 아닌것 빼기
print(n-ans_count)
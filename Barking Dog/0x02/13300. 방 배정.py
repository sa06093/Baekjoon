n, k = map(int, input().split())

dict_of_man = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0}
dict_of_woman = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0}

for i in range(n):
    s, y = map(int, input().split())
    if s == 1:
        dict_of_man[y] += 1
    else:
        dict_of_woman[y] += 1

sum_of_man = 0
sum_of_woman = 0

for i in dict_of_man.values():
    if i > k:
        if i % k == 0:
            sum_of_man += (i // k)
        else:
            sum_of_man += (i // k + 1)
    elif i == 0:
        sum_of_man = sum_of_man
    else:
        sum_of_man += 1

for i in dict_of_woman.values():
    if i > k:
        if i % k == 0:
            sum_of_woman += (i // k)
        else:
            sum_of_woman += (i // k + 1)
    elif i == 0:
        sum_of_woman = sum_of_woman
    else:
        sum_of_woman += 1

print(sum_of_man + sum_of_woman)

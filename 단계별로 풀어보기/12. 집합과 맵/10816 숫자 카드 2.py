import sys

n = int(sys.stdin.readline())
list_n = list(map(int, sys.stdin.readline().split()))
m = int(sys.stdin.readline())
list_m = list(map(int, sys.stdin.readline().split()))

card_dict = {}
for i in list_n:
    if i not in card_dict:
        card_dict[i] = 1
    else:
        card_dict[i] += 1

for i in list_m:
    if i in card_dict:
        print(card_dict[i], end=' ')
    else:
        print(0, end=' ')
import sys

n = int(sys.stdin.readline())
list_n = list(map(int, sys.stdin.readline().split()))
m = int(sys.stdin.readline())
list_m = list(map(int, sys.stdin.readline().split()))

card_dict = {}
for i in list_n:
    card_dict[i] = 0

for i in list_m:
    if i in card_dict:
        print(1, end=' ')
    else:
        print(0, end=' ')
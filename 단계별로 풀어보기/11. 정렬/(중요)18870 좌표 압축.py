import sys

n = int(sys.stdin.readline())
lista = list(map(int, sys.stdin.readline().split()))

listb = sorted(list(set(lista)))

index_dict = {value: index for index, value in enumerate(listb)}

ans_list = [index_dict[i] for i in lista]

print(*ans_list)
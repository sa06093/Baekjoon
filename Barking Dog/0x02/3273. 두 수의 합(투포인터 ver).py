import sys

n = int(sys.stdin.readline())
lista = list(map(int, sys.stdin.readline().split()))
lista = sorted(lista)
x = int(sys.stdin.readline())

start = 0
end  = len(lista) - 1
count = 0

while start < end:
    if lista[start] + lista[end] == x:
        count += 1
        start += 1
        end -= 1
    elif lista[start] + lista[end] > x:
        end -= 1
    else:
        start += 1
print(count)
n = int(input())
lista = list(map(int, input().split()))
x = int(input())
count = 0
seta = set(lista)
already = set()

for i in lista:
    if i in already:
        pass
    else:
        tofind = x - i
        if i != tofind:
            if tofind in seta:
                count += 1
                already.add(i)
                already.add(tofind)
print(count)
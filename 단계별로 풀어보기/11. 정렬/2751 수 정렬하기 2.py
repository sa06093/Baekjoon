import sys

n = int(sys.stdin.readline())
lista = []
for i in range(n):
    a = int(sys.stdin.readline())
    lista.append(a)
    
lista.sort()

for i in lista:
    print(i)
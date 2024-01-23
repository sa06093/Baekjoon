n, b = map(float, input().split())
lista = []

while True:
    lista.append(n % b)
    n = n // b

    if n < b:
        lista.append(n)
        break

lista.reverse()
int_list = []
for i in lista:
   int_list.append(int(i))

if int_list[0] == 0:
    int_list.pop(0)

ans_list = []

for i in int_list:
    i = int(i)
    if i > 9:
        ans_list.append(chr(i + 55))
    else:
        ans_list.append(str(i))

ans = ''.join(ans_list)
print(ans)
n = int(input())
origin_n = n
i = 1
while True:
    if n > i:
        n -= i
        i += 1
    else:
        break

# 홀수라면
if i % 2 == 1:
    a = i - n + 1
    b = n
else:
    a = n
    b = i - n + 1

print(a,end='')
print('/', end='')
print(b)
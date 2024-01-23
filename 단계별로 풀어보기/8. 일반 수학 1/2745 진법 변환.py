n, b = map(str, input().split())
b = int(b)
ans = 0

for i in range(len(n)):
    y = b**i
    
    j = len(n)-i-1
    if ord(n[j]) <= 57:
        x = int(n[j])
    else:
        x = ord(n[j]) - 55

    ans += x*y

print(ans)
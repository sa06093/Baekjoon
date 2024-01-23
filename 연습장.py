btw_val = [2, 3]

for i in range(min(btw_val), 0, -1):
    count = 0
    for j in btw_val:
        if j % i == 0:
            count += 1

    if count == len(btw_val):
        ans = i
        break

print(ans)
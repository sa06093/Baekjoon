import sys

n, m = map(int, sys.stdin.readline().split())

dict_s = {}
count = 0

for i in range(n):
    string = str(sys.stdin.readline())
    dict_s[string] = 0

for j in range(m):
    judge = str(sys.stdin.readline())
    if judge in (key for key in dict_s.keys()):
        count += 1
        
print(count)
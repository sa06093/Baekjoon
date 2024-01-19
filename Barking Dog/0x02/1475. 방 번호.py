n = int(input())
for i in range(0, n):
    print(" " * i, end="")
    print("*" * (2*n-2*i-1))
    
for i in range(n-2, -1, -1):
    print(" " * i, end="")
    print("*" * (2*n-2*i-1))
    

    9
    7
    5
    3
    1
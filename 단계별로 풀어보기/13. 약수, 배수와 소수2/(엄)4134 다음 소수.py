import sys
import math

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True

n = int(sys.stdin.readline())

for _ in range(n):
    case = int(sys.stdin.readline())
    while True:
        if is_prime(case):
            print(case)
            break
        else:
            case += 1
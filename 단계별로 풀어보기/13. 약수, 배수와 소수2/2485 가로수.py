import sys

n = int(sys.stdin.readline())

place = []
btw_val = []

for i in range(n):
    place.append(int(sys.stdin.readline()))

for i in range(len(place)-1):
    btw_val.append(place[i + 1] - place[i])


# 유클리드 호제법 함수
def find_gcd(x, y):
    while y:
        x, y = y, x % y
    return x

# 함수를 사용해 최대공약수 구하기
gcd_val = btw_val[0]
for val in btw_val[1:]:
    gcd_val = find_gcd(gcd_val, val)

result_list = [(x // gcd_val) - 1 for x in btw_val]
print(sum(result_list))
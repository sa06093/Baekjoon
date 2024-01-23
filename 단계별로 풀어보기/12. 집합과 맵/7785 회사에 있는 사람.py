import sys

n = int(sys.stdin.readline())

state_dict = {}

for i in range(n):
    name, state = map(str, sys.stdin.readline().split())
    state_dict[name] = state

left_list = []

for i in state_dict.keys():
    if state_dict[i] == 'enter':
        left_list.append(i)

ans_list = sorted(left_list, reverse=True)

for i in ans_list:
    print(i)
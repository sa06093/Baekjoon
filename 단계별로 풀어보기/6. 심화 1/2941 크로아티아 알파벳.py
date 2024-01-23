string = input()

count = 0
a_list = ['dz=', 'c=', 'c-', 'd-', 'lj', 'nj', 's=', 'z=']
i = 0

while i < len(a_list):
    if a_list[i] in string:
        count += 1
        string = string.replace(a_list[i], ",", 1)
    else:
        i += 1

string = string.replace(",", "")
print(count + len(string))
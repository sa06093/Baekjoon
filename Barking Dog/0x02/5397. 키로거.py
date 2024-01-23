l = int(input())

for i in range(l):
    a = input()
    cursor = 0

    result = []

    for char in a:
        if char == '<':
            cursor = max(0, cursor - 1)
        elif char == '>':
            cursor = min(len(result), cursor + 1)
        elif char == '-':
            if cursor > 0:
                result.pop(cursor - 1)
                cursor -= 1
        else:
            result.insert(cursor, char)
            cursor += 1

    print("".join(result))
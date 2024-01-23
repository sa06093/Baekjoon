l = int(input())
 

for i in range(l):
    lista = []
    ans_list = ['|']
    a = str(input())
    for i in range(len(a)):
        lista.append(a[i])
    
    for i in range(len(lista)):
        if lista[i] == '<':
            if ans_list[0] == '|':
                pass
            else:
                place = ans_list.index('|')
                ans_list = ans_list[0:place-1] + list('|') + list(str(ans_list[place-1])) + ans_list[place+1:]

        elif lista[i] == '>':
            if ans_list[-1] == '|':
                pass
            else:
                place = ans_list.index('|')
                ans_list = ans_list[0:place]  + list(str(ans_list[place + 1])) + list('|') + ans_list[place+2:]
        elif lista[i] == '-':
            place = ans_list.index('|')
            if place == 0:
                pass
            else:
                ans_list = ans_list[0:place-1] + list('|') + ans_list[place + 1:]
        else:
            place = ans_list.index('|')
            ans_list = ans_list[0:place] + list(str(lista[i])) + list('|') + ans_list[place + 1:]
    place = ans_list.index('|')
    answer = ans_list[0:place] + ans_list[place + 1:]
    result = ''.join(i for i in answer)
    print(result)
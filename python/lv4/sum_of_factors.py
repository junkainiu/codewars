def sum_for_list(lst):
    result = []
    an = []
    for index,elem in enumerate(lst):
        i = 2
        while abs(elem) > 1:
            while elem%i == 0:
                elem = elem/i
                if not [i,index] in result:
                    result.append([i,index])
            i += 1
    keys = sorted(list(set([a[0] for a in result])))
    for elem in keys:
        r = 0
        for value in result:
            if value[0] == elem:
                r += lst[value[1]]
        an.append([elem,r])
    return an


sum_for_list([15, 21, 24, 30, -45])

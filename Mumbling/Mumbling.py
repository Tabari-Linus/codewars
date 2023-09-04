def accum(s):
    lenght = len(s)
    s_to_list = list(s)
    results = ''
    for i in range(lenght):
        code = (i+1)* s_to_list[i]
        if lenght == 1 or i == 0:
            results = results+code.capitalize()
        else:
            results = results+"-"+code.capitalize()
    return results


print(accum("RqaEzty"))
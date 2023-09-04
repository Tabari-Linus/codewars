def accum(s):
    s_to_list = list(s)
    results = ''
    for i in range(len(s)):
        code = (i+1)* s_to_list[i]
        if len(s) == 1 or i == 0:
            results = results+code.capitalize()
        else:
            results = results+"-"+code.capitalize()
    return results


print(accum("RqaEzty"))
# return masked string
def maskify(cc):

    if len(cc) < 4:
        return cc
    else:
        cc_arr = list(cc)
        for i in range(len(cc)-4):
            cc_arr[i]= '#'
        cc = ''.join(cc_arr)
        return cc

def maskify_alt(cc):

    length = len(cc)
    return '#'*(length-4)+cc[-4:]
    

print(maskify("64607935616"))
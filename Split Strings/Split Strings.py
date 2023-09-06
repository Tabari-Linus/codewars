def solution(s):
    s_list = list(s)
    length = len(s_list)
    results = []
    count = 0
    for i in range(0,length, 2):
        results[count] = ''.join([s_list[i],s_list[i+1]])
        ++count
    # if length % 2 == 1:
    #     results[len(results)]
        
    return results


print(solution('abcdef'))
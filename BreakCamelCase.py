def solution(s):
    ###First solution
    # count = 0
    # x=1
    # start =count
    # words = []
    # res =False
    # for letter in s:
    #     if letter.isupper():
    #         res =True
    #         words.append(s[start:count])
    #         start = count
    #     count+=1
    # words.append(s[start:])
    # print(words)
    # if len(s) <1:
    #     return s
    # elif res:
    #     return " ".join(words)
    # else:
    #     return s
    
    if len(s)<1:
        return s
    Words = []
    start = 0
    for i, letter in enumerate(s):
        if letter.isupper():
            Words.append(s[start:i])
            start = i
    Words.append(s[start:])
    return " ".join(Words) if len(Words) > 1 else s
print(solution("breakCamelCase"))
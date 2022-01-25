def solution(s):
    if(len(s)%2 != 0):
        return 0
    while(True):
        find = False
        for i in range(1, len(s)):
            if(s[i] == s[i-1]):
                s = s[0:i-1] + s[i+1:len(s)]
                find = True
                break
        if(find == False):
            break
    if(len(s) == 0):
        return 1
    return 0
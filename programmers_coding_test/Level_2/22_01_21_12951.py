def solution(s):
    s_len = len(s)
    s = s[0].upper() + s[1:s_len]
    for i in range(1, s_len):
        if(s[i-1] == " "):
            s = s[0:i] + s[i].upper() + s[i+1:s_len]
        else:
            s = s[0:i] + s[i].lower() + s[i+1:s_len]
    return s
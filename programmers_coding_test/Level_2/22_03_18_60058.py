def balance(s):
    if s == "":
        return ""
    temp1 = 0
    temp2 = 0
    u = ""
    v = ""
    for i in range(len(s)):
        u += s[i]
        if s[i] == '(':
            temp1 += 1
        if s[i] == ')':
            temp2 += 1
        if temp1 == temp2:
            if i != len(s)-1:
                v += s[i+1:len(s)]
            break
    temp1 = u
    for i in range(len(u)//2):
        temp2 = temp1.find("()")
        if temp2 == -1:
            break
        temp1 = temp1[:temp2] + temp1[temp2+1:]
        temp1 = temp1[:temp2] + temp1[temp2+1:]
    if temp1 == "":
        return u + balance(v)
    else:
        temp1 = "(" + balance(v) + ")"
        for i in range(1, len(u)-1):
            if u[i] == "(":
                temp1 += ")"
            else:
                temp1 += "("
        return temp1

def solution(p):
    return balance(p)

print(solution("()))((()"))
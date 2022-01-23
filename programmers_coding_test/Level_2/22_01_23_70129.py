def solution(s):
    count1 = 0
    count2 = 0
    while(True):
        if(s == "1"):
            break
        temp = s.replace("0", "")
        count2 += (len(s) - len(temp))
        s = bin(len(temp))
        s = s[2:len(s)]
        count1 += 1
    return [count1, count2]
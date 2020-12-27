def distance(n, l):#n부터 l까지 거리
    if(n==2):
        if(l==2):
            return 0
        elif(l==1 or l==3 or l==5):
            return 1
        elif(l==4 or l==6 or l==8):
            return 2
        elif(l==7 or l==0 or l==9):
            return 3
        else:
            return 4
    elif(n==5):
        if(l==5):
            return 0
        elif(l==2 or l==4 or l==6 or l==8):
            return 1
        elif(l==1 or l==3 or l==7 or l==9 or l==0):
            return 2
        else:
            return 3
    elif(n==8):
        if(l==8):
            return 0
        elif (l == 0 or l == 5 or l == 7 or l == 9):
            return 1
        elif (l==2 or l==4 or l==6 or l=="*" or l=="#"):
            return 2
        else:
            return 3
    elif(n==0):
        if(l==0):
            return 0
        elif(l==8 or l=="*" or l=="#"):
            return 1
        elif(l==5 or l==7 or l==9):
            return 2
        elif(l==2 or l==4 or l==6):
            return 3
        else:
            return 4
def solution(numbers, hand):
    answer = ''
    leri = ["*", "#"]
    for i in numbers:
        if(i==1 or i==4 or i==7):
            answer+="L"
            leri[0] = i
        elif(i==3 or i==6 or i==9):
            answer+="R"
            leri[1] = i
        else:
            if(distance(i, leri[0])<distance(i, leri[1])):
                answer+="L"
                leri[0] = i
            elif(distance(i, leri[0])>distance(i, leri[1])):
                answer+="R"
                leri[1] = i
            else:
                if(hand=="left"):
                    answer+="L"
                    leri[0] = i
                else:
                    answer+="R"
                    leri[1] = i
        print(leri)
    return answer

print(solution([1, 2, 3, 4, 5, 6, 7, 8, 9, 0], "right"))
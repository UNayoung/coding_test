def solution(n, words):
    answer = []
    order = 0
    list = dict()
    list[words[0]] = 1
    list_order = [words[0]]
    for i in range(1, len(words)):
        if(list.get(words[i]) != None or list_order[i-1][len(list_order[i-1])-1] != words[i][0]):
            print(words[i])
            print(list_order[i-1])
            order = i+1
            break
        list[words[i]] = 1
        list_order.append(words[i])
    if(order == 0):
        return [0, 0]
    elif(order%n == 0):
        answer.append(n)
    else:
        answer.append(order%n)
    answer.append(((order-1)//n)+1)
    return answer
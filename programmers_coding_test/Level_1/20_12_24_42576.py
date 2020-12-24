def solution(participant, completion):
    answer = ''
    answer = list(set(participant)-set(completion))
    if(answer!=[]):
        return answer[0]
    else:
        for i in participant:
            c1 = participant.count(i)
            if(c1>=2):
                c2 = completion.count(i)
                print(c1)
                print(c2)
                if(c1!=c2):
                    return i

print(solution(["mislav", "stanko", "mislav", "ana"], ["stanko", "ana", "mislav"]))
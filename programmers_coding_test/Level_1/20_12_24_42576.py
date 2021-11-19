# def solution(participant, completion):
#     answer = ''
#     answer = list(set(participant)-set(completion))
#     if(answer!=[]):
#         return answer[0]
#     else:
#         for i in participant:
#             c1 = participant.count(i)
#             if(c1>=2):
#                 c2 = completion.count(i)
#                 # print(c1)
#                 # print(c2)
#                 if(c1!=c2):
#                     return i

# print(solution(["mislav", "stanko", "mislav", "ana"], ["stanko", "ana", "mislav"]))

# def solution(participant, completion):
#     answer = ''
#     for i in completion:
#         for j in range(len(participant)):
#             if(participant[j]==i):
#                 participant.pop(j)
#                 break
#     answer = participant[0]
#     return answer
#
# print(solution(["mislav", "stanko", "mislav", "ana"], ["stanko", "ana", "mislav"]))

import collections

def solution(participant, completion):
    # participant.sort()
    # completion.sort()
    # print(collections.Counter(participant))
    # print(collections.Counter(completion))
    result = collections.Counter(participant) - collections.Counter(completion)
    # print(list(result)[0])
    return list(result)[0]

print(solution(["mislav", "stanko", "mislav", "ana"], ["stanko", "ana", "mislav"]))

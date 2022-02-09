from itertools import combinations

people = int(input())
member = []
for i in range(people):
    member.append(i)
arr = [list(map(int, input().split())) for _ in range(people)]
combine = list(combinations(member, people//2))
result = []

for i in range(len(combine)//2):
    sum1 = 0
    sum2 = 0
    for j in combine[i]:
        for k in combine[i]:
            sum1 += arr[j][k]
    for j in combine[len(combine)-i-1]:
        for k in combine[len(combine)-i-1]:
            sum2 += arr[j][k]
    result.append(abs(sum1-sum2))
    if ((sum1 - sum2) == 0):
        break

print(min(result))
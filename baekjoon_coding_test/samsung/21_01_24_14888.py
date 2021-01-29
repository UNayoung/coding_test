import itertools
import math

count = input()
num = list(map(int, input().split()))
operator = list(map(int, input().split()))

operator_list = []
result = []

for i in range(operator[0]):
    operator_list.append(1)
for i in range(operator[1]):
    operator_list.append(2)
for i in range(operator[2]):
    operator_list.append(3)
for i in range(operator[3]):
    operator_list.append(4)

calculate_list = set(itertools.permutations(operator_list, len(operator_list)))

for i in calculate_list:
    sum = num[0]
    for j in range(len(i)):
        if(i[j]==1):
            sum = sum+num[j+1]
        elif(i[j]==2):
            sum = sum-num[j+1]
        elif(i[j]==3):
            sum = sum*num[j+1]
        else:
            sum = sum/num[j+1]
            sum = math.trunc(sum)
    result.append(sum)

print(max(result))
print(min(result))

# itertools - 순열, 조합
# eval() - 문자열 계산 툴
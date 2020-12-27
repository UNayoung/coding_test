a, b = map(int, input().strip().split(' '))
width = ''
for j in range(0, a):
    width+='*'
for i in range(0, b):
    print(width)
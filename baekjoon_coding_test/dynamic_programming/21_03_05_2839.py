def main():
    n = input()
    n = int(n)
    result = 0
    while(True):
        if(n<0):
            result = -1
            break
        elif(n%5==0):
            result += n//5
            break
        else:
            n = n - 3
            result += 1
    print(result)

main()
def solution(phone_book):
    phone_book.sort()
    for i in range(0, len(phone_book)-1):
        if phone_book[i] == phone_book[i + 1][0:len(phone_book[i])]:
            print()
            return False
    return True

print(solution(["119", "97674223", "1195524421"]))
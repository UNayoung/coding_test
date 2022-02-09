# def find_max_sum(numbers):
#     for k in range(2):
#         for i in range(len(numbers)-2-k):
#             if numbers[i] > numbers[i + 1]:
#                 temp = numbers[i]
#                 numbers[i] = numbers[i + 1]
#                 numbers[i + 1] = temp
#     return numbers[len(numbers)-1] + numbers[len(numbers)-2]
#
#
# if __name__ == "__main__":
#     print(find_max_sum([5, 9, 7, 11]))

def find_max_sum(numbers):
    numbers.sort()
    return numbers[len(numbers)-1] + numbers[len(numbers)-2]


if __name__ == "__main__":
    print(find_max_sum([5, 9, 7, 11]))
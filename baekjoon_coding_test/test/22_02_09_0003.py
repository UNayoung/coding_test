def find_all_hobbyists(hobby, hobbies):
    answer = []
    for i in hobbies:
        if hobby in hobbies[i]:
            answer.append(i)
    return answer


if __name__ == "__main__":
    hobbies = {
        "Steve": ['Fashion', 'Piano', 'Reading'],
        "Patty": ['Drama', 'Magic', 'Pets'],
        "Chad": ['Puzzles', 'Pets', 'Yoga']
    }

    print(find_all_hobbyists('Yoga', hobbies));
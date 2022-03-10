def solution(clothes):
    data = dict()

    for clothe in clothes:
        if clothe[1] not in data:
            data[clothe[1]] = 2
        else:
            data[clothe[1]] = data[clothe[1]] + 1
    answer = 1
    for value in data.values():
        answer *= value

    return answer - 1
'''
def solution(clothes):
    answer = 0
    data = dict()
    clothe_type = []

    for clothe in clothes:
        if clothe[1] not in data:
            data[clothe[1]] = 1
            clothe_type.append(clothe[1])
        else:
            data[clothe[1]] = data[clothe[1]] + 1
    counts = []

    if len(clothe_type) == 30:
        return 1073741823;

    for clothe in clothe_type:
        counts.append(data[clothe])
    data_combinations = []

    for i in range(len(clothe_type)):
        data_combinations += list(combinations(counts, i + 1))

    for numbers in data_combinations:
        value = 1
        for i in range(len(numbers)):
            value *= numbers[i]
        answer += value

    return answer
'''

print(solution([["yellowhat", "headgear"], ["bluesunglasses", "eyewear"], ["green_turban", "headgear"]]))
print(solution([["crowmask", "face"], ["bluesunglasses", "face"], ["smoky_makeup", "face"]]))

from functools import cmp_to_key

def compare(one, other):
    one_str = int(str(one) + str(other))
    other_str = int(str(other) + str(one))
    if one_str > other_str:
        return -1
    return 1

def sum_of_numbers_to_char(numbers):
    ret = ''
    for number in numbers:
        ret += str(number)

    return ret

def solution(numbers):
    numbers_sorted = sorted(numbers, key=cmp_to_key(compare))
    answer = sum_of_numbers_to_char(numbers_sorted)
    if answer[0] == '0':
        return '0'

    return answer


print(solution([2, 6, 10]))





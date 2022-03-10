from itertools import permutations
import math
def is_prime_number(number):
    if number <= 1:
        return False

    for i in range(2, int(math.sqrt(number) + 1)):
        if number % i == 0:
            return False
    return True

def solution(numbers):
    answer = 0
    number_array = []
    number_permutations = []
    for i in range(len(numbers)):
        number_array.append(numbers[i])

    for i in range(1, len(numbers) + 1):
        number_permutations = number_permutations + list(permutations(number_array, i))
    number_permutations = set(number_permutations)
    count = 0
    for number_str in number_permutations:
        if number_str[0] == '0' or number_str[len(number_str) - 1] == '0':
            continue
        number = int(''.join(number_str))
        if is_prime_number(number):
            count += 1
    return count

print(solution('929'))
print(solution('011'))
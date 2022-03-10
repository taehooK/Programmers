def find_left(target, string, current):
    i = current
    length = len(string)
    distance = 0

    while distance <= length:
        if target[i] != string[i]:
            return i, distance

        i -= 1
        if i < 0 :
            i = len(string) - 1
        distance += 1

    return -1, 0



def find_right(target, string, current):
    i = current
    length = len(string)
    distance = 0

    while distance <= length:
        if target[i] != string[i]:
            return i, distance

        i += 1
        if i >= len(string):
            i = 0
        distance += 1

    return -1, 0

def get_min_cost_change(target):
    left = int(ord('Z') - ord(target)) + 1
    right = int(ord(target) - ord('A'))

    return min(left, right)


def solution(name):
    answer = 0
    current = 0
    name_string = []
    for i in range(len(name)):
        name_string.append(name[i])
    string = ['A' for _ in range(len(name))]

    while True:
        left_index, left_cost = find_left(name_string, string, current)
        right_index, right_cost = find_right(name_string, string, current)
        if left_index == -1:
            break
        index = right_index
        cost = right_cost
        if left_cost < right_cost:
            index = left_index
            cost = left_cost

        string[index] = name_string[index]
        answer += cost + get_min_cost_change(name_string[index])
        current = index

    return answer

print(solution("ABAAAAAAAAABB"))
print(solution("BBBBAAAAAB"))
print(solution("BBBBAAAABA"))
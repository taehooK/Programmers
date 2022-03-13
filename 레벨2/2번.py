clockwise_array = [(1, 0), (0, 1), (-1, 0), (0, -1)]  # 우측-아래-좌측-위
anticlockwise_array = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # 아래-우측-위-좌측

def get_next_direct(current_direct, is_clockwise):
    next_direct = (0, 0)
    if is_clockwise:
        i = 0
        while i < len(clockwise_array):
            if current_direct == clockwise_array[i]:
                next_index = i + 1
                if next_index >= len(clockwise_array):
                    next_index = 0

                next_direct = clockwise_array[next_index]
                break
            i += 1
    else:
        i = 0
        while i < len(anticlockwise_array):
            if current_direct == anticlockwise_array[i]:
                next_index = i + 1
                if next_index >= len(anticlockwise_array):
                    next_index = 0
                next_direct = anticlockwise_array[next_index]
                break
            i += 1
    return next_direct
def solution(n, clockwise):
    answer = [[0] * n for _ in range(n)]
    if n == 1:
        answer[0][0] = 1
        return answer

    positions = [(0, 0), (n - 1, 0), (n - 1, n - 1), (0, n - 1)]  # x, y
    direct = [(1, 0), (0, 1), (-1, 0), (0, -1)]  # x, y

    if clockwise == False:
        positions = [(0, 0), (0, n -1), (n - 1, n - 1), (n - 1, 0)]
        direct = [(0, 1), (1, 0), (0, -1), (-1, 0)]

    for position in positions:
        answer[position[1]][position[0]] = 1

    stopCount = 0
    while stopCount < 3:
        i = 0
        while i < len(positions):
            row = positions[i][1]
            column = positions[i][0]
            current = answer[row][column]

            next_row = row + direct[i][1]
            next_column = column + direct[i][0]
            next = answer[next_row][next_column]

            if next != 0 and next < current:
                next_direct = get_next_direct(direct[i], clockwise)
                direct[i] = next_direct #방향 변경
                next_row = row + direct[i][1]
                next_column = column + direct[i][0]
                next = answer[next_row][next_column]

            if next >= current:
                stopCount += 1
                i += 1
                continue
            answer[next_row][next_column] = current + 1
            positions[i] = (next_column, next_row)

            i += 1

    return answer


def print_array(array):
    for i in range(len(array)):
        for j in range(len(array)):
            print(array[i][j], end=' ')
        print()

print_array(solution(1, False))
print()


print_array(solution(6, False))
print()

print_array(solution(9, False))
print()

print_array(solution(9, True))
print()
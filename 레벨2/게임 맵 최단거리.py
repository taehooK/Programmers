from collections import deque

def solution(maps):
    n = len(maps)
    m = len(maps[0])

    rowOffset = [-1, 1, 0, 0]
    columnOffset = [0, 0, -1, 1]

    queue = deque()
    queue.appendleft((0, 0))

    while queue:
        row, column = queue.pop()

        for i in range(4):
            next_row = row + rowOffset[i]
            next_column = column + columnOffset[i]

            if 0 <= next_row < n and 0 <= next_column < m and maps[next_row][next_column] == 1:
                queue.appendleft((next_row, next_column))
                maps[next_row][next_column] = maps[row][column] + 1



    # 우측 하단이 1이면 -1출력
    # 이외에는 그냥 출력
    answer = maps[n - 1][m - 1]
    if answer == 1:
        answer = -1

    return answer


maps = [[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,1],[0,0,0,0,1]]

print(solution(maps))
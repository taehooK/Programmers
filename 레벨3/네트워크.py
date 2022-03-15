from collections import deque
def solution(n, computers):
    queue = deque()
    ret = 0
    visited = dict()

    for i in range(n):
        if i in visited:
            continue
        visited[i] = True
        queue.append(i)
        while queue:
            node = queue.popleft()
            for neighbor in range(n):
                if neighbor in visited or computers[node][neighbor] == 0:
                    continue
                visited[neighbor] = True
                queue.append(neighbor)
        ret += 1

    return ret

print(solution(3, [[1, 1, 0], [1, 1, 0], [0, 0, 1]]))
print(solution(3, [[1, 1, 0], [1, 1, 1], [0, 1, 1]]))
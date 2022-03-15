from collections import deque

def bfs(graph, start):
    queue = deque()
    visited = dict()
    queue.append(start)
    number_of_distance = [0] * len(graph)

    visited[start] = True

    while queue:
        node_index = queue.popleft()
        distance = number_of_distance[node_index]

        for neighbor_node in graph[node_index]:
            if neighbor_node in visited:
                continue
            visited[neighbor_node] = True
            number_of_distance[neighbor_node] = distance + 1
            queue.append(neighbor_node)
    max_value = max(number_of_distance)
    ret = number_of_distance.count(max_value)

    return ret

def solution(n, edge):
    #노드 개수만큼 2차원 배열 생성
    graph = [[] for i in range(n)]
    #edge 수만큼 반복 간선연결
    for e in edge:
        graph[e[0] - 1].append(e[1] - 1)
        graph[e[1] - 1].append(e[0] - 1)
    ret = bfs(graph, 0)

    return ret

print(solution(6, [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]))

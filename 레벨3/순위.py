def dfs(graph, visited, index):
    visited[index] = True
    count = 0
    for opponent in graph[index]:
        if opponent not in visited:
            count += dfs(graph, visited, opponent)
            count += 1
    return count

def solution(n, results):
    answer = 0

    victory_graph = [[] for i in range(n)]
    loose_graph = [[] for i in range(n)]
    win_data = [-1] * n
    loose_data = [-1] * n

    for result in results:
        winner = result[0] - 1
        looser = result[1] - 1
        victory_graph[winner].append(looser)
        loose_graph[looser].append(winner)

    for i in range(n):
        visited = dict()
        win_data[i] = dfs(victory_graph, visited, i)
        visited.clear()
        loose_data[i] = dfs(loose_graph, visited, i)

    # 두 조건의 인원이 n-1 보다 크거나 같으면 순위 파악 가능
    for i in range(n):
        if win_data[i] + loose_data[i] >= n - 1:
            answer += 1

    return answer

print(solution(3, [[1, 2], [1, 3]])) # 2
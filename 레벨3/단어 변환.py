from collections import deque
def possible_change(from_str, to_str):
    length = len(from_str)
    uncorrect_count = 0

    for i in range(length):
        if from_str[i] != to_str[i]:
            uncorrect_count += 1
        if uncorrect_count > 1:
            return False

    return True
def solution(begin, target, words):
    queue = deque()
    visited = dict()

    queue.append(begin)
    visited[begin] = True
    current_level_append_count = 1
    level = 0
    while queue:
        count = 0
        i = 0
        while i < current_level_append_count:
            string = queue.popleft()
            if string == target:
                return level
            for word in words:
                if word not in visited and possible_change(string, word):
                    queue.append(word)
                    visited[word] = True
                    count += 1
            i += 1
        current_level_append_count = count
        level += 1

    return 0

print(solution('hit', 'cog', ["hot", "dot", "dog", "lot", "log", "cog"]))
print(solution('hit', 'cog', ["hot", "dot", "dog", "lot", "log"]))
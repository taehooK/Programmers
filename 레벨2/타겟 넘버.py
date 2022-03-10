global count

def dfs(numbers, target, index, sum):
    global count
    # 종료조건
    if index >= len(numbers):
        if sum == target:
            count += 1
        return
    # 수행문
    dfs(numbers, target, index + 1, sum + numbers[index])
    dfs(numbers, target, index + 1, sum - numbers[index])

def solution(numbers, target):
    global count
    count = 0
    dfs(numbers, target, 0, 0)
    return count
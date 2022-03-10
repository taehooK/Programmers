from collections import deque


def solution(progresses, speeds):
    answer = []

    speed_index = 0
    day = 1
    queue = deque(progresses)

    while queue:
        temp = deque()
        for index in range(speed_index, len(speeds)):
            progress = queue.popleft()
            progress += speeds[index]
            temp.append(progress)

        queue = temp
        count = 0
        while queue:
            progress = queue.popleft()
            if progress >= 100:
                count += 1
                speed_index += 1
            else:
                progress = queue.appendleft(progress)
                break
        if count > 0:
            answer.append(count)

    # 큐가 빌때까지 반복
    # n일차 진행한다.
    # 100% 진행된 프로그래스를 센다.
    # 1개 이상이면 정답배열에 넣는다.

    return answer

print(solution([95, 90, 99, 99, 80, 99],[1, 1, 1, 1, 1, 1]))
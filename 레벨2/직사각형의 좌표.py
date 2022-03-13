def solution(v):
    answer = []
    # 사이에 있는 점 찾기
    # 점과 다른점의 좌표비교 - 좌표값이 다르면 그 값이 나머지 점좌표
    other_dots = []
    between_dot = [0, 0]
    for dot in v:
        i = 0
        while i < len(v):
            if dot[0] != v[i][0] and dot[1] != v[i][1]:
                other_dots.append(dot)
                break
            i += 1
        if i >= len(v):
            between_dot = dot

    for dot in other_dots:
        if between_dot[0] != dot[0]:
            answer.insert(0, dot[0])
        else:
            answer.append(dot[1])
    return answer

print(solution([[1, 1], [2, 2], [1, 2]]))
print(solution([[1, 1], [2, 2], [2, 1]])) # (1,2)
print(solution([[1, 1], [2, 1], [1, 2]])) # 2,2
print(solution([[2, 1], [2, 2], [1, 2]])) # 1,1
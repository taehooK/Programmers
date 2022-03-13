def solution(answers):
    answer = []

    answer_styles = [[1, 2, 3, 4, 5], [2, 1, 2, 3, 2, 4, 2, 5], [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]]
    indexes = [0, 0, 0]
    scores = [0, 0, 0]

    for i in range(len(answers)):
        for j in range(len(answer_styles)):
            if answer_styles[j][indexes[j]] == answers[i]:
                scores[j] += 1
            indexes[j] = (indexes[j] + 1) % len(answer_styles[j])

    max_score = max(scores)
    index = 0

    for score in scores:
        if score >= max_score:
            answer.append(index + 1)
        index += 1

    return answer
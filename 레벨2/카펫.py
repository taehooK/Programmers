def solution(brown, yellow):
    answer = []

    yellow_width = yellow
    yellow_height = 1

    while yellow_width >= yellow_height:
        brown_count = (yellow_width + 2) * (yellow_height + 2) - yellow
        if brown_count == brown:
            answer.append(yellow_width + 2)
            answer.append(yellow_height + 2)
            break

        yellow_width -= 1
        while yellow_width >= yellow_height:
            if yellow % yellow_width == 0:
                yellow_height = yellow // yellow_width
                break
            yellow_width -= 1

    return answer
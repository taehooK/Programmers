def solution(money):
    answer = 0
    #점화식
    #dp[0] = array[0]
    #dp[1] = array[1]
    # i >= 2 인 경우
    #dp[i] = max(dp[i - 1], dp[i - 2] + array[i])

    dp_one = [0] * (len(money) - 1)
    dp_other = [0] * (len(money) - 1)

    dp_one[0] = money[0]
    dp_one[1] = max(dp_one[0], money[1])

    for i in range(2, len(money) - 1):
        dp_one[i] = max(dp_one[i - 1], dp_one[i - 2] + money[i])

    dp_other[0] = money[1]
    dp_other[1] = max(dp_other[0], money[2])

    for i in range(3, len(money)):
        dp_other[i - 1] = max(dp_other[i - 2], dp_other[i - 3] + money[i])


    return max(dp_one[len(money) - 2], dp_other[len(money) - 2])

print(solution([1, 2, 3, 1])) # 4
print(solution([1, 6, 4, 8, 10])) # 13
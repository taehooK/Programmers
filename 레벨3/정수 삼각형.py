def solution(triangle):
    answer = 0
    dp = [[0] * len(triangle[i]) for i in range(len(triangle))]

    for i in range(len(triangle)):
        for j in range(len(triangle[i])):
            leftTop = 0
            rightTop = 0
            if i - 1 >= 0 and j - 1 >= 0:
                leftTop = dp[i - 1][j - 1]
            if i - 1 >= 0:
                rightTop = dp[i - 1][j]
            dp[i][j] = max(dp[i][j], triangle[i][j] + max(leftTop, rightTop))

    return max(dp[len(dp) - 1])
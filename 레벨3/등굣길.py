def solution(m, n, puddles):
    answer = 0
    #점화식 m(i, k) = m(i-1,k) + m(i, k-1)
    dp = [[0 for j in range(m)] for i in range(n)]
    dp[0][0] = 1

    for puddle in puddles:
        dp[puddle[1] - 1][puddle[0] - 1] = -1

    for i in range(n):
        for j in range(m):
            if dp[i][j] == -1:
                dp[i][j] = 0
            else:
                if i - 1 >= 0:
                    dp[i][j] += dp[i - 1][j]
                if j - 1 >= 0:
                    dp[i][j] += dp[i][j - 1]

    return dp[n - 1][m - 1]

print(solution(4, 3, [[2, 2,]]))


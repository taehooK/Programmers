def solution(money, costs):
    dp = [1000001] * (money + 1)
    dp[0] = 0

    temp = [1, 5, 10, 50, 100, 500]
    costs_array = []
    i = 0
    for cost in costs:
        costs_array.append((cost, temp[i]))
        i += 1

    costs_array.sort()

    for i in range(len(costs_array)):
        for j in range(1, money + 1):
            if j - costs_array[i][1] >= 0 and dp[j - costs_array[i][1] != 1000001]:
                dp[j] = min(dp[j], dp[j - costs_array[i][1]] + costs_array[i][0])

    return dp[money]

print(solution(500, [2, 11, 20, 100, 200, 1]))
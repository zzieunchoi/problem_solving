def solution(triangle):
    answer = 0
    n = len(triangle)
    dp = [[0]*n for _ in range(n)]
    dp[0][0] = triangle[0][0]
    
    for i in range(1, n):
        for j in range(0, len(triangle[i])):
            if j == 0:
                # 그냥 더해
                dp[i][j] = dp[i-1][j] + triangle[i][j]
            elif j == i:
                # 그냥 더해
                dp[i][j] = dp[i-1][j-1] + triangle[i][j]
            else:
                # max 한 걸로 더해
                dp[i][j] = max(dp[i-1][j-1], dp[i-1][j]) + triangle[i][j]
    answer = max(dp[n-1])
    return answer
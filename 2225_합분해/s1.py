import sys
sys.stdin = open('input.txt','r')

n, k = map(int, input().split())

dp = [[0]* 201 for _ in range(201)]

for i in range(201):
    dp[1][i] =1
    dp[2][i] =i+1

for j in range(3, 201):
    dp[j][1] =j
    for m in range(2, 201):
        dp[j][m] = (dp[j][m-1] + dp[j-1][m]) % 1000000000

print(dp[k][n])

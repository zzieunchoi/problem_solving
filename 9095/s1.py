import sys
sys.stdin = open('input.txt','r')

T = int(input())
for t in range(1, T+1):
    n= int(input())
    dp = [0] * 11

    dp[1] = 1
    dp[2] = 2
    dp[3] = 4

    for k in range(4, n+1):
        dp[k] = dp[k-1] + dp[k-2] + dp[k-3]

    print(dp[n])
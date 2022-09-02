import sys
sys.stdin= open('input.txt','r')

n= int(input())

dp = [0] * 1001

dp[1] = 1
dp[2] = 3

for k in range(3, n+1):
    dp[k] = dp[k-1] + 2 * (dp[k-2])

print(dp[n] % 10007)
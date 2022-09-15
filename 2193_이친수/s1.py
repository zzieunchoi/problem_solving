import sys
sys.stdin= open('input.txt','r')

n= int(input())
dp = list([0]*2 for _ in range(91))

dp[1] = [0,1]
for k in range(2, 91):
    dp[k] = [sum(dp[k-1]), dp[k-1][0]]

print(sum(dp[n]))
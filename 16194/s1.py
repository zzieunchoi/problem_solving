import sys
sys.stdin = open('input.txt','r')

n= int(input())
cards = [0] + list(map(int, input().split()))

dp = [0] * (n+1)
dp[1] = cards[1]
dp[2] = min(cards[1] * 2, cards[2])

for k in range(3, n+1):
    dp[k] = cards[k]
    for m in range(1, k//2 +1):
        dp[k] = min(dp[k], dp[m]+dp[k-m])
print(dp[n])
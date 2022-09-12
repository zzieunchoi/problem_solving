import sys
sys.stdin = open('input.txt','r')


dp = list([0]* 10 for _ in range(101))
dp[1] = [0, 1, 1, 1, 1, 1, 1, 1, 1, 1]

for i in range(2, 101):
    for j in range(0, 10):
        if j == 0:
            dp[i][0] = dp[i-1][1]
        elif j == 9:
            dp[i][9] = dp[i-1][8]
        else:
            dp[i][j] = dp[i-1][j-1] + dp[i-1][j+1]
            

n = int(input())
print(sum(dp[n]) % 1000000000)

import sys
sys.stdin = open('input.txt','r')

n= int(input())
# dp = [0, 1, 2, 3, 4, 5 ....]
dp = [x for x in range(n+1)]

# i가 4일 때, 제곱근인 2의 제곱으로 나타날 수 있음
# i가 8일 때, 2^2 + 2^2으로 나타날 수 있음
# i가 9일 때, 제곱근인 3의 제곱으로 나타날 수 있음 ...

# 따라서 경우의 수는 
# 1) i가 누군가의 제곱일 때 
# 2) i가 누군가의 제곱으로 최소의 값을 나타낼 수 있는 수 일때
for i in range(1, n+1):
    for j in range(1, i):
        if j*j > i :
            break
        # 뒤에 1을 붙이는 이유는 x^2으로 나타내는 경우의 수를 더하기 위해
        if dp[i] > dp[i-j*j] +1:
            dp[i] = dp[i-j*j] +1

print(dp[n])
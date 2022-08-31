import sys
sys.stdin = open('input.txt','r')

N = int(input())
dp = [0] * 1000001

for i in range(2, N+1):
    # 1을 뺄 경우를 생각
    dp[i] = dp[i-1] + 1
    # 숫자가 3으로 나눠질 경우
    if i % 3 == 0:
        # 1로 뺀 것과, 3으로 나눠서 그 다음 단계로 넘어간 숫자 중 작은 것!
        dp[i] = min(dp[i], dp[i//3]+1)
    # 숫자가 2로 나눠질 경우
    if i % 2 == 0:
        # 1을 뺀 것과, 2로 나워서 그 다음 단계로 넘어간 숫자 중 작은 것!
        dp[i] = min(dp[i], dp[i//2] +1)


# for k in range(1, 11):
#     print(dp[k], k)

# 0 1
# 1 2
# 1 3
# 2 4
# 3 5
# 2 6
# 3 7
# 3 8
# 2 9
# 3 10

# 답은 dp[N]
print(dp[N])
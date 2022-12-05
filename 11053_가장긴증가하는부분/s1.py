import sys
sys.stdin = open('input.txt','r')

n = int(input())
nums = list(map(int,input().rsplit()))
dp = [0] * n

# i = 0, j = 0
# i = 1, j = 0, 1 
# i = 2, j = 0, 1, 2 ...
for i in range(0, n):
    print(dp)
    for j in range(i):
        if nums[i] > nums[j] and dp[i] < dp[j]:
            dp[i] = dp[j]
    dp[i] +=1
    # print(dp)

print(max(dp))




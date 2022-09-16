import sys
sys.stdin = open('input.txt','r')

n= int(input())
numbers= [0] + list(map(int, input().split()))
dp = [0]* (n+1)
v = [-1] * (n+1)
for i in range(1, n+1):
    for j in range(1, i, 1):
        if numbers[i] > numbers[i-j] and dp[i] < dp[i-j]:
            dp[i] = dp[i-j]
            v[i] = i-j
    dp[i] +=1

# v = [-1, -1, 1, -1, 2, 3, 4]
# dp = [0, 1, 2, 1, 3, 2, 4]

# 가장 긴 부분수열의 길이 
k = max(dp)
print(k)

# 부분 수열 출력
result = []

#  가장 긴 부분수열의 최종 값이 어디있는지 확인
max_idx = dp.index(k) # 6
while max_idx != -1:
    result.append(numbers[max_idx])
    max_idx = v[max_idx] 
r_result = result[::-1]
print(*r_result)

import sys
sys.stdin = open('input.txt','r')

# 순열 함수 구하기
def permute(arr, k):
    result = []
    if k == 0:
        return [[]]

    for j in range(len(arr)):
        elem = arr[j]
        for rest in permute(arr[:i] + arr[i+1:], k-1):
            if elem not in rest:
               result.append([elem] + rest)

    return result

n, m = map(int, input().split())

numbers = []
for i in range(1, n+1):
    numbers.append(i)

for list in permute(numbers,m):
    print(*list)


import sys
input = sys.stdin.readline

channel = int(input())
n = int(input())
numbers = list(map(int, input().split()))

# 처음 결과값은 100-> 원하는 채널까지 + , - 버튼 클릭하는 것
res = abs(channel- 100)

# 완탐
for i in range(1000001):
    k = str(i)
    for j in range(len(k)):
        if int(k[j]) in numbers:
            break
        elif j == len(k) -1:
            # 지금까지 리모컨 고장난 버튼에 구애 받지 않고 올 수 있었던 수 - 가려고 했던 채널 수 : + , - 를 누르는 수
            # + ex) 5426을 누르는 총 4번
            res = min(res, abs(int(k) - channel)+len(k))

print(res)
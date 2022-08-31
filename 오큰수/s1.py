import sys
sys.stdin= open('input.txt','r')

n= int(input())
list_n = list(map(int, input().split()))

for i in range(n-1):
    if list_n[i] == max(list_n):
        print(-1, end=" ")
    for j in range(i+1, n):
        if list_n[i] < list_n[j]:
            print(list_n[j], end = " ")
            break

print(-1, end=" ")
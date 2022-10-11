import sys
sys.stdin= open('input.txt','r')

T = int(input())
for t in range(T):
    m, n, x, y = map(int, input().split())
    x -=1
    y -=1
    year = x
    while year < m*n:
        if year % n == y:
            print(year+1) 
            break

        year += m
    if year % n != y:
        print(-1)
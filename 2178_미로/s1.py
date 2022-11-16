import sys
sys.stdin = open('input.txt','r')

n, m = map(int, input().split())
arr = [[0]* (m+1) for _ in range(n+1)]
print(arr)
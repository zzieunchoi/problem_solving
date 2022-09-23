import sys
sys.stdin = open('input.txt','r')

n = int(input())
arr = [list(input()) for _ in range(n)]

def cnt_candy(arr):
    maxx = 1
    for i in range(n):
        # 행만 count
        cnt = 1
        for j in range(n-1):
            if arr[i][j] == arr[i][j+1]:
                cnt+=1
            else:
                cnt = 1
            maxx = max(cnt, maxx)
    
        # 열만 count
        cnt = 1
        for j in range(n-1):
            if arr[j][i] == arr[j+1][i]:
                cnt +=1
            else:
                cnt = 1
            maxx = max(cnt, maxx)
    return maxx

ans = 0
for i in range(n):
    for j in range(n):
        # 자신의 오른쪽에 있는 데이터와 바꾸기
        if j+1<n:
            arr[i][j], arr[i][j+1] = arr[i][j+1], arr[i][j]
            # 바꾼 데이터로 사탕의 max 세기
            ccount = cnt_candy(arr)
            ans = max(ccount, ans)
            # 다시 원래대로 돌려놓기 
            arr[i][j], arr[i][j+1] = arr[i][j+1], arr[i][j]
    
        # 자신의 아래쪽에 있는 데이터와 바꾸기
        if i+1<n:
            arr[i][j], arr[i+1][j] = arr[i+1][j], arr[i][j]
            # 바꾼 데이터로 사탕의 max 세기
            ccount = cnt_candy(arr)
            ans = max(ccount, ans)
            # 다시 원래대로 돌려놓기
            arr[i][j], arr[i+1][j] = arr[i+1][j], arr[i][j]
        
print(ans)
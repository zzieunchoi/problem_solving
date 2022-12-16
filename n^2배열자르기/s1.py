def solution(n, left, right):
    answer = []
    ## 몫과 나머지 중 큰것의 +1을 하면 나오는 거였음.. 
    for i in range(left, right +1):
        answer.append(max(i//n, i%n)+1)
        

    # 너무 어렵게 생각한 듯
    # arr = [[0] * (n) for _ in range(n)]
    # for i in range(n):
    #     for j in range(n):
    #         arr[i][j] = max(i,j) +1
    # s_i , s_j = left//n, left%n
    # e_i, e_j = right//n, right%n
    # while True:
    #     if s_i == e_i and s_j == e_j:
    #         answer.append(arr[s_i][s_j])
    #         break
    #     answer.append(arr[s_i][s_j])
    #     if s_j == n-1:
    #         s_i = s_i+1
    #         s_j = 0
    #     else:
    #         s_j = (s_j+1) % n
    return answer
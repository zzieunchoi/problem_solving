def solution(citations):
    answer = 0
    citations.sort()
    citations = citations[::-1]
    
    for i in range(max(citations), 0, -1):
        cnt = 0
        for j in citations:
            if j >= i:
                cnt +=1
        if cnt >= i:
            answer = i
            break
        
    return answer
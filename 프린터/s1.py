from collections import deque 
def solution(priorities, location):
    answer = 0
    
    # 내 문서 위치 알리기
    my_doc = [0] * len(priorities)
    my_doc[location] = 1
    
    priorities = deque(priorities)
    
    # while 문
    while True:
        if my_doc == [] or max(my_doc) == 0:
            break
        if max(priorities) == priorities[0]:
            priorities.popleft()
            del my_doc[0]
            answer +=1
        else:
            priorities.append(priorities[0])
            my_doc.append(my_doc[0])
            priorities.popleft()
            del my_doc[0]
            
       
    return answer
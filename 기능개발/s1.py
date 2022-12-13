import math
def solution(progresses, speeds):
    answer = []
    llist = []

    for i in range(len(progresses)):
        llist.append(math.ceil((100 - progresses[i])/speeds[i]))
    print(llist)
    i= 0 
    while i < len(llist):
        cnt = 1
        for j in range(i+1, len(llist)):
            if llist[i]>= llist[j]:
                cnt +=1
            else:
                break
        answer.append(cnt)
        i += cnt
    return answer
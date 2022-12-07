def isokay(ss):
    isornot = 0
    stack = []
    for s in ss:
        if s== "[" or s=="(" or s=="{":
            stack.append(s)
        elif s== "]":
            if "[" in stack and stack[-1] == "[" :
                stack.pop()
            else:
                isornot =1
                break
        elif s== ")":
            if "(" in stack and stack[-1] == "(" :
                stack.pop()
            else:
                isornot =1
                break
        elif s=="}":
            if "{" in stack and stack[-1] == "{" :
                stack.pop()
            else:
                isornot =1
                break
    if stack != []:
        isornot =1
    return isornot
    

def solution(s):
    answer = 0
    llist = list(s)
    for i in range(len(llist)):
        a = llist[0]
        llist.pop(0)
        llist.append(a)
        whether = isokay(llist)
        if whether == 0:
            answer +=1
    return answer

def solution(operations):
    answer = []
    llist = []
    for oper in operations:
        if oper[0] == "I":
            llist.append(int(oper[2:]))
        elif oper[0] == "D":
            if llist == []:
                continue
            if oper[2:] == "-1":
                llist.remove(min(llist))
            elif oper[2:] == "1":
                llist.remove(max(llist))
    if llist == []:
        answer = [0,0]
    else :
        answer= [max(llist), min(llist)]
    return answer
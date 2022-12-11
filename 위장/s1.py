def solution(clothes):
    answer = 1
    ttype = []
    llist = []
    for i in range(len(clothes)):
        ttype.append(clothes[i][1])
        if clothes[i][1] not in llist:
            llist.append(clothes[i][1])
    style_list = []
    for style in llist:
        # print(ttype.count(style))
        style_list.append(ttype.count(style))
    print(style_list)
    for k in style_list:
        answer = answer *(1+k)
    answer = answer -1
    return answer
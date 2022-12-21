# import math
# def solution(str1, str2):
#     answer = 0
#     str1 = str1.lower()
#     str2 = str2.lower()
#     str1list = []
#     str2list = []
#     for i in str1:
#         if i.isalpha() == False:
#             str1 = str1.replace(i, '')
#     for i in range(len(str1)-1):
#         str1list.append(str1[i]+str1[i+1])
    
#     for i in str2:
#         if i.isalpha() == False:
#             str2 = str2.replace(i, '')
#     for i in range(len(str2)-1):
#         str2list.append(str2[i]+str2[i+1])
    
#     gyo = 0
#     intersection = list(set(str1list).intersection(str2list))
#     print(intersection)
#     hap = 0
#     union = list(set().union(str1list,str2list))
#     print(union)
#     answer = math.floor((len(intersection)/len(union))*65536)
#     return answer

def solution(str1, str2):
    answer = 0
    merge_str1 = []
    merge_str2 = []
    for i in range(1,len(str1)):
        temp = str1[i-1] + str1[i]
        if temp.isalpha() == True:
            merge_str1.append(temp.upper())
    for i in range(1,len(str2)):
        temp = str2[i-1] + str2[i]
        if temp.isalpha()==True:
            merge_str2.append(temp.upper())
    print(merge_str1, merge_str2)

    str_g = []
    for i in (set(merge_str1+merge_str2)):
        k = merge_str1.count(i)
        l = merge_str2.count(i)
        m = min(k,l)
        str_g.append(m)
    str_t = []
    for i in (set(merge_str1+merge_str2)):
        k = merge_str1.count(i)
        l = merge_str2.count(i)
        m = max(k,l)
        str_t.append(m)

    if sum(str_g) != 0 and len(str_t) != 0:
        answer = int((sum(str_g) / sum(str_t)) * 65536)
    elif sum(str_g) == 0 and len(str_t) != 0:
        return 0
    else:
        return 65536
    return answer
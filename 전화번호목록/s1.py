# def solution(phone_book):
#     answer = True
#     nope = 0
    
#     for i in range(0, len(phone_book)-1):
#         for j in range(i+1, len(phone_book)):
#             if len(phone_book[i]) > len(phone_book[j]) :
#                 continue
#             llen = len(phone_book[i])
#             if phone_book[j][0:llen] ==phone_book[i]:
#                 nope = 1
#                 break
#         if nope == 1:
#             break
#     print(nope)
#     if nope == 1:
#         answer = False
#     return answer

# def solution(phone_book):
#     phone_book.sort()
#     s = dict()
#     for p in phone_book:
#         for i in range(1, len(p)):
#             s[p[:i]] = 1
#     s = list(s)
#     for p in phone_book:
#         if p in s:
#             return False
#     return True

# 간단하게 풀지만 해시 x
def solution(p):

    p.sort()
    print(p)
    for i in range(len(p)-1): 
        if p[i] == (p[i+1])[:len(p[i])] : 
            return False

    return True
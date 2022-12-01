def tournament(n, a, b):
    for i in range(n):
        if 2**i >= a:
            expA = i
            break
    for j in range(expA, n):
        if 2**j >= b:
            expB = j
            break
    if expA == expB :
        number = 2**(expA-1)
        a = tournament(n-number, a-number, b-number)
    else:
        return expB
    return a

def solution(n,a,b):
    answer = 0
    big  = max(a,b)
    small = min(a, b)
    answer = tournament(n, small, big)

    return answer
def solution(people, limit):
    
    left = 0
    right = len(people) -1
    cnt = 0
    people.sort()
    people = people[::-1]
    
    while left <= right:
        if people[left] + people[right] > limit:
            cnt +=1
            left +=1
        else:
            cnt +=1
            left +=1
            right -=1
           
    return cnt
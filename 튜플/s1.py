def solution(s):
    answer = []
    result = []
    tuples = s[2:-2].split("},{")
    tuples.sort(key = lambda x : len(x))
    for tuple in tuples:
        temp = set(list(map(int, tuple.split(','))))
        a = list(temp.difference(set(result)))
        answer.append(a[0])
        result = result + list(temp.difference(set(result)))
    return answer
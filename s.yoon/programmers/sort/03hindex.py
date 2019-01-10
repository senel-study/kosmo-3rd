def solution(citations):
    reversed_arr = sorted(citations, key = lambda x: -x)
    h = 0
    cnt = 0
    for i in reversed_arr:
        if i>cnt:
            cnt+=1
            h+=1
        elif i==cnt:
            cnt+=1
        else:
            break
    return h

citations = [3, 0, 6, 1, 5]
citations = [3,3,3,4,4]

print(solution(citations))
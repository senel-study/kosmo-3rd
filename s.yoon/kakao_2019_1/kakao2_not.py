# 버블정렬이라 폐기용 코드

def failure(n, stages):
    total = len(stages)
    fail = []
    for i in range(1, n+1):
        challenger = stages.count(i)
        fail.append([challenger/total, i])
        total-=challenger
    fail.sort(reverse=True)
    while True:
        cnt = 0
        for i, _ in enumerate(fail):
            if i is 0:
                continue
            elif fail[i-1][0] == fail[i][0] and fail[i-1][1] > fail[i][1]:
                fail[i-1], fail[i] = fail[i], fail[i-1]
                cnt+=1
        if cnt is 0:
            break
    f_list = [x[1] for x in fail]
    return f_list
        

n_list = [5,4]
s_list = [[2,1,2,6,2,4,3,3], [4,4,4,4,4]]

result = [ failure(s, c) for s,c  in zip(n_list,s_list) ]

# result = failure(5,[2,1,2,6,2,4,3,3])
print(result)
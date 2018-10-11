def failure(n, stages):
    total = len(stages)
    fail = []
    for i in range(1, n+1):
        challenger = stages.count(i)
        fail.append([challenger/total, i])
        total-=challenger

    s = sorted(fail, key = lambda x: (-x[0], x[1]))
    n_fail = [x[1] for x in s]
    
    return n_fail
        

n_list = [5,4]
s_list = [[2,1,2,6,2,4,3,3], [4,4,4,4,4]]

result = [ failure(s, c) for s,c  in zip(n_list,s_list) ]

# result = failure(5,[2,1,2,6,2,4,3,3])
print(result)
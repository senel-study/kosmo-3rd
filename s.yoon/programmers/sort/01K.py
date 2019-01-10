def solution(array, commands):
    answer = []
    for items in commands:
        if items[0] == items[1]:
            answer.append(array[items[0]-1])
        else:
            tmp = array[items[0]-1 : items[1]]
            tmp.sort()
            answer.append(tmp[items[2]-1])  
    return answer

array = [1, 5, 2, 6, 3, 7, 4]
commands = [[2, 5, 3], [4, 4, 1], [1, 7, 3]]

print(solution(array, commands))
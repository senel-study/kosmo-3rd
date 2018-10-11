def muji(k, food_times):
    tmp = 0
    flag = True
    if k >= sum(food_times):
        food = -1
        return food
    while flag:
        for i, _ in enumerate(food_times):
            if food_times[i] is not 0:
                food_times[i] -= 1
                tmp+=1
            if tmp == k+1:
                if i == len(food_times)-1:
                    food = len(food_times)
                else:
                    food = i+1
                flag = False
                break
            
    return food

result = muji(5, [3,1,2])
print(result)


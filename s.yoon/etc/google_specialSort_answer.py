def special_sort(s_list):
    return [x for x in s_list if x < 0 ] + [x for x in s_list if x is 0] + [x for x in s_list if x > 0]


print(special_sort([-1,1,3,-2,2]))
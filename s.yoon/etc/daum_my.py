def distance(dot_list):
    if len(dot_list) < 2:
        return print("plz put more than 2 dots")
    
    _min = None
    for i, _ in enumerate(dot_list):
        if i is 0:
            continue
        tmp = dot_list[i] - dot_list[i-1]
        if _min is None or tmp < _min:
            _min = tmp
            dots = [ [dot_list[i-1], dot_list[i]] ]
        elif tmp == _min:
            dots.append([dot_list[i-1], dot_list[i]])
    return dots

dot_list = [1,3,4,8,13,17,20]
result = distance(dot_list)
print(result)


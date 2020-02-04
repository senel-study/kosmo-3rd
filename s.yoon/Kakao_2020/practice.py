def a(i, j):
    num = i+j
    print(num)
    if num < 10:
        num + a(i,j)
    else:
        return num
        
a(1,2)
    
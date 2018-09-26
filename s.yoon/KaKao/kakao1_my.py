import time
start = time.process_time()

def miro(n, arr1, arr2):
    listkey = []
    for i in range(n):
        key = format(arr1[i]|arr2[i], "b").zfill(n)
        key = key.replace("1", "#").replace("0", " ")
        listkey.append(key)
    return print(listkey)

miro(5, [9,20,28,18,11], [30,1,21,17,28])
miro(6, [46,33,33,22,31,50], [27,56,19,14,14,10])

end = time.process_time()
print(end-start)
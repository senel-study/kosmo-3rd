import time
start = time.process_time()

def secret(n, arr1, arr2):
    print(['{0:b}'.format((i | j)).zfill(n).replace('0', ' ').replace('1', '#') for i, j in zip(arr1, arr2)])


secret(5, [9, 20, 28, 18, 11], [30, 1, 21, 17, 28])
secret(6, [46, 33, 33 ,22, 31, 50], [27 ,56, 19, 14, 14, 10])

end = time.process_time()
print(end-start)
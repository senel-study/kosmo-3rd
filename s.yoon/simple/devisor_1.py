import math
import time
start = time.process_time()

def devisor():
    inp = input()
    try:
       num = int(inp)
    except ValueError:
        print("Plz input Number")
        return devisor()
    center = int(math.sqrt(num))
    dev_f = [x for x in range(1, center+1) if num%x == 0]
    dev_b = [int(num/x) for x in dev_f]
    dev_list = list(set(dev_f+dev_b))
    dev_list.sort()
    return print(dev_list)  

devisor()
end = time.process_time()
print(end-start)

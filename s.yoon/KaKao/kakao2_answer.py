import re
import time
start = time.process_time()

def dart(inp):
    shot = re.findall(r'\d{1,2}[SDT][*#]?', inp)

    opt = [1,1,1]
    for i, s in enumerate(shot):
        if s[-1] == '#':
            opt[i] *= -1
            shot[i] = shot[i][:-1]
        elif s[-1] == '*':
            opt[i] *= 2
            shot[i] = shot[i][:-1]
            if i:
                opt[i-1] *= 2

    point = [(int(s[:-1]) ** '0SDT'.find(s[-1]) * o) for s, o in zip(shot, opt)]

    return sum(point)


print(dart('1S2D*3T'))
print(dart('1D2S#10S'))
print(dart('1D2S0T'))
print(dart('1S*2T*3S'))
print(dart('1D#2S*3S'))
print(dart('1T2D3D#'))
print(dart('1D2S3T*'))

end = time.process_time()
print(end-start)
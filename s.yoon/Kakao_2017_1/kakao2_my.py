import time
start = time.process_time()

def score(raw_result):
    result_list = divide_token(raw_result)
    total_score = convert_score(result_list)
    return print(total_score)

def divide_token(result):
    point_list = []
    tmp = ""
    for i, char in enumerate(result):
        if char.isdigit(): # 숫자일 때
            if i is 0:
                tmp+=char
                continue
            if int(char) is 0:
                tmp+=char
                continue
            point_list.append(tmp)
            tmp = char
        else: # 문자일 때
            tmp+=char
            if i is len(result)-1:
             point_list.append(tmp)
    return point_list

def convert_score(result_list):
    result_list.reverse() # 계산을 편하기 위해 역순으로 (스타상이 현재와 다음 점수를 2배로 올려준다.)
    star = False
    score = 0
    for items in result_list:
        # 숫자 취득
        if int(items[0]) is 1: # 인덱스1이 1이면 두번째가 0일 가능성이 존재 만약 그렇다면 점수가 10
            if items[1].isdigit():
                point = int(items[0:2]) 
            else:
                point = int(items[0])
        else:
            point = int(items[0])
        if "D" in items: # Double
            point**=2
        elif "T" in items: # Triple
            point**=3
        if star: # 전 회차에 스타상을 받았따면
            point*=2
            star = False
        if "*" in items: # 스타상
            point*=2
            star = True
        if "#" in items: # 아차상
            point*=(-1)
        score+=point
    return score

score("1S2D*3T")
score("1D2S#10S")
score("1D2S0T")
score("1S*2T*3S")
score("1D#2S*3S")
score("1T2D3D#")
score("1D2S3T*")

end = time.process_time()
print(end-start)
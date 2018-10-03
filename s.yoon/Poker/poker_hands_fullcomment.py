import re

def poker_hands(code): # 제어함수
    code = code.replace("J","11").replace("Q","12").replace("K","13") # 잭 퀸 킹 치환
    black_hand, white_hand = separte_user(code) # 블랙 / 화이트 유저별로 손패 나눔
    black_made = made(black_hand) # 블랙 족보 체크
    white_made = made(white_hand) # 화이트 족보 체크
    result = judge(black_made, white_made) # 승패 판결
    return result #결과 리턴

def separte_user(code):
    hand_list = code.split() # 공백을 기준으로 리스트로 스플릿
    black_hand = separte_hand([x for i, x in enumerate(hand_list) if i<5]) # 인덱스 0~4
    white_hand = separte_hand([x for i, x in enumerate(hand_list) if i>=5]) #인덱스 5~9
    return black_hand, white_hand # 리턴(파이썬은 여러개 리턴 가능)

def separte_hand(hand):
    pn = re.compile(r'[0-9,A]{1,2}') # 숫자(1~2자리) or A
    pm = re.compile(r'[SDHC]') # 무늬 부분
    hand_list = []
    hand_list = [ pn.findall(x) + pm.findall(x) for x in hand ] # [[숫자,문자],[숫자,문자]...] 꼴로 리스트화
    hand_list.sort() # 리스트 정렬, hand_list[0][0] 즉 숫자의 오름차순으로 따라 정렬된다.(파이썬의 정렬기능)
    return hand_list 

def made(hand):
    
    num =  [x[0] for x in hand] # 숫자 부분만 리스트화
    index = ["2","3","4","5","6","7","8","9","10","11","12","13","A"] #참조 인덱스
    cnt = [num.count(x) for x in index] #한 숫자를 몇개 들었는지 표시하는 리스트

    isQuad = False # 포카드 트리거
    isTriple = False # 트리플 트리ㅓㄱ
    pair = 0 # 페어 갯수
    
    for i, x in enumerate(cnt):
        if x == 2: # cnt에 2가 있으면
            pair+=1 # 페어 변수 1증가
            top = index[i] # 탑 카드는 페어의 숫자
        if x == 3: # 3이 있으면
            isTriple = True  # 트리플 카드 존재
            top = index[i] # 탑 카드는 트리플의 숫자
        if x == 4: # 4가 있으면 존재
            isQuad = True # 포 카드가 존재
            top = index[i] # 탑 카드는 포카드의 숫자
        
    if isQuad: # 포카드가 존재하면
        return "QU", top #포카드/탑숫자 리턴
    
    if isTriple: #트리플이 존재하면
        if pair > 0 : #페어가 1이상(사실 1밖에 안되지만)
            return "FU", top #풀 하우스/탑숫자 리턴
        else: # 페어가 없다면
            return "TR", top #트리플/탑숫자 리턴
    
    if pair is 2: #페어가 2라면
        return "TP", top #투페어/탑숫자 리턴
    if pair is 1: #페어가 1이라면 (트리플은 이미 걸러서 무조건 원페어)
        return "OP", top #원페어/탑숫자 리턴
    
    mark =  set([x[1] for x in hand]) # 마크를 리스트에 넣어서 집합화 -> 중복이 자동 제거
    isFlush = False # 플러쉬 트리거
    if len(mark) is 1: # 마크를 모은 집합의 길이가 1이라면
        isFlush = True # 당연히 같은 무늬니까 플러쉬
    
    for i, x in enumerate(cnt): # 탑 카드 검색을 위한 반복문
        if x:
            top = index[i] #페어가 없기 때문에 가장 높은 숫자가 탑

    if cnt[12]: # A가 존재한다면
        index = ["1"] + index #A,2,3,4,5도 스트레이트(백스트레이트)이므로 리스트 맨 앞에 1을 추가
        cnt = [1] + cnt #A의 갯수(1) -> 페어는 없기 때문에 무조건 1

    
    isStraight = False # 스트레이트 트리거
    isMoutain = False # 마운틴 트리거
    line = 0 # 변수
    for i, x in enumerate(cnt): # 반복문
        if x: # cnt에 값이 있으면 True이므로 조건에 걸림
            line+=1 # 라인변수에 1추가
            if line is 5: #라인이 5라면 (cnt의 값이 5개 연속으로 있다면)
                isStraight = True # 스트레이트
                top = index[i] # 탑 카드는 스트레이트에서 가장 높은 카드
                if index[i] == "A": # 만약 탑 카드가 A라면
                    isMoutain = True # 마운틴
                break # 스트레이트가 완성된 시점에서 뒷 카드는 더 볼 필요가 없음
        else:
            if line > 0:
                break # 라인이 1이상인데 다음 숫자가 존재하지 않는다면 스트레이트가 아니므로 반복문을 더 체크할 필요 없으므로 브레이크
               
    if isFlush: # 플러쉬라면
        if isStraight: # 스트레이트라면
            if isMoutain: # 마운틴이라면
                return "RSF", top # 로얄스트레이트 플러쉬/탑카드 숫자 리턴
            else:
                return "SF", top #스트레이트 플러쉬/ 탑카드 숫자 리턴
        else:
            return "FL", top #플러쉬 / 탑카드 숫자 리턴

    return "TOP", top # 모든 if에 걸리지 않았다면 족보가 없음

def judge(black_made, white_made):
    board = ["TOP", "OP", "TP", "TR", "ST", "FL", "FU", "QU", "SF", "RSF"] # 족보 서열
    balck_score = board.index(black_made[0]) #인덱스 숫자 할당
    black_top = black_made[1] # 탑숫자 할당
    white_score = board.index(white_made[0])
    white_top = white_made[1]
    result = None
    if balck_score > white_score: # 족보가 높은쪽 승리
        result = "Black wins."
    elif balck_score == white_score: # 족보가 같으면 탑카드 숫자가 높은쪽 승리
        if black_top > white_top:
            result = "Black wins."
        elif black_top == white_top: # 둘 다 같으면 무승부
            result = "Tie."
        else:
            result = "White wins."
    else:
        result = "White wins"
    return result
        

test_list = [
    "2H 3D 5S 9C KD 2C 3H 4S 8C AH",
    "2H 4S 4C 2D 4H 2S 8S AS QS 3S",
    "2H 3D 5S 9C KD 2C 3H 4S 8C KH",
    "2H 3D 5S 9C KD 2D 3H 5C 9S KH",
]

result = [ poker_hands(s) for s in test_list ]
# result = poker_hands("10S JS QS KS 2S 3S AC AD 3H 3C")
print(result)

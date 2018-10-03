import re

def poker_hands(code):
    code = code.replace("J","11").replace("Q","12").replace("K","13")
    black_hand, white_hand = separte_user(code)
    black_made = made(black_hand)
    white_made = made(white_hand)
    result = judge(black_made, white_made)
    return result

def separte_user(code):
    hand_list = code.split()
    black_hand = separte_hand([x for i, x in enumerate(hand_list) if i<5])
    white_hand = separte_hand([x for i, x in enumerate(hand_list) if i>=5])
   
    return black_hand, white_hand

def separte_hand(hand):
    pn = re.compile(r'[0-9,A]{1,2}')
    pm = re.compile(r'[SDHC]')
    hand_list = []
    hand_list = [ pn.findall(x) + pm.findall(x) for x in hand ]
    hand_list.sort()
    return hand_list

def made(hand):
    
    mark =  set([x[1] for x in hand])
    num =  [x[0] for x in hand]
    index = ["A","2","3","4","5","6","7","8","9","10","11","12","13","A"]  
    cnt = [num.count(x) for x in index]

    isFlush = False
    if len(mark) is 1: # 플러쉬
        isFlush = True
  
    for i, x in enumerate(cnt):
        if x:
            top = index[i]

    isStraight = False
    isMoutain = False
    line = 0
    for i, x in enumerate(cnt): # 스트레이트
        if x:
            line+=1
            if line is 5:
                isStraight = True
                top = index[i]
                if index[i] == "A":
                    isMoutain = True
        else:
            line = 0
               
    if isFlush:
        if isStraight:
            if isMoutain:
                return "RSF", top
            else:
                return "SF", top
        else:
            return "FL", top

    index.pop(0)
    cnt.pop(0)  # 스트레이트 연산이 끝났으니 에이스는 1의 역할이 필요 없으니 지움.

    isQuad = False # 포카드
    isTriple = False # 트리플
    pair = 0 # 페어
    
    for i, x in enumerate(cnt):
        if x == 2:
            pair+=1
            top = index[i]
        if x == 3:
            isTriple = True
            top = index[i]
        if x == 4:
            isQuad = True
            top = index[i]
        
    if isQuad:
        return "QU", top
    
    if isTriple:
        if pair > 0 :
            return "FU", top
        else:
            return "TR", top
    
    if pair is 2:
        return "TP", top
    elif pair is 1:
        return "OP", top
    else:
        return "TOP", top

def judge(black_made, white_made):
    board = ["TOP", "OP", "TP", "TR", "ST", "FL", "FU", "QU", "SF", "RSF"]
    balck_score = board.index(black_made[0])
    black_top = black_made[1]
    white_score = board.index(white_made[0])
    white_top = white_made[1]
    result = None
    if balck_score > white_score:
        result = "Black wins."
    elif balck_score == white_score:
        if black_top > white_top:
            result = "Black wins."
        elif black_top == white_top:
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

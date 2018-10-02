import re

test_list = [
    "2H 3D 5S 9C KD 2C 3H 4S 8C AH",
    "2H 4S 4C 2D 4H 2S 8S AS QS 3S",
    "2H 3D 5S 9C KD 2C 3H 4S 8C KH",
    "2H 3D 5S 9C KD 2D 3H 5C 9S KH",
]
def poker_hands(code):
    code = code.replace("J","11").replace("Q","12").replace("K","13")
    black_hand, white_hand = separte_user(code)
    result = made(white_hand)
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
    if len(mark) is 1:
        return "Flush"

# result = [ poker_hands(s) for s in test_list ]
result = poker_hands("2H AS 4C 2D 4H 2S 8S AS QS 3S")
print(result)
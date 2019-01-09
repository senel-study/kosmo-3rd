def solution(clothes):
    category = list(set([x[1] for x in clothes]))
    combination = []
    answer = 1
    for items in category:
        combination.append([x[0] for x in clothes if x[1]==items])
    for items in combination:
        answer *= (len(items)+1)
    return answer-1

clothes = [["yellow_hat", "headgear"], ["blue_sunglasses", "eyewear"], ["green_turban", "headgear"]]

print(solution(clothes))
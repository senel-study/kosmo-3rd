phone = ["123", "456", "789"]

def solution(phone_book):
    answer = True
    sorted_list = sorted(phone_book, key=len)
    short = sorted_list.pop(0)
    for i in sorted_list:
        if short == i[0:len(short)]:
            answer = False
    return answer

print(solution(phone))

# if short in i가 이상하게 통과를 못함




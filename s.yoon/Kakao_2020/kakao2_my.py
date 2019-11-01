p =')()()()('
# (()())()

def solution(p):
    cnt = 0
    stack = ""
    sort_list = []
    for c in p:
        stack+=c
        if c == "(":
            cnt+=1
        else:
            cnt-=1
        if cnt == 0:
            if score(stack) is True:
                sort_list.append(stack)
            else:
                text = switch(stack)
                sort_list.append(text)
            stack=""
    answer = "".join(sort_list)
    flag = score(answer)
    if flag is True:
        return answer
    else:
        solution(answer)

        

def switch(txt):
    result = ""
    if txt == "":
        return result
    else:
        result += "("
        for c in txt[1:-1]:
            if c == "(":
                result+=")"
            else:
                result+="("
        result+=")"
    return result

def score(p):
    cnt = 0
    for c in p:
        if c == "(":
            cnt+=1
        else:
            cnt-=1
        if cnt < 0:
            return False
    if cnt == 0:
        return True
    else:
        return False

a = solution(p)
print(a)
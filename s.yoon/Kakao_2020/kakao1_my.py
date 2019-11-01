
# s = ["aabbaccc", "ababcdcdababcdcd", "abcabcdede", "abcabcabcabcdededededede", "xababcdcdababcdcd"]
s = "a"


def solution(s):
    full_length = len(s)
    half_length = (int(len(s)/2))
    full_list = []

    for i in range(1, half_length+1):
        stack = ""
        split_list = []
        division = int(full_length/i)
        rest = full_length%i
        cnt = 1
        for j in range(0, division):
            text = s[i*j:i*(j+1)]
            if stack == "":
                stack = text
            elif stack == text:
                cnt+=1
            else:
                if cnt > 1:
                    split_list.append(str(cnt)+stack)
                    stack = text
                    cnt = 1
                else:
                    split_list.append(stack)
                    stack = text
                    cnt = 1
        if rest is not 0:
            if cnt > 1:
                split_list.append(str(cnt)+stack)
                split_list.append(s[-rest:])
            else:
                split_list.append(stack)
                split_list.append(s[-rest:])
        else:
            if cnt > 1:
                split_list.append(str(cnt)+stack)
            else:
                split_list.append(stack)
        full_list.append(len("".join(split_list)))
    if len(full_list) > 1:
        return min(full_list)
    elif len(full_list) == 0:
        return len(s)


solution(s)

# EOF

def solution(record):
    inp = [ x.split() for x in record ]
    name_dict = {}
    answer = []

    for items in inp:
        if items[0] != "Leave":
            name_dict[items[1]] = items[2]

    for items in inp:
        if items[0] == "Enter":
            answer.append("{0}님이 들어왔습니다.".format(name_dict[items[1]]))
        elif items[0] == "Leave":
            answer.append("{0}님이 나갔습니다.".format(name_dict[items[1]]))

    return answer

record = ["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"]

result = solution(record)
print(result)
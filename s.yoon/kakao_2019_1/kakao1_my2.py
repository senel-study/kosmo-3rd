def solution(record):
    inp = [ x.split() for x in record ]
    name_dict = {}
    event = []
    answer = []

    for items in inp:
        if items[0] == "Enter":
            name_dict[items[1]] = items[2]
            event.append([items[1], "님이 들어왔습니다."])
        elif items[0] == "Change":
            name_dict[items[1]] = items[2]
        else:
            event.append([items[1], "님이 나갔습니다."])

    for items in event:
        answer.append(name_dict[items[0]]+items[1])

    return answer

record = ["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"]

result = solution(record)
print(result)
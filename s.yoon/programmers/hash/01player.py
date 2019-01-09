participant = ["marina", "josipa", "nikola", "vinko", "filipa", "filipa"]	
completion = ["josipa", "filipa", "marina", "filipa", "nikola"]

def solution(participant, completion):
    answer = ''
    isDuplicated = ( len(participant) == len(set(participant)) )

    if(isDuplicated):
        player = set(participant) - set(completion)
        answer = list(player)[0]
        return answer
    else:
        participant.sort()
        completion.sort()
        for i, s in enumerate(completion):
            if(participant[i] != s):
                answer = participant[i]
                return answer
        answer = participant[-1]
        return answer


print(solution(participant, completion))
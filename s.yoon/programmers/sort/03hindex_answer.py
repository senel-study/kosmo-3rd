
def solution(citations):
    citations.sort(reverse=True)
    answer = max(map(min, enumerate(citations, start=1)))
    # print(list(enumerate(citations, start=1)))
    # print(list(map(min, enumerate(citations, start=1))))
    return answer

citations = [3, 3, 3,4,4,5]
citations = [3, 0,6,1,5,4,4]
print(solution(citations))
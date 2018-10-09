def failure(n, stages):
    total = len(stages) # 전체 도전자 숫자 stage 리스트의 길이
    fail = [] #  리스트 생성
    for i in range(1, n+1):
        challenger = stages.count(i) # 1번부터 끝 스테이지까지 도전하고 있는 도전자 숫자
        fail.append([challenger/total, i]) # [실패율, 스테이지넘버]의 형식으로 리스트의 추가
        total-=challenger # 전체 도전자 숫자에서 각 스테이지마다 도전자숫자를 뺌
    fail.sort(reverse=True) # 파이썬의 내림차순 정렬로 인해 실패율의 내림차순으로 정렬이 완료

    # 실패율의 내림차순으로 정렬 되었으나 이 방법으로는 실패율이 같을 때 스테이지 넘버도 내림차순으로 정렬된다.

    n_fail = [] # 스테이지 번호를 닮을 새로운 리스트

    tmp = fail[0][0] # 실패율이 같은지 확인할 변수
    tmp_list = [] # 실패율이 같을 경우 정렬을 위한 임시리스트
    while True: 
        if fail[0][0] == tmp: # 실패율이 같을 경우
            tmp_list.append(fail[0][1]) # 스테이지 번호를 임시 리스트에 추가
        else: # 실패율이 다를 경우
            tmp_list.sort() # 임시리스트를 오름차순으로 정렬
            n_fail += tmp_list # 새 리스트와 병합
            tmp_list=[] # 임시 리스트 초기화
            tmp = fail[0][0] # 현재의 실패율로 비교변수 갱신
            tmp_list.append(fail[0][1]) # 스테이지 번호를 임시 리스트에 추가
        fail.pop(0) # 첫번째 리스트의 값을 제거
        if len(fail) is 0: # 리스트를 전부 순환했을 경우
            tmp_list.sort() # 임시 리스트를 오름차순으로 정렬
            n_fail += tmp_list # 새 리스트와 병합
            break # 반복문 종료

    return n_fail # 리턴

n_list = [5,4]
s_list = [[2,1,2,6,2,4,3,3], [4,4,4,4,4]]

# result = failure(4,[4,4,4,4,4])

result = [ failure(s, c) for s,c  in zip(n_list,s_list)]
print(result)
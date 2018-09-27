import time
start = time.process_time()

def slice_list(list): # 리스트에 한글자씩 나눠서 넣음
    index = []
    for items in list: 
        arr = []
        for i in items:
            arr.append(i)
        index.append(arr) 
    return index

def pop(m, n, index):
    loop_flag = False 
    crash = [] # 자신을 기준으로 상, 우상, 우의 무늬를 비교. 가로로 0부터 폭-1, 세로로 1부터 높이까지 체크하면 전부 체크가능 
    for i in range(1, m): # m은 리스트의 순서 0이 젤 위 블럭
        for j in range(0, n-1): # n은 블럭 안에서의 순서
            if (
                index[i][j] is not " " and
                index[i][j] == index[i-1][j] and 
                index[i][j] == index[i-1][j+1] and 
                index[i][j] == index[i][j+1]
                ):
                tmp_index = [[i,j],[i-1,j],[i-1,j+1],[i,j+1]]
                for items in tmp_index:
                    if items not in crash:
                        crash.append(items) # 터트릴 리스트의 좌표들
    for x, y in crash: # 터트릴 리스트의 값을 ' '로 교환
        index[x][y] = ' '
        loop_flag = True

    while True:
        move_flag = False # 이동이 있었는지 체크하는 변수
        for i in range(1, m):
            for j in range(0, n):
                if index[i][j] is ' ' and index[i-1][j] is not ' ':
                    index[i][j], index[i-1][j] = index[i-1][j], index[i][j]
                    move_flag = True # 이동이 존재하면 한 번 더 스캔 해주어야 한다. 그렇지 않으면 0이 붙어있는 상황에서 해결이 되지 않기 때문
        if not move_flag:
            break
    return index, loop_flag

def join_index(index): # 개별로 쪼개놓은 리스트를 다시 원래 입력양식으로 돌려주는 함수
    new_board = []
    for items in index:
        new_board.append(''.join(items))
    return new_board

def kakao(m, n, board):
    index = slice_list(board)
    while True:
        index, flag = pop(m,n,index)
        new_board = join_index(index)
        if flag:
            index = slice_list(new_board)
            pop(m, n, index)
        if not flag:
            break
    cnt = ''.join(new_board).count(' ')
    return cnt

m = [4,6]
n = [5,6]
board = [["CCBDE", "AAADE", "AAABF", "CCBBF"], ["TTTANT", "RRFACC", "RRRFCC", "TRRRAA", "TTMMMF","TMMTTJ"]]
result = [kakao(a,b,c) for a,b,c in zip(m,n,board)]
print(result)

end = time.process_time()
print(end-start)
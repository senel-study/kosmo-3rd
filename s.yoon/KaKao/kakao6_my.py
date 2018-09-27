import time
start = time.process_time()

def kakao(m, n, board):
    
    self_flag = False
    
    index = []

    for items in board: # 리스트에 한글자씩 나눠서 넣음
        arr = []
        for i in items:
            arr.append(i)
        index.append(arr) 

    crash = [] # 자신을 기준으로 상, 우상, 우의 무늬를 비교. 가로로 0부터 폭-1, 세로로 1부터 높이까지 체크하면 전부 체크가능 
    for i in range(1, m): # m은 리스트의 순서 0이 젤 위 블럭
        for j in range(0, n-1): # n은 블럭 안에서의 순서
            if (
                index[i][j] is not " " and
                index[i][j] == index[i-1][j] and 
                index[i][j] == index[i-1][j+1] and 
                index[i][j] == index[i][j+1]
                ):
                tmp_list = [[i,j],[i-1,j],[i-1,j+1],[i,j+1]]
                for items in tmp_list:
                    if items not in crash:
                        crash.append(items) # 터트릴 리스트의 좌표들
    
    for x, y in crash: # 터트릴 리스트의 값을 Z로 교환
        index[x][y] = ' '
        self_flag = True

    while True:
        move_flag = False
        for i in range(1, m):
            for j in range(0, n):
                if index[i][j] is ' ' and index[i-1][j] is not ' ':
                    index[i][j], index[i-1][j] = index[i-1][j], index[i][j]
                    move_flag = True
        if not move_flag:
            break
    
    new_board = []
    for items in index:
        new_board.append(''.join(items))
    
    if self_flag:
        kakao(m, n, new_board)
    else:
        global cnt
        cnt = ''.join(new_board).count(' ')

    return cnt

m = [4,6]
n = [5,6]
board = [["CCBDE", "AAADE", "AAABF", "CCBBF"], ["TTTANT", "RRFACC", "RRRFCC", "TRRRAA", "TTMMMF","TMMTTJ"]]
result = [kakao(a,b,c) for a,b,c in zip(m,n,board)]
print(result)

end = time.process_time()
print(end-start)
from collections import Counter
from operator import itemgetter
import time
start = time.process_time()

def solution(genres, plays):
    queue = [ [({g:p}),i] for i,(g,p) in enumerate(zip(genres,plays)) ]
    tmp = Counter()
    for items in queue:
        tmp+=Counter(items[0])
    sorted_gen = sorted(tmp.items(), key=itemgetter(1), reverse=True)
    best_genre = [x[0] for x in sorted_gen]
    answer = []
    for gen in best_genre:
        loop_queue = queue[:]
        arr = []
        # for q in queue:
        for q in loop_queue:
            if gen in q[0]:
                arr.append([q[0][gen], q[1]])
                queue.remove(q)
        sorted_arr = sorted(arr, key= lambda x:(-x[0],x[1]))
        answer += [x[1] for i,x in enumerate(sorted_arr) if i<2]
    return answer

genres = ["classic", "pop", "classic", "classic", "pop", "rock", "classic" "rock", "R&B", "rock"]
plays = [500, 600, 150, 800, 2500, 800, 1000, 1600, 400, 900]


print(solution(genres, plays))

end = time.process_time()
print(end-start)
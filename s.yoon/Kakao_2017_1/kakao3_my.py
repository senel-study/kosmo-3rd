import time
start = time.process_time()

def runtime(size, cities):
    if size < 0 or size > 30: # 예외처리
        print('캐시 사이즈의 범위는 1~30 입니다.')
    if len(cities) > 100000:
        print('최대 도시 수는 100,000개 입니다.')

    cache_list = []  # 캐시 리스트 준비
    time = 0 # 캐시타임 준비

    if size is 0:
        time = len(cities) * 5
        return time

    for city in cities:
        if city.upper() in cache_list: # 캐시 리스트에 도시가 있을 경우
            time+=1
        else: # 캐시 리스트에 도시가 없을 경우
            if len(cache_list) < size: # 캐시 사이즈보다 리스트가 작을경우
                cache_list.append(city.upper()) # 리스트에 도시 추가
            else: # 리스트가 가득 찼을 경우
                del cache_list[0] # 가장 오래된 리스트 삭제
                cache_list.append(city.upper()) # 리스트에 도시 추가
            time+=5
    
    return time

test_size = [3, 3, 2, 5, 2, 0]
test_cities = [
    ["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "Jeju", "Pangyo", "Seoul", "NewYork", "LA"],
    ["Jeju", "Pangyo", "Seoul", "Jeju", "Pangyo", "Seoul", "Jeju", "Pangyo", "Seoul"],
    ["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "SanFrancisco", "Seoul", "Rome", "Paris", "Jeju", "NewYork", "Rome"],
    ["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "SanFrancisco", "Seoul", "Rome", "Paris", "Jeju", "NewYork", "Rome"],
    ["Jeju", "Pangyo", "NewYork", "newyork"],
    ["Jeju", "Pangyo", "Seoul", "NewYork", "LA"]
]

result = [runtime(s,c) for s, c in zip(test_size, test_cities)]
print(result)

end = time.process_time()
print(end-start)
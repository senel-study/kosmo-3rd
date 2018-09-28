import time
start = time.process_time()

def measure(size, cities):
    cache =[''] * size

    time = 0
    for city in cities:
        if city.lower() in cache:
            time += 1
        else:
            time += 5
            cache.append(city.lower())
            cache.pop(0)

    return time


test_size = [3, 3, 2, 5, 2, 0]
test_cities = [['Jeju', 'Pangyo', 'Seoul', 'NewYork', 'LA', 'Jeju', 'Pangyo', 'Seoul', 'NewYork', 'LA'], 
               ['Jeju', 'Pangyo', 'Seoul', 'Jeju', 'Pangyo', 'Seoul', 'Jeju', 'Pangyo', 'Seoul'],
               ['Jeju', 'Pangyo', 'Seoul', 'NewYork', 'LA', 'SanFrancisco', 'Seoul', 'Rome', 'Paris', 'Jeju', 'NewYork', 'Rome'],
               ['Jeju', 'Pangyo', 'Seoul', 'NewYork', 'LA', 'SanFrancisco', 'Seoul', 'Rome', 'Paris', 'Jeju', 'NewYork', 'Rome'],
               ['Jeju', 'Pangyo', 'NewYork', 'newyork'],
               ['Jeju', 'Pangyo', 'Seoul', 'NewYork', 'LA']]
result = [measure(s, c) for s, c in zip(test_size, test_cities)]
print(result)

end = time.process_time()
print(end-start)
def smallest_range(*lists):
    heap = []
    for items in lists:
        items.sort()
        heap.append(items[0])
        heap.sort()
    result = [[min(heap), max(heap)]]
    distance = max(heap) - min(heap)
    flag = True
    while flag:
        for items in lists:
            if min(heap) in items:
                items.pop(0)
                if len(items) is 0:
                    flag = False
                    break
                heap[0] = items[0]
                heap.sort()
                if distance > max(heap) - min(heap):
                    result = [[min(heap), max(heap)]]
                    distance = max(heap) - min(heap)
                elif distance == max(heap) - min(heap) and heap not in result:
                    result.append([min(heap), max(heap)])

    return result

list1 = [4, 10, 15, 24, 26]
list2 = [0, 9, 12, 20 ]
list3 = [5, 18, 22, 23, 30]

result = smallest_range(list1, list2, list3)
print(result)

import re

def multiset_intersection(list1, list2):
    intersection = []
    set1 = set(list1)
    set2 = set(list2)
    inter_set = set1&set2
    for items in inter_set:
        if (items in list1) and (items in list2):
            num = min(list1.count(items), list2.count(items))
            tmplist = [items]*num
            intersection.extend(tmplist)
    return intersection

def multiset_union(list1, list2):
    union = []
    set1 = set(list1)
    set2 = set(list2)
    union_set = set1|set2
    for items in union_set:
        num = max(list1.count(items), list2.count(items))
        tmplist = [items]*num
        union.extend(tmplist)
    return union

def slice_txt(str):
    slice_list = []
    p = re.compile(r'[a-zA-Z]{2}')
    for i in range(0,len(str)-1):
        tmp = str[i:i+2]
        if p.match(tmp):
            tmp = tmp.lower()
            slice_list.append(tmp)
    return slice_list


def jaccard(str1, str2): 
    list1 = slice_txt(str1)
    list2 = slice_txt(str2)
    intersection = multiset_intersection(list1, list2)
    union = multiset_union(list1, list2)
    if union:
        similar = len(intersection)/len(union)*65536
    else:
        similar = 65536
    return int(similar)

list1 = ['France', 'handshake', 'aa1+aa2', 'E=M*C^2']
list2 = ['french', 'shake hands', 'AAAA12', 'e=m*c^2']

result = [jaccard(s,c) for s,c in zip(list1, list2)]
print(result)
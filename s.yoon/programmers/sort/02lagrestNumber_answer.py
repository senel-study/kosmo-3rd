import functools

numbers = [3, 30, 34, 5, 9]

def solution(numbers):
    numbers = list(map(str, numbers))
    numbers.sort(key=functools.cmp_to_key(lambda x,y: int(x+y)-int(y+x)), reverse=True)
    if numbers[0] == '0':
        return '0'
    return ''.join(numbers)

# numbers.sort(key=functools.cmp_to_key(lambda x,y: x-y))

print(numbers)
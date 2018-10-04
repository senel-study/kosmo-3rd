result = sum(set(range(1, 50)) - {x + sum([int(a) for a in str(x)]) for x in range(1, 50)})

print(result)
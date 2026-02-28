def intersections(first, second):
    sf = set(first)
    ss = set(second)
    return list(sf & ss)

print(intersections([0,1,2], [0,2,4]))
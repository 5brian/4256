# section 1
def union(s1,s2):
    result = set()

    for item in s1:
        result.add(item)

    for item in s2:
        result.add(item)

    return result

def difference(s1, s2):
    result = set()

    for item in s1:
        if item not in s2:
            result.add(item)

    return result

def is_subset(s1, s2):
    for item in s1:
        if item not in s2:
            return False

    return True

def are_disjoint(s1,s2):
    for item in s1:
        if item in s2:
            return False

    return True

def symmetric_difference(s1,s2):
    result = set()

    for item in s1:
        if item not in s2:
            result.add(item)

    for item in s2:
        if item not in s1:
            result.add(item)

    return result

def cartesian_product(s1,s2):
    result = set()

    for item1 in s1:
        for item2 in s2:
            result.add((item1, item2))

    return result

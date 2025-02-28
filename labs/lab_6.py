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

# section 2

def union_2(*sets):
    result = set()

    for s in sets:
        for item in s:
            result.add(item)

    return result

def isdisjoint_2(*sets):
    for i in range(len(sets)):
        for j in range(i + 1, len(sets)):
            for item in sets[i]:
                if item in sets[j]:
                    return False

    return True

# section 3

def is_well_formed(s):
    stack = []
    brackets = {')': '(', '}': '{', ']': '['}

    for char in s:
        if char in '({[':
            stack.append(char)
        elif char in ')}]':
            if not stack or stack.pop() != brackets[char]:
                return False

    return len(stack) == 0

# section 4

def rpn(s):
    stack = []

    for char in s:
        if char.isdigit():
            stack.append(int(char))
        else:
            if len(stack) < 2:
                raise ValueError("Invalid RPN expression")

            b = stack.pop()
            a = stack.pop()

            if char == '+':
                stack.append(a + b)
            elif char == '-':
                stack.append(a - b)
            elif char == '*':
                stack.append(a * b)

    return stack[0]

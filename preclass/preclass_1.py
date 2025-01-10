def maximum(li):
    max_val = float("-inf")
    for num in li:
        if num > max_val:
            max_val = num
    return max_val

def maximum_index(li):
    max_val = float("-inf")
    max_index = 0
    for i in range(len(li)):
        if li[i] > max_val:
            max_val = li[i]
            max_index = i
    return max_index

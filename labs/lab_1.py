# 1
def foo(n):
    result = 0

    for i in range(2, n + 1, 3):
        result += i

    print(result)
    return result


print('P1')
foo(10)


# 2
def sum_largest(li):
    max_val = float("-inf")
    second_max_val = float("-inf")

    for item in li:
        if item > max_val:
            second_max_val = max_val
            max_val = item
        elif max_val > item > second_max_val:
            second_max_val = item

    print(max_val, second_max_val)
    print(max_val + second_max_val)
    return max_val + second_max_val


print('P2')
sum_largest([10, 4, 6, 12, -3, 1, 14, -7, 9])


# 3
def sum_largest_sorted(li):
    li_sorted = sorted(li)

    print(sum(li_sorted[-2:]))
    return sum(li_sorted[-2:])


print('P3')
sum_largest_sorted([10, 4, 6, 12, -3, 1, 14, -7, 9])


# 4a
# 3

# 4b
# sort() will modify the list but sorted() returns the sorted list

# 5
def merge(li1, li2):
    merged = []
    i = 0
    j = 0

    while i < len(li1) and j < len(li2):
        if li1[i] <= li2[j]:
            merged.append(li1[i])
            i += 1
        else:
            merged.append(li2[j])
            j += 1

    merged.extend(li1[i:])
    merged.extend(li2[j:])

    print(merged)
    return merged


print('P5')
merge(([2, 4, 5, 8, 10, 11, 13]), ([3, 6, 7, 8, 10, 12]))


# 6
def largest_so_far(li):
    max_left = float('-inf')
    count = 0

    for i in li:
        if i > max_left:
            count += 1
            max_left = i

    print(count)
    return count


print('P6')
largest_so_far([10, 8, 9, 9, 13, 16, 12])


# 7
def evens(li):
    count = 0

    for i in range(0, len(li), 2):
        if li[i] % 2 == 0:
            count += 1

    print(count)
    return count


print('P7')
evens([3, -2, 4, 7, -6, 7, 5])


# 8
def linear_search(li, num):
    for i in li:
        if i == num:
            print(True)
            return True

    print(False)
    return False


print('P8')
linear_search([1, 2, 3, 4, 5, 6, 7, 8, 9], 7)


# 9
def binary_search(li, num):
    low = 0
    high = len(li) - 1

    while low <= high:

        mid = (high + low) // 2

        if li[mid] < num:
            low = mid + 1

        elif li[mid] > num:
            high = mid - 1

        else:
            print(True)
            return True

    print(False)
    return False


print('P9')
binary_search([1, 2, 3, 4, 5, 6, 7, 8, 9], 7)

# O(n) = log(n)

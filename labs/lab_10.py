def median(nums):
    sorted_nums = sorted(nums)
    n = len(sorted_nums)

    if n % 2 == 1:
        return sorted_nums[n // 2]
    else:
        return (sorted_nums[n // 2 - 1] + sorted_nums[n // 2]) / 2

def mode(nums):
    counts = {}
    for num in nums:
        if num in counts:
            counts[num] += 1
        else:
            counts[num] = 1

    max_count = 0
    for num, count in counts.items():
        if count > max_count:
            max_count = count

    modes = set()
    for num, count in counts.items():
        if count == max_count:
            modes.add(num)

    return modes

def arithmetic_mean(nums):
    if not nums:
        return 0

    total = 0
    count = 0

    for num in nums:
        total += num
        count += 1

    return total / count

def olympic_mean(nums):
    if len(nums) < 3:
        return None

    min_val = float('inf')
    max_val = float('-inf')
    total = 0

    for num in nums:
        if num < min_val:
            min_val = num
        if num > max_val:
            max_val = num
        total += num

    total -= (min_val + max_val)

    return total / (len(nums) - 2)

def geometric_mean(nums):
    if not nums:
        return None

    for num in nums:
        if num <= 0:
            return None

    product = 1
    count = 0

    for num in nums:
        product *= num
        count += 1

    return product ** (1 / count)

def harmonic_mean(nums):
    if not nums:
        return None

    reciprocal_sum = 0
    count = 0

    for num in nums:
        if num == 0:
            return None
        reciprocal_sum += 1 / num
        count += 1

    return count / reciprocal_sum

def sample_variance(nums):
    if len(nums) < 2:
        return None

    mean = arithmetic_mean(nums)

    sum_squared_diff = 0
    for num in nums:
        sum_squared_diff += (num - mean) ** 2

    return sum_squared_diff / (len(nums) - 1)

import random

def ten_flips():
    flips = [random.randint(0, 1) for _ in range(10)]
    return sum(flips) == 7

def prob_seven_out_of_ten(n):
    count = 0
    for _ in range(n):
        if ten_flips():
            count += 1
    return count / n

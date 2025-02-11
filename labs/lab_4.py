import numpy

def ice_cream(trials):
    successes = 0

    for _ in range(trials):
        bill_arrival = numpy.random.uniform(0, 30)
        lilly_arrival = numpy.random.uniform(0, 30)

        if bill_arrival <= lilly_arrival <= bill_arrival + 5 or lilly_arrival <= bill_arrival <= lilly_arrival + 7:
            successes += 1

    return round(successes / trials, 2)

def matches_helper():
    used = book1_matches = book2_matches = 0
    while True:
        book = numpy.random.randint(0, 2)
        if book == 0:
            if book1_matches < 20:
                book1_matches += 1
                used += 1
            else:
                return used
        else:
            if book2_matches < 20:
                book2_matches += 1
                used += 1
            else:
                return used

def die_rolls(trials):
    results = {}
    for i in range(2, 13):
        results[i] = 0
    for _ in range(trials):
        total =numpy.random.randint(1, 7) + numpy.random.randint(1, 7)
        results[total] += 1
    for key in results:
        results[key] = (results[key] / trials) * 100
    return results

def die_rolls_2(trials, n):
    results = {}
    for i in range(n, (6 * n) + 1):
        results[i] = 0
    for _ in range(trials):
        total = sum(numpy.random.randint(1, 7) for _ in range(n))
        results[total] += 1
    for key in results:
        results[key] = round((results[key] / trials) * 100, 1)
    return results

def birthday():
    trials = 10000
    def check_birthday_match(num_people):
        birthdays = [numpy.random.randint(1, 365) for _ in range(num_people)]
        return len(set(birthdays)) < len(birthdays)
    for num_people in range(1, 367):
        matches = sum(check_birthday_match(num_people)
                        for _ in range(trials))
        probability = matches / trials
        if probability > 0.5:
            return num_people

    return None

# 5) Alice and Bob each roll a die repeatedly. Alice rolls hers until she rolls a
# five followed by a six. Bob rolls his until he rolls two fives in a row.
# Who is more likely to use fewer rolls? Or will they be the same?
#
# bob

print(ice_cream(10000))
print(matches_helper())
print(die_rolls(10000))
print(die_rolls_2(10000, 3))
print(birthday())

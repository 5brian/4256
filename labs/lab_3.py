import math

# 1
def grades(di):
    result = {}

    for name, score in di.items():
        if score >= 90:
            result[name] = 'A'
        elif score >= 80:
            result[name] = 'B'
        elif score >= 70:
            result[name] = 'C'
        elif score >= 60:
            result[name] = 'D'
        else:
            result[name] = 'E'

    return result

# 2
def letter_grades(di):
    counts = {'A': 0, 'B': 0, 'C': 0, 'D': 0, 'E': 0}

    for grade in di.values():
        counts[grade] += 1

    return counts

# 3
def letter_grades_2(di):
    result = {'A': set(), 'B': set(), 'C': set(), 'D': set(), 'E': set()}

    for name, grade in di.items():
        result[grade].add(name)

    return result

# 4
def highest_scores(di):
    all_scores = [score for scores in di.values() for score in scores]

    if not all_scores:
        return set()

    max_score = max(all_scores)

    return {name for name, score in di.items() if max_score in score}

# 5
def course_average(di):
    result = {}

    for name, scores in di.items():
        m1, m2, final = scores
        avg = m1 * 0.3 + m2 * 0.3 + final * 0.4
        rounded_avg = math.ceil(avg)
        result[name] = rounded_avg

    return result

# 6
def list_to_dict(li):
    counts = {}

    for num in li:
        counts[num] = counts.get(num, 0) + 1

    return counts

# 7
def dict_to_list(di):
    result = []

    for key, value in di.items():
        result.extend([key] * value)

    return result

# 8
def most_cats(di):
    max_count = -1
    max_person = ''

    for name, pets in di.items():
        cats = pets.get('Cats', 0)
        if cats > max_count:
            max_count = cats
            max_person = name

    return max_person

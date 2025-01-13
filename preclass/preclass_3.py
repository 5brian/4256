def high_grades(di):
    result = {}

    for student, grades in di.items():
        count = sum(1 for grade in grades if grade >= 90)
        result[student] = count

    return result

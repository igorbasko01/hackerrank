# https://www.hackerrank.com/challenges/grading/problem


def grading_students(grades):
    result = []
    for g in grades:
        if g < 38:
            result += [g]
        else:
            closest_g = (int(g / 5) + 1) * 5
            if closest_g - g < 3:
                result += [closest_g]
            else:
                result += [g]
    return result

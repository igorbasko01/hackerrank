# https://www.hackerrank.com/challenges/breaking-best-and-worst-records/problem


def breaking_records(scores):
    max_score = scores[0]
    min_score = scores[0]
    min_changes = 0
    max_changes = 0
    for s in scores[1:]:
        if s < min_score:
            min_score = s
            min_changes += 1
        if s > max_score:
            max_score = s
            max_changes += 1
    return [max_changes, min_changes]

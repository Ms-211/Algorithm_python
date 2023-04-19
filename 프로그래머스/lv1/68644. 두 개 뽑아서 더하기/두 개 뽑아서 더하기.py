def solution(numbers):
    from itertools import combinations

    return sorted(list(set(map(sum,combinations(numbers,2)))))
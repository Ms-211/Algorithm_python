def solution(number):
    from itertools import combinations
    return list(map(sum,combinations(number,3))).count(0)
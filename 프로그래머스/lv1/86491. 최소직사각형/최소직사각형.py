def solution(sizes):
    return max(list(map(max,sizes))) * max(list(map(min,sizes)))


# 1. w,h중 가장 큰 값을 찾고 그중에서 max를 찾는다
# 2. w,h중 가장 작은 값을 찾고 그중에서 max를 찾는다.
# 3. 곱한다
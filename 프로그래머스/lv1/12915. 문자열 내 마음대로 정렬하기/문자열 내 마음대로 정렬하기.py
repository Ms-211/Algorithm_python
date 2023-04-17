def solution(strings, n):
    strings.sort()
    return sorted(strings, key = lambda x : x[n])

# 1. 각 리스트의 원소의 인덱스 n을 찾는다.
# 2. 비교후 정렬한다.
# 3. 사전순으로 확인한다.

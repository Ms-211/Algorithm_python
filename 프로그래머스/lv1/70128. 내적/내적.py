def solution(a, b):
    result = [a[i]*b[i] for i in range(len(a))]

    return sum(result)
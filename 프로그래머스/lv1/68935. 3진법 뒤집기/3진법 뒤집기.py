def solution(n):
    answer = 0
    result = ''

    while n > 0:
        n, mod  = divmod(n,3)
        result += str(mod)
             
    return int(result,3)


# n을 3으로 계속 나눠
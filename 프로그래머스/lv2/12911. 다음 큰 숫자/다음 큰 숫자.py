def solution(n):
    answer = 0
    
    first_n = bin(n)[2:].count('1')
    
    cnt = 1
    
    while True:
        second_n = bin(n+cnt)[2:].count('1')
        if(first_n == second_n):
            return n+cnt
        cnt += 1

    return answer


# n을 2진수로 변환해서 1의 갯수를 샌다.
# n+1를 2진수로 변환해서 1의 갯수를 샌다.
# n+1의 1의 수와 n의 1의 수가 같으면 10진수로 변환해서 리턴한다.
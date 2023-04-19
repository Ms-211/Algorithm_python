def solution(a, b, n):
    cnt = 0
    
    while n >= a:
        remain = n % a
        n = n // a * b
        cnt += n
        n += remain
    return cnt

    
    
    
    
    
# 마트에 줘야되는 빈병 수 a개
# 빈병 a개를 주면 받을 수 있는 콜라 b개
# 가지고 있는 빈병 n개

# 1. n을 a개로 나눈 몫과 나머지를 가지고 있는다.
# 2. 몫 * b개 를 cola 에 더한다
# 3. 나머지 + 몫*b개를 초기값으로 다시 반복한다.
# 4. 초기값이 a보다 작으면 종료한다.

#  재귀로 푸는 방법
# def solution(a, b, n):
#     if n < a:
#         return 0
    
#     cola = n // a * b
#     rest = n % a

#     return cola + solution(a,b,rest + cola)
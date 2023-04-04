def solution(n):
    su = '수'
    bak = '박'
    answer = ''
    
    if n % 2 == 0:
        answer = (su+bak) * (n//2)
    else: 
        answer = (su+bak) * (n//2) + su
    return answer
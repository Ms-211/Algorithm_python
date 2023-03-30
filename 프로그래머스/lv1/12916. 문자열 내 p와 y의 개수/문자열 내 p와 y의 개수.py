def solution(s):
    answer = False
    
    count_p = s.lower().count('p')
    count_s = s.lower().count('y')
    
    if count_p == count_s:
        answer = True

    return answer
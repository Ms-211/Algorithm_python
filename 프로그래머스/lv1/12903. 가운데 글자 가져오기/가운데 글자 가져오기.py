def solution(s):
    answer = ''
    a = len(s)//2
    if len(s) % 2 == 0:
        answer = s[a-1:a+1]
    else: 
        answer = s[a:a+1]
    
    return answer
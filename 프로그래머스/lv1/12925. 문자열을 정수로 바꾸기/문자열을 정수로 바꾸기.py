def solution(s):
    
    if s[0] == '-':
        num = s[1:]
        answer =  -1 * int(num)
    else:
        answer = int(s)    
    return answer
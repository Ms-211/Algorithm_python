def solution(n):
    answer = 0
    length = str(n)
    
    for i in range(len(length)):
        answer += int(length[i])
    return answer
def solution(k, score):
    answer = []
    result = []

    for i in score:
        result.append(i)
        result = sorted(result, reverse=True)[:k] 
        
        answer.append(min(result))    
            
    return answer

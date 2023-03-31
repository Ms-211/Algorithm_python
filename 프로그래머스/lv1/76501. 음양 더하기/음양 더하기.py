def solution(absolutes, signs):
    result = [absolutes[i] if signs[i] else absolutes[i] * -1 for i in range(len(signs))]
    
    return sum(result)
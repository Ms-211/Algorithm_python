def solution(food):
    answer = []
    
    for i in range(len(food)):
        if food[i] >= 2:
            answer.append(str(i) * (food[i]//2))
    
    result = ''.join(answer) + '0' + ''.join(sorted(answer, reverse = True))         
        
    return result


# 1. 1명은 왼쪽부터 오른쪽, 다른 1명은 오른쪽부터 왼쪽
# 2. 중앙에 먼저 다다르면 이김

# food의 원소가 2 이상이면 인덱스 값을 넣고 아니면 안넣음
# 절반씩 넣고 '0' 넣고 거꾸로 정렬해서 붙이기

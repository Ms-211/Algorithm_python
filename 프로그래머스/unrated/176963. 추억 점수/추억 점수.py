def solution(name, yearning, photo):
    answer = []
    
    dic = {name:point for name, point in zip(name,yearning)}
    
    for names in photo:
        total = 0
        for name in names:
            if name in dic:
                total += int(dic.get(name))
        answer.append(total)        
    return answer

# 1.이름, 점수를 dict 형식으로 바꾸고
# 2.배열을 돌면서 value 값으로 치환
# 3. int sum 출력
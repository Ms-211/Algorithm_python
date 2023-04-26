def solution(answers):
    one = [1,2,3,4,5]
    two = [2,1,2,3,2,4,2,5]
    three = [3,3,1,1,2,2,4,4,5,5]
    
    point = [0,0,0]
    answer = []
    
    for i in range(len(answers)):
        if answers[i] == one[i%len(one)]:
            point[0] += 1
        
        if answers[i] == two[i%len(two)]:
            point[1] += 1     
        
        if answers[i] == three[i%len(three)]:
            point[2] += 1
    
    for i in range(len(point)):
        if point[i] == max(point):
            answer.append(i+1)
    return answer


# 1번 규칙 : 1,2,3,4,5           (5개)
# 2번 규칙 : 2,1,2,3,2,4,2,5     (8개)
# 3번 규칙 : 3,3,1,1,2,2,4,4,5,5 (10개)
# 최소 10개는 검사해야함 공배수?

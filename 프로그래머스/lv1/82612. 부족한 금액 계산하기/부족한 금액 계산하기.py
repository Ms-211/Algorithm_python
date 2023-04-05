def solution(price, money, count):
    answer = 0
    total = sum(i*price for i in range(1,count+1))
        
    if total < money:
        answer = 0
    else:
        answer = total - money
        
    return answer
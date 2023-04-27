from itertools import combinations

def solution(nums):
    cnt = 0
    three = list(map(sum,combinations(nums,3)))
    
    for i in three:
        for j in range(2,i):
            if i % j == 0:
                break
        else:
            cnt += 1
    return cnt
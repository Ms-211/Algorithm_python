def solution(d, budget):
    cnt = 0
    d.sort()

    for i in range(len(d)):
        if budget < d[i]:
            break
        else:
            budget -= d[i]  
            cnt += 1
    return cnt

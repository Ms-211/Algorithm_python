def solution(t, p):
    cnt = 0
    for i in range(len(t)):
        if len(t[i:i+len(p)]) < len(p):
            break
        else:
            temp = t[i:i+len(p)]
            if int(temp) <= int(p):
                cnt += 1
    return cnt
def solution(n, m):
    answer = []

    d_n = divisor(n)
    d_m = divisor(m)
    intersec = d_n.intersection(d_m)
    # 최대 공약수
    GCD = max(intersec)
    LCM = n*m // GCD

    answer.append(GCD)
    answer.append(LCM)
    
    return answer

def divisor(n):
    result = [i for i in range(1,(n//2)+1) if n % i == 0] + [n]
    return set(result)
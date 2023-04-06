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



# 풀고나서 찾아본 방식

# # 최대 공약수
# def GCD(x,y):
# 	# y가 참일동안 == 자연수일 때 == a % b != 0
# 	while(y)
# 		x,y = y, x%y
# 	return x

# # 최소 공배수
# def LCM(x,y):
# 	result = (x*y) // GCD(x,y)
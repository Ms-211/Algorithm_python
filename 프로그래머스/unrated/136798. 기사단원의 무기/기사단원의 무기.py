def solution(number, limit, power):
    result = []
    over_limit = 0

    for i in range(1,number+1):
        count = 0
        for j in range(1,int(i**0.5+1)):
            if i % j == 0:
                if j**2 != i:
                    count += 2
                else:
                    count += 1
                
        if count <= limit:
            result.append(count)
        else:
            over_limit += 1
        
    return sum(result) + over_limit*power


# 기사 번호의 약수의 갯수가 공격력
# 정해진 max 공격력을 넘는다면 정해진 값으로 간다.
# 공격력 1당 철 1키로그램 --> sum 철값
# 기사단원의 수 number
# 제한수치 limit
# 넘은 기사의 공격력 power
# return 철의 무게

# 약수 최적화
# 임의의 자연수 N의 약수들 중에서 두 약수의 곱이 N이 되는 약수 A와 약수 B는 반드시 존재한다. (N = A * B)
# 즉, 자연수 N의 제곱근까지 약수를 구하면 그 짝이 되는 약수는 자동으로 구해진다, (i, n// i)

# - N = A * B 일떄 (A == B) 일 수 있기 때문에 값을 중복해서 넣지 않게 if문으로 같으면 cnt를 1만 해주도록 한다.
# - 나머지는 2씩 추가

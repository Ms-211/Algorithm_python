def solution(s):
    answer = []
    dict ={}
    for i,j in enumerate(s):
        if s[:i].find(j) != -1:
            answer.append(i - dict[j])
        else:
            answer.append(s[:i].find(j))
        dict[j] = i
    print(answer)
    return answer


# 리스트를 앞만 비교하는거니까 슬라이싱으로 땡겨가면서 비교




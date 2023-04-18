def solution(array, commands):
    
    return [sorted(array[i[0]-1:i[1]])[i[2]-1] for i in commands]
    
    # 1번 풀이
    # for i in commands:
        # first = array[i[0]-1:i[1]]
        # second = sorted(first)
        # third = second[i[2]-1]
        # answer.append(third)
        
    # 2번 풀이
    # answer = []
    # for i in commands:
    #   answer.append(sorted(array[i[0]-1:i[1]])[i[2]-1])
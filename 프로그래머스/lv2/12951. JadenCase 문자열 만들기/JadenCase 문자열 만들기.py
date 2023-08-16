def solution(s):
    words = s.split(" ")
    answer_list = []
        
    for word  in words:
        answer_list.append(word.capitalize())
        
    answer = ' '.join(answer_list)

    return answer


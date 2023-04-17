def solution(s):
    answer = ''
    dic_num = {'zero':'0','one':'1','two':'2','three':'3','four':'4','five':'5','six':'6','seven':'7','eight':'8','nine':'9'}
    split_s = list(s)
    
    temp = ''
    for i in split_s:
        if i.isdigit():
            answer += i
            continue
            
        temp += i
        if temp in dic_num:
            answer += dic_num.get(temp)
            temp = ''
        else:
            continue
        
    return int(answer)
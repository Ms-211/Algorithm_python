def solution(s):
    list_s = s.split(' ')
    
    for i in range(len(list_s)):
        word_s = list(list_s[i])
        for j in range(len(word_s)):
            if j % 2 == 0:
                word_s[j] = word_s[j].upper()
            else:
                word_s[j] = word_s[j].lower()
        list_s[i] = ''.join(word_s)
    
    result = ' '.join(list_s)                

    return result
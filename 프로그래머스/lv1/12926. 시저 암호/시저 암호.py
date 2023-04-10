def solution(s, n):
    list_s = list(s)
    cnt = 0
    for word in list_s:
        if word == ' ':
            cnt += 1
            continue
        else:
            if (word.isupper() and int(ord(word)) + n > 90) or (word.islower() and (int(ord(word) + n) > 122)):
                temp = (int(ord(word)) + n) - 26
            else:
                temp = int(ord(word)) + n
            list_s[cnt] = chr(temp)
            cnt += 1
    print(''.join(list_s))
    return ''.join(list_s)

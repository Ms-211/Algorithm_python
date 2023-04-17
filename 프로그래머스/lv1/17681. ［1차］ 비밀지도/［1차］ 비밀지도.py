def solution(n, arr1, arr2):
    answer = []
    for i in range(n):
        list_ar = bin(arr1[i] | arr2[i])
        list_ar = list_ar[2:].zfill(n)
        list_ar = list_ar.replace('1','#').replace('0',' ')
        answer.append(list_ar)
        
    return answer


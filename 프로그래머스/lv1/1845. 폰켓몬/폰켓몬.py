def solution(nums):
    pon = set(nums)
    choice = len(nums)//2

    
    if choice < len(pon):
        return choice
    else:
        return len(pon)

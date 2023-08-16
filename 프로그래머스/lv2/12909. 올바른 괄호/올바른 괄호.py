def solution(s):
    stack = []
    if s[0] == ')' or s[-1] == '(':
        return False
        
    for i in s:
        if i == '(':
            stack.append('(')
        else:
            if not stack:
                return False
            stack.pop()
            
    if not stack:
        return True
    else:
        return False
    
    
    # ())(()
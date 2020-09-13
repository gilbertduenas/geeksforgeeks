# https://www.geeksforgeeks.org/check-for-balanced-parentheses-in-python/

def check_paren(s):
    start = ['[', '{', '(']
    close = [']', '}', ')']
    valid = []
    
    for i in s:
        if i in start:
            valid.append(i)
        elif i in close:
            index = close.index(i)
            if ((len(valid) > 0) and (start[index] == valid[len(valid)-1])):
                valid.pop()
            else:
                return 'Unbalanced'
                
    if len(valid) == 0:
        return 'Balanced'
    else:
        return 'Unbalanced'

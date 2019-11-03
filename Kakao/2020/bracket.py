def _is_gyun(str):
    left_count = 0
    right_count = 0
    for i in list(str):
        if i == '(':
            left_count += 1
        else: 
            right_count += 1
    return left_count == right_count


def _is_all(str):
    stack = []
    for i in list(str):
        if i == '(':
            stack.append(i)
        elif len(stack) > 0:
            stack.pop()
    
    return len(stack) == 0


def _seperate(str1):
    if _is_all(str1):
        return str1, ''

    left_count = 0
    right_count = 0

    for c in list(str1):
        if c == '(':
            left_count += 1
        else:
            right_count += 1
        if left_count == right_count:
            return str1[:left_count*2], str1[left_count*2:]


def solution(p):
    if p == '':
        return ''

    u, v = _seperate(p)
    if _is_all(u):
        return u + solution(v)
    else:
        temp_str = '(' + solution(v) + ')'

        temp = ''
        for c in u[1:-1]:
            if c == '(':
                temp += ')'
            else:
                temp += '('
    
    return temp_str + temp

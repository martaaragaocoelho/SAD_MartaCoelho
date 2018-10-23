def solution(S):
    if ((S[0] == '{' and S[-1] == '}') or (S[0] == '[' and S[-1] == ']')):
        return '1'
    elif ((S[0] == '(' and S[-1] == ')') or (S[0:] == ' ')):
        return '1';
    else:
        return '0'            
print(solution('{[() ()]}'))

# P va Q ni hisoblaydi 1 ta qiymatda
def truth_value(P, Q):
    result = P & Q
    return result

result = truth_value(1, 0)
print(f'Result = {result}')
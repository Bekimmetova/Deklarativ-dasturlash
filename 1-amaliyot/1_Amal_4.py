#Bu funksiya x sonini y darajaga oshiradi
def st(x, y):
    if y == 1:
        return x
    elif y > 1:
        return st(x, y - 1) * x

result = st(2, 3)
print(result)

#Bu funksiya x sonini y darajaga oshiradi
def st(x, y):
    if y == 1:
        return x
    else:
        yy = y - 1
        zz = st(x, yy)
        return zz * x

result = st(3, 4)
print(result)

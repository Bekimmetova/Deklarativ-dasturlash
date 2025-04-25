#ro‘yxatdagi barcha elementlarning musbatligini tekshiradi.
def all_positive(lst):
    return all(x > 0 for x in lst)

result = all_positive([1, 2, 3])

print(result)

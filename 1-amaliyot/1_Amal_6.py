# Royxatdagi elementlar sonini rekursiya yordamida hisoblovchi funksiya
def list_length(lst):
    if not lst:  # Agar ro‘yxat bo‘sh bo‘lsa
        return 0
    else:
        return 1 + list_length(lst[1:])  # Birinchi elementni hisoblab, qolganini rekursiv chaqiradi

print(list_length([123446, 232, 2332, 23]))  
# Natija: 4 (4 ta element bor)

print(list_length([123446, 232, 2332, 23, 'sdfds', 'sdfsf', 'sdfa', 'asd']))  
# Natija: 8 (8 ta element bor — aralash son va matn)

print(list_length([]))  
# Natija: 0 (bo‘sh ro‘yxat)

print(list_length([1]))  
# Natija: 1 (bitta element bor)

print(list_length([1, 9, 8, 7, 6, 5, 4, 3, 2]))  
# Natija: 9 (9 ta son)

# 1-usul — oddiy iteratsiya (eng oson tushuniladigan)
sonlar = [5, 8, 3, 12, 7, 2, 10, 6, 15, 4]

# Minimal qiymatni boshlang'ich sifatida birinchi elementni olamiz
min_qiymat = sonlar[0]

# Minimal qiymatni izlash
for qiymat in sonlar:
    if qiymat < min_qiymat:
        min_qiymat = qiymat

# Minimal qiymatni chiqarish
print("Minimal qiymat:", min_qiymat)



# 2-usul — rekursiya (biroz ilg‘or, lekin chiroyli va funksional usul)
def min_top(royxat, hozirgi_min=None):
    if not royxat:
        return hozirgi_min
    else:
        bosh, *qolgan = royxat
        yangi_min = bosh if hozirgi_min is None or bosh < hozirgi_min else hozirgi_min
        return min_top(qolgan, yangi_min)

# Misol ma'lumotlar
mening_royxatim = [5, 8, 3, 12, 7, 2, 10, 6, 15, 4]

# Funksiyani chaqirish
natija = min_top(mening_royxatim)

# Minimal qiymatni chiqarish
print("Minimal qiymat:", natija)

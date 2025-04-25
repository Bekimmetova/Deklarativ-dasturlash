# Faktorialni hisoblash funktsiyasini ta'riflash
def faktorial(n):
    if n == 0:
        return 1
    else:
        return n * faktorial(n - 1)

# Misol sifatida foydalanish
natija = faktorial(5)  # 5 sonining faktorialini hisoblash

# Natijani chiqarish
print(natija)

#P VA Q hisoblaydi
def haqiqat_jadvali():
    sarlavha = ["P", "Q", "P VA Q"]
    print("|".join(sarlavha))

    for P in [0, 1]:
        for Q in [0, 1]:
            natija = P & Q
            qator = [str(P), str(Q), str(natija)]
            print("|".join(qator))

# Haqiqat jadvalini yaratish uchun funksiyani chaqirish
haqiqat_jadvali()

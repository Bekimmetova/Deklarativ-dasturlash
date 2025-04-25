class Mahsulot:
    def __init__(self, mahsulot_nomi, narx):
        self.mahsulot_nomi = mahsulot_nomi
        self.narx = narx

# Savatchadagi mahsulotlarning umumiy narxini hisoblash uchun funksiya
def umumiy_narx(mahsulotlar):
    return sum(mahsulot.narx for mahsulot in mahsulotlar)

# Misol sifatida foydalanish
if __name__ == "__main__":
    savat = [
        Mahsulot("Laptop", 1200.0),
        Mahsulot("Smartfon", 699.99),
        Mahsulot("Quloqchinlar", 99.95)
    ]

    print("Savatdagi mahsulotlar:")
    for mahsulot in savat:
        print(f"{mahsulot.mahsulot_nomi}: ${mahsulot.narx}")

    print(f"\nUmumiy narx: ${umumiy_narx(savat)}")

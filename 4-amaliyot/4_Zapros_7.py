class Talaba:
    def __init__(self, ism, baho):
        self.ism = ism
        self.baho = baho

# Talabalar o'rtacha bahosini hisoblash uchun funksiya
def ortacha_baho(talabalar):
    return sum(talaba.baho for talaba in talabalar) / len(talabalar)

# Misol sifatida foydalanish
if __name__ == "__main__":
    talaba_royxati = [
        Talaba("Alice", 85.0),
        Talaba("Bob", 92.5),
        Talaba("Charlie", 78.3),
        Talaba("David", 89.7)
    ]

    print("Talabalar ro'yxati va baholari:")
    for talaba in talaba_royxati:
        print(f"{talaba.ism}: {talaba.baho}")

    print(f"\nO'rtacha baho: {ortacha_baho(talaba_royxati)}")

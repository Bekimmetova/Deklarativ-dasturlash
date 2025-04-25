# Shaxsning onasi kimligini aniqlovchi funksiya
def mother(person):
    mothers = {"дочь1": "Наташа", "дочь2": "Ольга", "дочь3": "Марина"}  # Har bir qizga mos ona
    return person in mothers and mothers[person]  # Agar bor bo‘lsa, onasini qaytaradi

# Ayol (qiz bola) ekanligini tekshiruvchi funksiya
def women(person):
    daughters = ["дочь1", "дочь2", "дочь3"]  # Qizlar ro'yxati
    return person in daughters  # Agar shaxs shu ro'yxatda bo‘lsa, True

# Yoshlikni aniqlovchi funksiya
def age(person):
    ages = {"дочь1": 20, "дочь2": 25, "дочь3": 18}  # Har bir qizning yoshi
    return ages.get(person, 0)  # Agar shaxs bor bo‘lsa, yoshini qaytaradi, aks holda 0


# Qiz bola voyaga yetganmi (18+) va onasi ma'lummi — shuni tekshiradi
def full_age_daughter(mother, daughter, age):
    return mother(daughter) and women(daughter) and age(daughter) >= 18
# Misol uchun foydalanish
result = full_age_daughter(mother, "дочь1", age)  # "дочь1" — bu 20 yoshli, onasi bor

# Natijani chop etish
print(result)  # True




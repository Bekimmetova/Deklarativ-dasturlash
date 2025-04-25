import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# mtcars ma'lumotlar to'plamini yuklash
mtcars = sns.load_dataset("mpg")

# Ma'lumotlarning dastlabki satrlarini chiqarish
print(mtcars.head())

# Ot kuchi (horsepower) va yoqilg'i sarfi (mpg) o'rtasidagi bog'liqlikni vizualizatsiya qilish
plt.figure(figsize=(8, 6))
sns.scatterplot(x="horsepower", y="mpg", data=mtcars, color="blue")
plt.title("Ot kuchi va MPG o'rtasidagi Scatterplot")
plt.xlabel("Ot kuchi")
plt.ylabel("MPG")
plt.show()

# Ot kuchi va yoqilg'i sarfi o'rtasidagi korrelyatsiya koeffitsiyentini hisoblash
correlation = mtcars["horsepower"].corr(mtcars["mpg"])
print(f"Ot kuchi va MPG o'rtasidagi korrelyatsiya: {correlation:.2f}")

# Yoqilg'i sarfi taqsimotining gistogrammasini qurish
plt.figure(figsize=(8, 6))
sns.histplot(mtcars["mpg"], bins=20, color="green", kde=True)
plt.title("MPG ning Gistogrammasi")
plt.xlabel("MPG")
plt.show()

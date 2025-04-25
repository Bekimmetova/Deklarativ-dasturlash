
import numpy as np
import matplotlib.pyplot as plt

# Tasodifiy ma'lumotlarni yaratish
data = np.random.normal(loc=10, scale=2, size=100)

# Gistogramma yaratish
plt.hist(data, bins=20, color="lightblue", edgecolor="black")
plt.title("Tasodifiy Ma'lumotlarning Gistogrammasi")
plt.xlabel("Qiymatlar")
plt.show()

# O'rtacha qiymatni hisoblash
mean_value = np.mean(data)
print(f"O'rtacha qiymat: {mean_value}")
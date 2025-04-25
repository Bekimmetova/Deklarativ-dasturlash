# 1-usul: oddiy tsikl bilan yig'indi hisoblash
numbers = [1, 2, 3, 4, 5]
total = 0
for num in numbers:
    total += num
print(total)

# 2-usul: sum() funksiyasi yordamida yig‘indi hisoblash
numbers = [1, 2, 3, 4, 5]
total = sum(numbers)
print(total)

# 3-usul: Klass (sinflar) orqali yig‘indi hisoblash
class Calculator:
    def __init__(self, numbers):
        self.numbers = numbers

    def calculate_total(self):
        return sum(self.numbers)

numbers = [1, 2, 3, 4, 5]
calc = Calculator(numbers)
total = calc.calculate_total()
print(total)

# 4-usul: Har bir elementni 2 ga ko‘paytirib, so‘ngra yig‘indi hisoblash
numbers = [1, 2, 3, 4, 5]
total = sum(map(lambda x: x * 2, numbers))
print(total)

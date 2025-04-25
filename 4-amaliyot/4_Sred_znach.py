

# sonlarning o'rtachasini hisoblash funksiyasi
def average(numbers):
    return sum(numbers) / len(numbers) if len(numbers) > 0 else 0

# misol
if __name__ == "__main__":
    numeric_list = [1.0, 2.5, 3.0, 4.5, 5.0]
    print("Original List:", numeric_list)
    print("Average:", average(numeric_list))

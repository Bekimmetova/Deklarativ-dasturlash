# -*- coding: utf-8 -*-
"""
Created on Mon Jan  1 23:14:03 2024

@author: Admin
"""

from kanren import run, fact, var, Relation

# Определение переменных
X = var()

# Определение отношений
animal = Relation()
predator = Relation()

# Добавление фактов
fact(animal, 'lion')
fact(animal, 'tiger')
fact(animal, 'rabbit')

# Правило: хищник - это животное, если оно лев или тигр
def rule_predator(x):
    return animal(x), (x == 'lion') | (x == 'tiger')

# Добавление правила в базу знаний
fact(predator, 'lion', True)
fact(predator, 'tiger', True)
fact(predator, 'rabbit', rule_predator)

# Запрос: Является ли кролик хищником?
result = run(1, X, predator('rabbit', True))

# Вывод результата
if result:
    print(f"Кролик является хищником: {result}")
else:
    print("Кролик не является хищником.")

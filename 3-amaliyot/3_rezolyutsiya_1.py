# -*- coding: utf-8 -*-
"""
Created on Mon Jan  1 23:07:36 2024

@author: Admin
"""

from kanren import run, eq, Relation, facts, var, lall

# Определение переменных
Student = var()

# Определение отношений
students = Relation()
courses = Relation()
attends = Relation()

# Добавление фактов
facts(students, 'john')
facts(students, 'mary')
facts(students, 'bob')
facts(courses, 'math')
facts(courses, 'physics')
facts(courses, 'english')

# Добавление фактов посещения курсов отдельно
facts(attends, ('john', 'math'))
facts(attends, ('john', 'physics'))
facts(attends, ('mary', 'math'))
facts(attends, ('bob', 'physics'))
facts(attends, ('bob', 'english'))

# Правило: успешный студент - тот, кто посещает курс "Математика"
def successful_student(x):
    return lall((students, x), (attends, x, 'math'))

# Запрос: Кто из студентов успешно посещает курс "Математика"?
result = run(1, Student, successful_student(Student))

# Вывод результата
if result:
    print(f"Студенты, успешно посещающие курс 'Математика': {result}")
else:
    print("Нет успешных студентов.")

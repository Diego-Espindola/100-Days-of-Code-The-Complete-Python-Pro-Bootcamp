# new_dict = {new_key:new_value for item in list}

# new_dict = {new_key:new_value for (key, value) in dict.items()}

# new_dict = {new_key:new_value for (key, value) in dict.items() if test}
import random as r
names = ["Angela", "Beth", "Caroline", "Dave", "Elanor", "Freddie"]
students_scores = {name: r.randint(1,100) for name in names}
# print(students_scores)

passed_students = {student: score for (student, score) in students_scores.items() if score > 60}
# print(passed_students)

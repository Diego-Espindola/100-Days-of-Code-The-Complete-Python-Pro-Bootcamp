from nutritionix import Nutritionix

natural_language_exercise = input("Tell me which exercises you did:\n")

result = Nutritionix.request_exercise(natural_language_exercise)
print(result)
for exercise in result['exercises']:
    name = exercise.get('name')
    duration = exercise.get('duration_min')
    calories = exercise.get('nf_calories')
